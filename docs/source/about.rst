=====
About
=====

A modern responsive theme for python's `Sphinx docs <https://www.youtube.com/watch?v=JmN9rkVfsmo>`_.

Javascript/CSS using Vue.js + Stylus managed by vue-cli-3 (webpack).



lala
====

Do you have to repeatedly call complex command like this?

.. code-block:: console

    $ aws s3 sync _built/html s3://buck/et --exclude "*" --include "*.html"


Wrap it into `dodo.py` file:

.. code-block:: python

    def task_publish():
      """Publish to AWS S3"""
      return {
        "actions": [
            'aws s3 sync _built/html s3://buck/et --exclude "*" --include "*.html"'
        ]
      }
