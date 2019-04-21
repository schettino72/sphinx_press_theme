from os import path

from docutils import nodes
from sphinx.environment.collectors import EnvironmentCollector
from sphinx import addnodes

__version__ = (0, 3, 0)


class SimpleTocTreeCollector(EnvironmentCollector):
    """A TocTree collector that saves toctrees in a simple dict.

    sphinx.environment.collectors.toctree.TocTreeCollector saves
    TocTree as docutils.nodes which are hard to work with...
    """
    def enable(self, app):
        super().enable(app)
        app.env.toc_dict = {}

    def clear_doc(self, app, env, docname):
        env.toc_dict.pop(docname, None)

    def process_doc(self, app, doctree):
        docname = app.env.docname # sphinx mutates this, ouch!!!

        # print(f"================ Collector\n{docname}\n============\n")
        # get 1 level document toc (sections)
        section_nodes = [s for s in doctree if isinstance(s, nodes.section)]
        # if first level is a single section,
        # ignore it and use second level of sections
        if len(section_nodes) == 1:
            section2_nodes = [s for s in section_nodes[0]
                              if isinstance(s, nodes.section)]
            if section2_nodes: # do not replace with level-2 sections if None
                section_nodes = section2_nodes

        sections = []
        for node in section_nodes:
            sections.append({
                'title': node[0].astext(),
                'href': '#{}'.format(node['ids'][0]),
            })

        app.env.toc_dict[docname] = {
            'sections': sections,
            'toctrees': doctree.traverse(addnodes.toctree)
        }


def add_doctree_data(app, pagename, templatename, context, doctree):
    """create toctree_data, used to build sidebar navigation"""
    # print(f"---------- Context\n{pagename}\n-------------\n")
    master = app.env.get_doctree(app.env.config.master_doc)
    res = [] # list of top level toctrees in master_doc
    for tree in master.traverse(addnodes.toctree):
        entries = []
        current0 = False

        # special case for toctree that includes a single item
        # that contains a nested toctree.
        # In this case, just use the referenced toctree directly
        if len(tree['entries']) == 1:
            toctrees = app.env.toc_dict[tree['entries'][0][1]]['toctrees']

            if toctrees:
                # FIXME
                assert len(toctrees) == 1, "Press: Not supported more then one toctree on nested toctree"
                tree = toctrees[0]

        for title, name in tree['entries']:
            if not title:
                title = app.env.titles[name].astext()

            current1 = (pagename == name)
            children = []
            if current1:
                current0 = True
                # if current, add another level
                children = app.env.toc_dict[name]['sections']
                # add page_toc for current page
            entries.append({
                'name': name,
                'title': title,
                'current': current1,
                'children': children,
            })

        title = tree['caption']
        if not title:
            title = app.env.titles[tree['parent']].astext()

        res.append({
            'docname': tree['parent'],
            'anchor': '#{}'.format(tree.parent.parent['ids'][0]),
            'title': title,
            'current': current0,
            'entries': entries,
        })
    context['toctree_data'] = res


def setup(app):
    app.add_env_collector(SimpleTocTreeCollector)
    app.connect('html-page-context', add_doctree_data)
    app.add_html_theme('press', path.abspath(path.dirname(__file__)))
