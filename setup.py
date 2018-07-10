#! /usr/bin/env python3

from distutils.core import setup


setup(
    name='realestates',
    author='HOMEINFO - Digitale Informationssysteme GmbH',
    author_email='info@homeinfo.de',
    maintainer='Richard Neumann',
    maintainer_email='r.neumann@homeinfo.de',
    requires=['peewee', 'mdb', 'openimmodb', 'wsgilib',],
    py_modules=['realestates'],
    description='Real estates API.')
