{
    'name': "Real Estate",
    'summary': """
        Testing the real estate module
    """,

    'description': """
        Testing the description real estate module
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        'views/estate_menus.xml'
    ],
    'application': True,
    'installable': True,
}
