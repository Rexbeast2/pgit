#!/usr/bin/env python3

from setuptools import setup

setup (name = 'pgit',
       version = '0.1.0',
       packages = ['pgit'],
       entry_points = {
           'console_scripts' : [
               'pgit = pgit.cli:main'
           ]
       })
