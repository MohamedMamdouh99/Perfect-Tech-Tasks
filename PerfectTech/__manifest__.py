# -*- coding: utf-8 -*-

{
    'name': 'Perfect Tech',
    'version': '1.0.0',
    'sequence': '-1',
    'category': 'Task',
    'author': 'Mohamed Mamdouh',
    'summary': 'Development Task',
    'description': """
    """,
    'depends': ['base'],
    'data': [
        'security\ir.model.access.csv',
        'views\partner.xml',
        'views\menu.xml',
        'views\student_registration.xml',
        'views\student.xml',
        'views\student.invoice.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
}
