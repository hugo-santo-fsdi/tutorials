# -*- coding: utf-8 -*-
{
    'name': "Estate Tutorial",
    'summary': """
        Real estate tutorial module
    """,
    'description': """
        Real estate tutorial module
    """,
    'version': '0.5',
    'application': True,
    'category': 'Tutorials',
    'installable': True,
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'estate/static/src/dashboard/**/*',
        ],
    },
    'author': 'Odoo S.A.',
    'license': 'AGPL-3',
}
