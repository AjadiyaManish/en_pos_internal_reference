# -*- coding: utf-8 -*-
{
    'name': 'POS Internal References',
    'summary': """Added internal references for improved tracking.""",
    'description': """
        Internal references are now integrated into the Product Screen, Order Lines, 
        and Receipts, enhancing product management and accuracy throughout transactions.
    """,
    'author': "Envision Technolabs",
    'maintainer': 'Envision Technolabs',
    "website": "https://www.envisiontechnolabs.com",
    'category': 'Point of Sale',
    'version': '19.0.1.0',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'en_pos_internal_reference/static/src/app/screens/product_screen/product_screen.js',
            'en_pos_internal_reference/static/src/app/models/pos_order_line.js',
        ],
    },
    'images': ['static/description/banner.gif'],
    'price': 5,
    'currency': 'USD',
    'license': 'OPL-1',
    'application': True,
    'auto_install': False,
}
