# -*- coding: utf-8 -*-
{
    'name': 'Partner-Multi-Address',
    'version': '0.1',
    'category': 'Tools',
    'description': """
This module is for managing a partner multiaddress environment.
=======================================================

This module is the ext module for other multi-address modules.
    """,
    'author': 'LiangJia@qq.com',
    'website': 'http://www.duuge.com',
    'depends': [
        'base',
        'sale_stock',
    ],
    'data': ['res_address_view.xml'],
    'demo': ['multi_address_demo.xml'],
    'installable': True,
    'auto_install': False,
}