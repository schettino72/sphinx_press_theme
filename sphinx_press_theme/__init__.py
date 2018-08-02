from os import path

def setup(app):
    # app.add_builder(builder,override=True)
    app.add_html_theme('press', path.abspath(path.dirname(__file__)))
