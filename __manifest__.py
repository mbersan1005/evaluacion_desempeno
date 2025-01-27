{
    'name': 'Gestión de vehículos',
    'version': '1.0',
    'summary': 'Gestión de vehículos de la empresa',
    'description': 'Este módulo gestiona los vehículos disponibles en la empresa.',
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