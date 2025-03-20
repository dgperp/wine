# -*- coding: utf-8 -*-
{
    'name': 'Product Class',
    'version': '15.0.1.0.0',
    'category': 'Warehouse',
    'summary': 'Product Class',
    'author': 'Wiroot.KL',
    'company': 'TOA',
    'maintainer': 'Wiroot.KL',
    'images': ['static/description/banner.png'],
    'website': 'https://www.toagroup.com',
    'depends': ['product_brand'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_class_views.xml',
        'views/product_sub_class_views.xml',
        'views/product_views.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,

}
