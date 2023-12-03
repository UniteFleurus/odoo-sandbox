# -*- coding: utf-8 -*-

{
    'name': 'Scout app',
    'version': '1.1',
    'category': 'Sales/Sales',
    'summary': 'Jab, Goeland et Verdier',
    'description': """
Using this application you can manage Sales Teams with CRM and/or Sales
=======================================================================
 """,
    'website': 'https://www.odoo.com/app/crm',
    'depends': ['base', 'mail', 'website'],
    'data': [
        'views/scout_views.xml',
        'views/res_partner_views.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    # 'assets': {
    #     'web.assets_backend': [
    #         'sales_team/static/**/*',
    #     ],
    # },
    'license': 'LGPL-3',
}
