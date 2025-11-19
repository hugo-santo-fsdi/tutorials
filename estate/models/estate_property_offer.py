from odoo import fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate property offer"

    price = fields.Float("Expected Price")
    status = fields.Selection(
        string="Status", selection=[("yes", "Accepted"), ("no", "Refused")], copy=False
    )

    partner_id = fields.Many2one(
        'res.partner',
        string='Salesman',
        ondelete='restrict',
        default=lambda self: self.env.user.partner_id,
        required=True,
    )

    property_id = fields.Many2one(
        'estate.property', string='Property', ondelete='restrict', required=True
    )
