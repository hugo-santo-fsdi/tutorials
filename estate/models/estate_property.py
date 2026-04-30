# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'
    _check_expected_price = models.Constraint(
        'CHECK(expected_price > 0)',
        'The expected price must be strictly positive.',
    )
    _check_selling_price = models.Constraint(
        'CHECK(selling_price >= 0)',
        'The selling price must be positive.',
    )

    name = fields.Char(required=True)
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled'),
        ],
        default='new',
        copy=False,
    )
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    best_price = fields.Float(compute='_compute_best_price')
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    total_area = fields.Integer(compute='_compute_total_area')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),
        ]
    )

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for property_record in self:
            property_record.total_area = property_record.living_area + property_record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for property_record in self:
            property_record.best_price = max(property_record.offer_ids.mapped('price'), default=0.0)

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False

    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        for property_record in self:
            if float_is_zero(property_record.selling_price, precision_rounding=0.01):
                continue
            minimum_price = property_record.expected_price * 0.9
            if float_compare(
                property_record.selling_price,
                minimum_price,
                precision_rounding=0.01,
            ) < 0:
                raise ValidationError('The selling price cannot be lower than 90% of the expected price.')

    def action_sold(self):
        for property_record in self:
            if property_record.state == 'canceled':
                raise UserError('A canceled property cannot be sold.')
            property_record.state = 'sold'
        return True

    def action_cancel(self):
        for property_record in self:
            if property_record.state == 'sold':
                raise UserError('A sold property cannot be canceled.')
            property_record.state = 'canceled'
        return True
