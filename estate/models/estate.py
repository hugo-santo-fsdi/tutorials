from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"

    _description = "Estate property model"
    name = fields.Char('Property name', required=True,)
    description = fields.Text('Property description')
    postcode = fields.Char()
    expected_price = fields.Float('Property expected price', required = True)
    date_availability = fields.Date()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string = 'Orientation',selection=[("north", "N"), ("south", "S"), ("east", "E"), ("west", "W")], help = 'Orientation of the garden')
