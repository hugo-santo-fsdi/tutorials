from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate property type"
    _name_unique = models.Constraint(
        'unique (name)',
        'A property type of that name already exists',
    )

    name = fields.Char('Property Type', required=True)
