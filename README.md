
A modern responsive theme for python's Sphinx docs.

Javascript/CSS using Vue.js + Stylus managed by vue-cli-3 (webpack).

This is WIP. Just concept for project structure is done.

First build web assets:

```
cd ui
npm run build
```

Sphinx theme currenlty has a soft link to to built assets...
Install theme locally with `pip install -e .`.

`docs` folder contains theme's documentantion (and uses the theme itself)

```
cd docs
make clean; make html
``` 

