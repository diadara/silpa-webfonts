#!/usr/bin/env python

from setuptools import setup, find_packages

name = "webfonts"

setup(
    name=name,
    version="0.2.1",
    url="http://silpa.org.in/Webfonts",
    license="LGPL-3.0",
    description="Webfonts for Indian languages",
    author="Santhosh Thottingal",
    author_email="santhosh.thottingal@gmail.com",
    long_description="""Webfonts for Indian languages""",
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['setuptools-git'],
    install_requires=['setuptools'],
    zip_safe=False,
)
