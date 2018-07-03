import setuptools

# Read in the README file, for the long_description.
with open("README.markdown", "r") as fh:
    long_description = fh.read()

with open("CHANGELOG.md") as history_file:
    history = history_file.read()

setuptools.setup(
    name="letterboxd",
    packages=setuptools.find_packages(exclude=["contrib", "docs", "tests*", "sample"]),
    version="0.1.0a5",
    python_requires=">=3.6",
    install_requires=["requests"],
    description="Python 3.6+ wrapper for the Letterboxd API",
    long_description=long_description,
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
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    license="MIT",
)


# -----------------------------------
# Boilerplate below: merge in.
# -----------------------------------

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

setup(
    author="Mark Boszko",
    author_email="mboszko@mac.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    description="Python 3 wrapper for the Letterboxd API.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="letterboxd",
    name="letterboxd",
    packages=find_packages(include=["letterboxd"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/bobtiki/letterboxd",
    version="0.1.0",
    zip_safe=False,
)
