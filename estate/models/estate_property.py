# -*- coding: utf-8 -*-
from odoo import fields, models


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(required=True)
