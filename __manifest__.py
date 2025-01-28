{
    'name': 'Evaluación de Desempeño',
    'version': '1.0',
    'summary': 'Gestión de evaluaciones de desempeño de empleados',
    'description': 'Este módulo permite gestionar las evaluaciones de desempeño de los empleados, asignando puntuaciones, comentarios y estados.',
    'author': 'Miguel Ángel Bernal Sánchez',
    'category': 'Human Resources',
    'license': 'LGPL-3',
    'depends': ['base', 'hr'],  
        'icon': '/evaluacion_desempeno/static/description/icono.png',
    'data': [
        'security/ir.model.access.csv',  
        'views/evaluacion_desempeno_views.xml',  
    ],
    'assets': {
        'web.assets_backend': [
            '/evaluacion_desempeno/static/src/css/styles.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
