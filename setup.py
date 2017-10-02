#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   Takahiro Oshima <tarotora51@gmail.com>
# License:  MIT License
# Created:  2017-10-01
#
from setuptools import setup, find_packages
import sys

sys.path.append('./src')
sys.path.append('./tests')

setup(
    name = 'Tutorial',
    version = '0.0.1',
    description = 'This is Graphillion sample code',
    packages = find_packages(),
    test_suite = 'tutorial_test.suite'
)
