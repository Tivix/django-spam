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
f = open(os.path.join(here, "README.md"))
long_description = f.read().strip()
f.close()

setup(
    name="django_spam",
    version="2.0.1",
    author="Nick Kelly",
    author_email="nick.kelly@tivix.com",
    url="http://github.com/Tivix/django-spam",
    description="Redirecting bots to utilize their time better...",
    packages=find_packages(exclude=("tests*",)),
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="django spam",
    zip_safe=False,
    include_package_data=True,
    py_modules=["django_spam"],
    test_suite="runtests.runtests",
    install_requires=[
        "Django>=2.0.0",
    ],
    classifiers=[
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
)
