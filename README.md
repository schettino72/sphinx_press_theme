A modern responsive theme for python's [Sphinx](http://www.sphinx-doc.org) documentation generator.

See it in action on Press Theme own [website](https://schettino72.github.io/sphinx_press_site/) 


This theme is based on [VuePress](https://vuepress.vuejs.org/).
It uses [Vue.js](https://vuejs.org/) & [Stylus](http://stylus-lang.com/) managed by
[webpack](https://webpack.js.org/) (through [vue-cli](https://cli.vuejs.org/)).


**Press** theme is still in **ALFA**, some core Sphinx features still not available.
Contributions are welcome.

## Usage

First install the theme:

```
$ pip install sphinx_press_theme
```

On Sphinx project's ``conf.py``: set the theme name to ``press``.

```
html_theme = "press"
```

See details on [Sphinx theming docs](http://www.sphinx-doc.org/en/master/theming.html#using-a-theme).


## Development

First build web assets:

```
cd ui
npm run build
```

Sphinx theme has a soft link to built assets...
Install theme locally with `pip install -e .`.

`docs` folder contains theme's own documentantion.

```
cd docs
make clean; make html
```
