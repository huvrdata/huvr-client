#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = ["requests"]

setup(
    author="HUVRdata",
    author_email="api@huvrdata.com",
    python_requires="!=2.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="A python client for the HUVRdata API.",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords="huvr_client",
    name="huvr_client",
    packages=find_packages(include=["huvr_client", "huvr_client.*"]),
    test_suite="tests",
    url="https://github.com/huvrdata/huvr-client",
    zip_safe=False,
)
