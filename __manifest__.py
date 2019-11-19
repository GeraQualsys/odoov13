{
    'name': 'cambios',
    'version': '1.2',
    'category': 'Uncategorized',
    'sequence': 60,
    'summary': '',
    'description': "primeros cambios en la version 13 de odoo",
    'website': 'https://www.odoo.com/page/purchase',
    'depends': ['purchase', 'sale_management'],
    'data': [
        #'security/purchase_security.xml',
        'views/approved.xml',
        'views/dueS.xml',

    ],
    'demo': [
        #'data/purchase_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
