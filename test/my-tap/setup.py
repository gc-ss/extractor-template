#!/usr/bin/env python
from setuptools import setup

setup(
    name="my-tap",
    version="0.1.0",
    description="Singer.io tap for ...", #Add purpose
    author="My name", #Add your name
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["my_tap"],
    install_requires=[
        # Add other packages used with versions for reliability
        "singer-python",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    my-tap=my_tap:main
    """,
    packages=["my_tap"],
    package_data = {
        "schemas": ["my_tap/schemas/*.json"]
    },
    include_package_data=True,
)
