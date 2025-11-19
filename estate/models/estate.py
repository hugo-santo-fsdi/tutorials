from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate property model"

    name = fields.Char("Title", required=True, default="Unknown")
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    expected_price = fields.Float("Expected Price", required=True)
    date_availability = fields.Date(
        "Available From",
        default=fields.Date.add(fields.Date.today(), months=3),
        copy=False,
    )
    selling_price = fields.Float("Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string="Orientation",
        selection=[
            ("north", "N"),
            ("south", "S"), 
            ("east", "E"), 
            ("west", "W"),
        ],
        help="Orientation of the garden",
    )
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string="State",
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("cancelled", "Cancelled"),
        ],
        default="new",
    )
