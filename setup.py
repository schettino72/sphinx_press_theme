from setuptools import setup

setup(
    name='sphinx_press_theme',
    version='0.1.0',
    #url=
    license='MIT',
    author='Eduardo Naufel Schettino <schetino72>',
    # description
    # long_description
    packages=['sphinx_press_theme'],
    package_data={'sphinx_press_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
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
        'Development Status :: 5 - Production/Stable',
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
)
