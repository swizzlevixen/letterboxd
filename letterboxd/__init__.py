# -*- coding: utf-8 -*-

"""Top-level package for Letterboxd."""

import logging

from letterboxd.config import API_BASE_URL
from letterboxd.letterboxd import Letterboxd

logging.getLogger(__name__).addHandler(logging.NullHandler())

name = "letterboxd"
__author__ = """Mark Boszko"""
__email__ = "mboszko@mac.com"
__version__ = "0.2.0"


def new(api_base=API_BASE_URL, api_key="", api_secret=""):
    """
    Create a new instance of the Letterboxd class

    :param api_base: str - the base URL of the API endpoints, including version number
    :param api_key: str - API key provided by Letterboxd
    :param api_secret: str - API shared secret provided by Letterboxd
    :return: Letterboxd instance
    """
    lbxd = Letterboxd(api_base=api_base, api_key=api_key, api_secret=api_secret)
    return lbxd
