# -*- coding: utf-8 -*-

#  Quickstarted Options:
#
#  sqlalchemy: True
#  auth:       sqlalchemy
#  mako:       True
#
#

# This is just a work-around for a Python2.7 issue causing
# interpreter crash at exit when trying to log an info message.

from distutils.core import setup

try:
    import logging
    import multiprocessing
    import os
except:
    pass

import sys
py_version = sys.version_info[:2]

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
    documentation = open(os.path.join(here, 'doc.md')).read()
except IOError:
    documentation = ''

testpkgs = [
    'WebTest >= 1.2.3',
    'nose',
    'coverage',
    'gearbox'
]

install_requires = [
    "TurboGears2 >= 2.3.10",
    "Beaker >= 1.8.0",
    "Kajiki >= 0.6.1",
    "Mako",
    "zope.sqlalchemy >= 0.4",
    "sqlalchemy",
    "alembic",
    "repoze.who",
    "tw2.forms",
    "tgext.admin >= 0.6.1",
    "WebHelpers2"
]

if py_version != (3, 2):
    # Babel not available on 3.2
    install_requires.append("Babel")

setup(
    name='preview_generator',
    # this must be the same as the name above
    version='0.13',
    description='Generation of file previews',
    long_description=documentation,
    author='Algoo',
    author_email='clemalex20@gmail.com',
    url='https://github.com/herawo/file_previewer_poc',
    # use the URL to the github repo
    download_url='https://github.com/herawo/file_previewer_poc/archive/0.1.tar.gz',
    # I'll explain this in a second
    keywords=['preview', 'preview_generator', 'thumbnail'],
    # arbitrary keywords
    classifiers=[],
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=testpkgs,
    package_data={'preview_generator': [
        'i18n/*/LC_MESSAGES/*.mo',
        'templates/*/*',
        'public/*/*'
    ]},
    message_extractors={'preview_generator': [
        ('**.py', 'python', None),
        ('templates/**.mak', 'mako', None),
        ('templates/**.xhtml', 'kajiki', {'strip_text': False}),
        ('templates/**.mako', 'mako', None),
    #        ('public/**', 'ignore', None)
    ]},
    entry_points={
        'paste.app_factory': [
            'main = preview_generator.config.middleware:make_app'
        ],
        'gearbox.plugins': [
            'turbogears-devtools = tg.devtools'
        ]
    },
    zip_safe=False
)
