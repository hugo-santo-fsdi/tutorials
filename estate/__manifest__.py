{
    'name': "Real Estate",

    'summary': """
        Cool Real Estate App
    """,
    'description': """
        Cool Real Estate App
    """,
    'author': "kmhma",
    'website': "https://www.odoo.com/",
    'category': 'Tutorials',
    'version': '0.1',
    'application': True,
    'installable': True,
    'depends': ['base'],

    'data': [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_menus.xml",
        "views/estate_list_view.xml",
        "views/estate_form_view.xml",
        "views/estate_search_view.xml",
    ],
    'assets': {
    },
    'license': 'AGPL-3'
}
