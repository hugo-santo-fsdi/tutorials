from odoo import models, fields
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property model"
    
    name = fields.Char('Property name', required=True, default="Unknown")
    description = fields.Text('Property description')
    postcode = fields.Char()
    expected_price = fields.Float('Property expected price', required=True)
    date_availability = fields.Date(default=fields.Date.today() + relativedelta(months=3), copy=False)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='Orientation', selection=[("north", "N"), ("south", "S"), ("east", "E"), ("west", "W")], help='Orientation of the garden')
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    active = fields.Boolean(default=True)
    state = fields.Selection(string='State', selection=[("new", "New"), ("offer_received", "Offer Received"), ("offer_accepted", "Offer Accepted"), ("sold", "Sold"), ("cancelled", "Cancelled")], default='new')
