#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name="capsulemq",
    version="0.1.0",
    description="A simple message queuing system, built on top of MongoDB and based upon B.Coe's Karait source code.",
    author="Antoine Boegli",
    author_email="edomaur@gmail.com",
    url="http://github.com/edomaur/capsulemq",
    packages = find_packages(),
    install_requires = [
        'pymongo>=2.2.0'
    ],
    tests_require=[
        'nose'
    ]
)