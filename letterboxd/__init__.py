# -*- coding: utf-8 -*-

"""Top-level package for Letterboxd."""

import logging

from letterboxd.config import API_BASE_URL
from letterboxd.letterboxd import Letterboxd

logging.getLogger(__name__).addHandler(logging.NullHandler())

name = "letterboxd"
__author__ = """Mark Boszko"""
__email__ = "mboszko@mac.com"
__version__ = "0.3.0"


def new(
    api_base: str = API_BASE_URL, api_key: str = "", api_secret: str = ""
) -> Letterboxd:
    """Instantiate the Letterboxd class

    :param api_base: Base URL of the API endpoints, including version
    :type api_base: str
    :param api_key: API key provided by Letterboxd
    :type api_key: str
    :param api_secret: API shared secret provided by Letterboxd
    :type api_secret: str
    :return: Letterboxd instance
    :rtype: Letterboxd
    """
    lbxd = Letterboxd(api_base=api_base, api_key=api_key, api_secret=api_secret)
    return lbxd
