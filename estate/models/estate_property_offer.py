from odoo import api, fields, models, _
from odoo.exceptions import UserError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate property offer"

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            if record.property_id.state == "new":
                record.property_id.state = "offer_received"
        return records

    price = fields.Float("Expected Price")
    status = fields.Selection(
        string="Status", selection=[("yes", "Accepted"), ("no", "Refused")], copy=False
    )
    validity = fields.Integer(default=7)
    offer_creation_date = fields.Date(default=fields.Date.today())
    deadline = fields.Date(
        "Offer Deadline", compute="_compute_deadline", inverse="_inverse_deadline"
    )

    partner_id = fields.Many2one(
        'res.partner',
        string='Buyer',
        ondelete='restrict',
        default=lambda self: self.env.user.partner_id,
        required=True,
    )
    property_id = fields.Many2one(
        'estate.property', string='Property', ondelete='restrict', required=True
    )

    @api.depends("validity", "offer_creation_date")
    def _compute_deadline(self):
        for record in self:
            record.deadline = fields.Date.add(
                record.offer_creation_date, days=record.validity
            )

    def _inverse_deadline(self):
        for record in self:
            record.validity = (record.deadline - record.offer_creation_date).days

    def action_accept_offer(self):
        for record in self:
            for offer in record.property_id.offer_ids:
                if offer.status == "yes":
                    raise UserError(_("Already accepted an offer for this property."))
            record.status = "yes"
            record.property_id.buyer_id = record.partner_id
            record.property_id.selling_price = record.price
            record.property_id.state = "offer_accepted"
        return True

    def action_reject_offer(self):
        for record in self:
            record.property_id.buyer_id = None
            record.property_id.selling_price = 0
            record.status = "no"
        return True
