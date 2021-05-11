=============
Configuration
=============

The Press theme webpage is composed of a fixed header, a sidebar and main content area.

On Sphinx project's ``conf.py``: set the theme name to ``press``.

.. code-block:: python

   html_theme = "press"


See details on `Sphinx theming docs <https://www.sphinx-doc.org/en/master/usage/theming.html>`_.


Config values
=============

Basic configuration on ``conf.py``:


``html_logo``
^^^^^^^^^^^^^

If defined shows an image instead of project name on page top-left (link to index page).

.. code-block:: python

   html_logo = '_static/myproject-logo.png'


``html_sidebars``
^^^^^^^^^^^^^^^^^

By default the *sidebars* include only: searchbox and a global TOC tree.
See docs on `html_sidebars <http://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_sidebars>`_.

.. code-block:: python

  html_sidebars = {'**': ['util/searchbox.html', 'util/sidetoc.html']}


``html_css_files``
^^^^^^^^^^^^^^^^^^

Adds custom CSS files to the theme

.. code-block:: python

    # Here we assume that the file is at _static/css/custom.css
    html_css_files = ["css/custom.css"]

``html_external_links``
^^^^^^^^^^^^^^^^^^^^^^^

If provided, creates external links (e.g. Github) in the top right corner:

.. code-block:: python

    html_theme_options = {
      "external_links": [
          ("Github", "https://github.com/username/repo"),
          ("Other", "https://bla.com")
      ]
    }


Templates
=========


The ``util`` folder contains Jinja2 snippets to be *included*,
from main templates. Those can be easily replaced by theme users.

To change site/page structure you should *extend* pages and give new implementations for Jinja2 **blocks**.

Jinja2 templates and blocks are organized as follow:


``layout.html``
^^^^^^^^^^^^^^^

Blocks on HTML head:

- ``htmltitle`` - HTML page title
- ``css`` - include theme's CSS files
- ``scripts`` - include theme's javascript files
- ``extrahead`` - empty by default, to be used by theme users


Blocks on HTML body:

``container`` - whole visible page

* ``header`` - fixed header (includes ``util/navbar.html``)

  - ``navbar.html`` - apart from home-link includes ``util/navlinks.html`` & ``util/extlinks.html``

* ``sidebar``

  - ``side_links`` - includes ``util/navlinks.html`` & ``util/extlinks.html``
  - include all templates listed on ``html_sidebars`` config

* ``document``

  - ``body_header`` - includes ``util/bodyheader.html``
  - ``body`` - main content generated from ReST documents
  - ``footer`` - includes ``util/pagenav.html`` & ``util/footer.html``


``util/navbar.html``
^^^^^^^^^^^^^^^^^^^^

Header content. Left side contains *home-link* with name.

Right side contains links from ``util/navlinks.html`` and ``util/extlinks.html``.


``util/navlinks.html``
^^^^^^^^^^^^^^^^^^^^^^

Links taken from TOCs defined on master document.


``util/extlinks.html``
^^^^^^^^^^^^^^^^^^^^^^

External links defined by theme's user.


``util/searchbox.html``
^^^^^^^^^^^^^^^^^^^^^^^

Form to perform site search.

``util/sidetoc.html``
^^^^^^^^^^^^^^^^^^^^^

Navigation from toctree.


``util/bodyheader.html``
^^^^^^^^^^^^^^^^^^^^^^^^

Breadcrumbs and page navigation.

``util/pagenav.html``
^^^^^^^^^^^^^^^^^^^^^

Links for previous/next page.


``util/footer.html``
^^^^^^^^^^^^^^^^^^^^

Copyright information.

