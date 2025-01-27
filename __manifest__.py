{
    'name': 'Evaluación de desempeños',
    'version': '1.0',
    'summary': 'Gestión de evaluación de desempeño',
    'description': 'Este módulo gestiona las evaluaciones de desempeño de los empleados.',
    'author': 'Miguel Ángel Bernal Sánchez',
    'category': 'Tools',
    'depends': ['base'],
    'icon': '/evaluacion_desempeno/static/description/icono.png',
    'data': [
        'security/ir.model.access.csv', # Control de acceso
        'views/evaluacion_desempeno_views.xml', # Vista del módulo
    ],
    'installable': True,
    'application': True,
}