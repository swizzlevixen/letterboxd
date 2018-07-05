#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import setuptools

# Read in the README file, for the long_description.
with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.rst") as changelog_file:
    changelog = changelog_file.read()

requirements = ["requests"]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

setuptools.setup(
    name="letterboxd",
    packages=setuptools.find_packages(exclude=["contrib", "docs", "tests*", "sample"]),
    version="0.2.3",
    python_requires=">=3.6",
    install_requires=requirements,
    description="Python 3 wrapper for the Letterboxd API",
    long_description=readme + "\n\n" + changelog,
    long_description_content_type="text/markdown",
    author="Mark Boszko",
    author_email="mboszko@mac.com",
    copyright="Copyright (c) 2018 Mark Boszko",
    url="https://github.com/bobtiki/letterboxd/",
    download_url="",
    keywords=[
        "api",
        "movie",
        "film",
        "movie database",
        "movie review",
        "watchlist",
        "letterboxd",
        "moviedb",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Utilities",
    ],
    license="MIT",
    include_package_data=True,
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    zip_safe=False,
)
