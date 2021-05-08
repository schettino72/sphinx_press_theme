# sphinx_press_theme


[![PyPI](https://img.shields.io/pypi/v/sphinx_press_theme.svg)](https://pypi.python.org/pypi/sphinx_press_theme)

Please help me keep this project alive [![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/A0A23ZL4A)


A modern responsive theme for python's [Sphinx](http://www.sphinx-doc.org) documentation generator.

See it in action on Press Theme own [website](https://schettino72.github.io/sphinx_press_site/)


This theme is based on [VuePress](https://vuepress.vuejs.org/).
It uses [Vue.js](https://vuejs.org/) & [Stylus](http://stylus-lang.com/) managed by
[webpack](https://webpack.js.org/) (through [vue-cli](https://cli.vuejs.org/)).


**Press** theme is still in **BETA**.
Contributions are welcome.

## Install

First install the theme:

```
$ pip install sphinx_press_theme
```

Sphinx version compatibility

|Sphinx |Press Theme|
|-----|-------------|
|3.X  | 0.6.0       |
|2.X  | 0.5.1       |


## Usage

On Sphinx project's ``conf.py``: set the theme name to ``press``.

```
html_theme = "press"
```

See details on [Sphinx theming docs](http://www.sphinx-doc.org/en/master/theming.html#using-a-theme).


## Development

First build web assets:

```
cd ui
yarn build
```

Sphinx theme has a soft link to built assets...
Install theme locally with `pip install -e .`.

`docs` folder contains theme's own documentantion.

```
cd docs
make clean html
```


## Website

To update website:

```
cd ../press_site
rsync -rvi ../sphinx_press_theme/docs/build/html/ .
git add --all
```
