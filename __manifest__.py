{
    'name': 'cambios',
    'version': '1.2',
    'category': 'Uncategorized',
    'sequence': 60,
    'summary': '''Cambios realizados en los módulos de 
    Ventas: Se agrego la cuenta analítica como un campo requerido.
    Compras: Se agrego un la cuenta analítica como un campo requeido.
    Campo de fecha de validez agregado en las solicitudes de compras y fecha de vencimiento de la cotización de compra
    
    ''',
    'description': "Modificaciones en los Modelos de Ventas y Compras",
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
    'application': True,
}
