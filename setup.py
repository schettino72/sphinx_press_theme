from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='sphinx_press_theme',
    version='0.1.1',
    url='https://schettino72.github.io/sphinx_press_site/',
    license='MIT',
    author='Eduardo Naufel Schettino <schetino72>',
    description='A Sphinx-doc theme based on Vuepress',
    long_description = long_description,
    packages=['sphinx_press_theme'],
    package_data={'sphinx_press_theme': [
        'theme.conf',
        '*.html',
        'util/*.html',
        'static/*.css',
        'static/*.js',
    ]},
        entry_points = {
        'sphinx.html_themes': [
            'press = sphinx_press_theme',
        ]
    },
    install_requires=[
       'sphinx'
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    keywords = "sphinx doc theme vue.js",
    project_urls = {
        'Documentation': 'https://schettino72.github.io/sphinx_press_site/',
        'Source': 'https://schettino72.github.io/sphinx_press_site/',
        'Tracker': 'https://schettino72.github.io/sphinx_press_site/issues',
    },
)
