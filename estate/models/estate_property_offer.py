from odoo import api, fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate property offer"

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
        string='Salesman',
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
