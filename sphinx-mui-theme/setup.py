# 'setup.py'
setup(
    ...
    entry_points = {
        'sphinx.html_themes': [
            'name_of_theme = sphinx-mui-theme',
        ]
    },
    ...
)

# 'your_package.py'
from os import path

def setup(app):
    app.add_html_theme('sphinx-mui-theme', path.abspath(path.dirname(__file__))
