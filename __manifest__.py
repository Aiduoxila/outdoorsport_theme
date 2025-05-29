# Manifest file for Outdoorsport theme
{
    'name': 'Outdoorsport Theme',
    'description': 'A bold adventure look with earthy tones and vibrant accents.',
    'version': '1.0',
    'author': 'Your Name',
    'category': 'Theme',
    'depends': ['base'],
    'data': [
        'views/templates.xml',
        'views/snippets.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'static/src/scss/styles.scss',
            'static/src/js/banner.js',
            'static/src/img/*'
        ]
    }
}