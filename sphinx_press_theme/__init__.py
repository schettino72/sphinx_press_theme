from os import path

from sphinx import addnodes


def add_doctree_data(app, pagename, templatename, context, doctree):
    # FIXME how to cache this, so it is not called for every page?
    master = app.env.get_doctree(app.env.config.master_doc)
    res = []
    for tree in master.traverse(addnodes.toctree):
        entries = []
        current0 = False
        for title, name in tree['entries']:
            current1 = (pagename == name)
            if current1:
                current0 = True
            if not title:
                title = app.env.titles[name].astext()
            entries.append({
                'name': name,
                'title': title,
                'current': current1,
            })
        res.append({
            'title': tree['caption'],
            'current': current0,
            'entries': entries,
        })
    context['toctree_data'] = res


def setup(app):
    app.connect('html-page-context', add_doctree_data)
    app.add_html_theme('press', path.abspath(path.dirname(__file__)))
