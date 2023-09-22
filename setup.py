#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import os


try:
    version = os.environ["GH_RELEASE_TAG"]
except KeyError as e:
    print("GH_RELEASE_TAG not set, (Hint - did you create a release on GitHub?)")
    raise e


with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = ["requests"]

setup(
    author="HUVRdata",
    author_email="api@huvrdata.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="A python client for the HUVRdata API.",
    install_requires=requirements,
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="huvr_client",
    name="huvr_client",
    packages=find_packages(include=["huvr_client", "huvr_client.api"]),
    test_suite="tests",
    url="https://github.com/huvrdata/huvr-client",
    version=version,
)
