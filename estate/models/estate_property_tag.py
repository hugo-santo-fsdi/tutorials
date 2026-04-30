# -*- coding: utf-8 -*-
from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Real Estate Property Tag'
    _order = 'name'
    _name_unique = models.Constraint(
        'UNIQUE(name)',
        'The property tag name must be unique.',
    )

    color = fields.Integer()
    name = fields.Char(required=True)
