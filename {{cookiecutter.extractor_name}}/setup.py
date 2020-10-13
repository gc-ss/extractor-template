#!/usr/bin/env python
from setuptools import setup

setup(
    name="{{cookiecutter.extractor_name}}",
    version="0.1.0",
    description="Singer.io tap for ...", #Add purpose
    author="My name", #Add your name
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["{{cookiecutter.package_name}}"],
    install_requires=[
        # Add other packages used with versions for reliability
        "singer-python",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    {{cookiecutter.extractor_name}}={{cookiecutter.package_name}}:main
    """,
    packages=["{{cookiecutter.package_name}}"],
    package_data = {
        "schemas": ["{{cookiecutter.package_name}}/schemas/*.json"]
    },
    include_package_data=True,
)
