"""
Python 3 wrapper for
Version 0 of the Letterboxd API
"""

import logging
import os
import requests
from letterboxd.api import API

# import service/auth
# import service/comments
# import service/contributors
from .services.film import Film

# import service/lists
# import service/log_entries
# import service/me
# import service/members
# import service/search

# default API URL for v0
API_BASE_URL = "https://api.letterboxd.com/api/v0"


class Letterboxd(object):
    def __init__(self, api_base=API_BASE_URL, api_key="", api_secret=""):
        self.api_base = api_base
        self.api_key = api_key
        self.api_secret = api_secret

        if self.api_key == "":
            # If the variable wasn't passed in,
            # try to get the environment variable instead
            LBXD_API_KEY = os.environ.get("LBXD_API_KEY", None)

            class APIKeyMissingError(Exception):
                pass

            if LBXD_API_KEY is None:
                raise APIKeyMissingError(
                    "All methods require an API key. See "
                    "https://letterboxd.com/api-coming-soon/ "
                    "for more information"
                )
            else:
                self.api_key = LBXD_API_KEY

        if self.api_secret == "":
            # If the variable wasn't passed in,
            # try to get the environment variable instead
            LBXD_API_SECRET = os.environ.get("LBXD_API_SECRET", None)

            class APISecretMissingError(Exception):
                pass

            if LBXD_API_SECRET is None:
                raise APISecretMissingError(
                    "All methods require an API secret. See "
                    "https://letterboxd.com/api-coming-soon/ "
                    "for more information"
                )
            else:
                self.api_secret = LBXD_API_SECRET

        self.api = API(self.api_base, self.api_key, self.api_secret)

    def film(self, film_id):
        return Film(film_id=film_id, api=self.api)
