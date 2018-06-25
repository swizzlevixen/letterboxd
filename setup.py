import setuptools

# Read in the README file, for the long_description.
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="letterboxd",
    packages=["letterboxd", "letterboxd.services", "tests"],
    version="0.1.0",
    description="Python 3.6+ wrapper for the Letterboxd API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mark Boszko",
    author_email="mboszko@mac.com",
    copyright="Copyright (c) 2018 Mark Boszko",
    url="http://github.com/bobtiki/letterboxd",
    download_url="",
    keywords=["api", "movies"],
    classifiers=["Programming Language :: Python :: 3"],
    license="MIT",
)
