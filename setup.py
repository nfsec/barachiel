#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.md').read()
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name = 'barachiel',
    version = '0.2',
    description = 'Script for manage virtual machines in OpenStack',
    long_description = readme,
    author = 'Patryk Krawaczyński',
    author_email = 'agresor@nfsec.pl',
    url = 'https://bitbucket.org/agresor/barachiel',
    license = 'Apache License (2.0)',
    keywords = 'openstack shell terminal manage machines',
    install_requires = required,
    data_files=[('', ['LICENSE', 'README.md'])],
    zip_safe = False,
    scripts = ['barachiel'],
    classifiers = (
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Shells'
    )
)
