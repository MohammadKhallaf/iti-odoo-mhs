{
    'name': 'Hospitals Management Software',
    'version': '1.0',
    'category': 'Hospital',
    'sequence': -100,
    'summary': 'Hospitals Management Software',
    'description': """Hospital Management Software""",
    'depends': ['base', 'crm'],
    'data': [
        'security/hms_groups.xml',
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/doctor.xml',
        'views/department.xml',
        'views/logs.xml',
        'views/customers.xml',
        'reports/report.xml',
        'reports/template.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
