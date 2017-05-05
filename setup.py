#!/usr/bin/env python


try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test
import os


here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(here,  'README.rst'))
long_description = f.read().strip()
f.close()

setup(
    name='django_spam',
    version='0.1.0',
    author='tivix',
    author_email='nick.kelly@tivix.com',
    url='http://github.com/Tivix/django-spam',
    description='Redirecting bots to utilize their time better...',
    packages=find_packages(),
    long_description=long_description,
    keywords='django spam',
    zip_safe=False,
    include_package_data=True,
    py_modules=['django_spam'],
    install_requires=[
        'Django>=1.8.0',
    ],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)
