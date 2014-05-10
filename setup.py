# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import readysaster-icannhas-web
version = readysaster-icannhas-web.__version__

setup(
    name='readysaster-icannhas-web',
    version=version,
    author='',
    author_email='neil@icannhas.com',
    packages=[
        'readysaster-icannhas-web',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['readysaster-icannhas-web/manage.py'],
)