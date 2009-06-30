#!/usr/bin/env python
# -*- coding: utf8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages



setup(name='meaningtoolws',
      version='0.1',
      description='Meaningtool Web Services Python Client',
      author='Popego Corporation',
      author_email='contact@popego.com',
      url='http://github.com/k0001/meaningtoolws',
      packages=['meaningtoolws'],
     )

