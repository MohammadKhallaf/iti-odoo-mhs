{
    'name': 'Hospitals Management Software',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'sequence': -100,
    'summary': 'Hospitals Management Software',
    'description': """Hospital Management Software""",
    'depends': ['base', 'crm'],
    'data': [
        'views/patient.xml',
        'views/doctor.xml',
        'views/department.xml',
        'views/logs.xml',
        'views/customers.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
