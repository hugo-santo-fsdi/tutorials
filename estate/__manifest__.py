# -*- coding: utf-8 -*-
{
    'name': "Estate",
    'summary': """
        Real estate tutorial module
    """,
    'description': """
        Real estate tutorial module
    """,
    'version': '0.4',
    'application': True,
    'category': 'Tutorials',
    'installable': True,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
    ],
    'author': 'Odoo S.A.',
    'license': 'AGPL-3',
}
