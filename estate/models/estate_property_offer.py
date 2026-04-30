# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import api, fields, models
from odoo.exceptions import UserError


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Real Estate Property Offer'

    price = fields.Float()
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_inverse_date_deadline')
    status = fields.Selection(
        selection=[
            ('accepted', 'Accepted'),
            ('refused', 'Refused'),
        ],
        copy=False,
    )
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for offer in self:
            create_date = offer.create_date.date() if offer.create_date else fields.Date.context_today(self)
            offer.date_deadline = create_date + timedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            create_date = offer.create_date.date() if offer.create_date else fields.Date.context_today(self)
            if offer.date_deadline:
                offer.validity = (offer.date_deadline - create_date).days

    @api.model_create_multi
    def create(self, vals_list):
        offers = super().create(vals_list)
        offers.mapped('property_id').write({'state': 'offer_received'})
        return offers

    def action_accept(self):
        for offer in self:
            accepted_offer = offer.property_id.offer_ids.filtered(
                lambda property_offer: property_offer.status == 'accepted' and property_offer != offer
            )
            if accepted_offer:
                raise UserError('Only one offer can be accepted for a property.')
            offer.status = 'accepted'
            offer.property_id.write({
                'buyer_id': offer.partner_id.id,
                'selling_price': offer.price,
                'state': 'offer_accepted',
            })
        return True

    def action_refuse(self):
        for offer in self:
            offer.status = 'refused'
        return True
