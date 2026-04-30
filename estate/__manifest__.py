# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'summary': """
        Real estate tutorial module
    """,
    'description': """
        Real estate tutorial module
    """,
    'version': '2.3',
    'application': True,
    'category': 'Tutorials',
    'installable': True,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
    ],
    'author': 'Odoo S.A.',
    'license': 'AGPL-3',
}
