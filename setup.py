#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import re


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('wagtail_box')


LONG_DESCRIPTION = open('README.rst').read()

setup(
    name="wagtail-nesting-box",
    version=version,
    description="Wagtail nesting box",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
    ],
    keywords='django wagtail',
    author="Emanuele Palazzetti",
    author_email='hello@palazzetti.me',
    url='https://github.com/palazzem/wagtail-nesting-box',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    test_suite='runtests',
    install_requires=[],
    zip_safe=False,
)
