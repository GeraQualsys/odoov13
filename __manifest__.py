{
    'name': 'Modificaciones en modulos compras, ventas e inventario',
    'version': '1.2',
    'category': 'Uncategorized',
    'sequence': 0,
    'author':'Qualsys consulting'
    'summary': '''Se agregaron campos y se hicieron campos requeridos. 
    ''',
    'description':'''Cambios realizados en los módulos de 
    Ventas: Se agrego la cuenta analítica como un campo requerido.
    Compras: Se agrego un la cuenta analítica como un campo requeido.
    Campo de fecha de validez agregado en las solicitudes de compras y fecha de vencimiento de la cotización de compra''',
    
    'website': 'https://www.qualsys.com,mx',
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
}
