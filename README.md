## LOOKING FOR PROJECT MAINTAINERS

Unfortunately I (the author) do not have time to maintain this project.

If you are interested just ask me and I will provide admin rights on PyPI and commit access to this repo.

# sphinx_press_theme


[![PyPI](https://img.shields.io/pypi/v/sphinx_press_theme.svg)](https://pypi.python.org/pypi/sphinx_press_theme)


A modern responsive theme for python's [Sphinx](http://www.sphinx-doc.org) documentation generator.

See it in action on Press Theme own [website](https://schettino72.github.io/sphinx_press_site/)


This theme is based on [VuePress](https://vuepress.vuejs.org/).
It uses [Vue.js](https://vuejs.org/) & [Stylus](http://stylus-lang.com/) managed by
[vite](http://vitejs.dev/).



**Press** theme is still in **BETA**.
Contributions are welcome.

## Install

First install the theme:

```
$ pip install sphinx_press_theme
```

Sphinx version compatibility

|Sphinx |Press Theme|
|-------|-----------|
|7.X    | latest    |
|4.X    | 0.8.0     |
|3.X    | 0.6.1     |
|2.X    | 0.5.1     |


## Usage

On Sphinx project's ``conf.py``: set the theme name to ``press``.

```
html_theme = "press"
```

See details on [configuration](https://schettino72.github.io/sphinx_press_site/configuration.html).


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

## Release

Set version on:

- `setup.py`
- `sphinx_press_theme/__init__.py`
- `sphinx_press_theme/theme.conf`
- `docs/source/conf.py`
- `ui/package.json`


## Website

To update website:

```
cd ../press_site
rsync -rvi ../sphinx_press_theme/docs/build/html/ .
git add --all
```
