# -*- coding: utf-8 -*-
{
    'name': "custom employee",

    'summary': """
        Menambahkan Master Divisi""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Fits!",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_expense'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/employee_view.xml',
        'views/pengajuan_sppd.xml',
        'report/report_sppd.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}