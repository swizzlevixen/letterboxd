"""
Python 3 wrapper for
Version 0 of the Letterboxd API
"""

import os
import requests
# import api
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

        if (self.api_key == ""):
            # If the variable wasn't passed in,
            # try to get the environment variable instead
            API_KEY = os.environ.get('LBXD_API_KEY', None)

            class APIKeyMissingError(Exception):
                pass

            if API_KEY is None:
                raise APIKeyMissingError(
                        "All methods require an API key. See "
                        "https://letterboxd.com/api-coming-soon/ "
                        "for more information"
                )

        if (self.api_secret == ""):
            # If the variable wasn't passed in,
            # try to get the environment variable instead
            API_SECRET = os.environ.get('LBXD_API_SECRET', None)

            class APISecretMissingError(Exception):
                pass

            if API_SECRET is None:
                raise APISecretMissingError(
                        "All methods require an API secret. See "
                        "https://letterboxd.com/api-coming-soon/ "
                        "for more information"
                )

        # Start the shared requests session
        self.session = requests.Session()
        self.session.params = {}
        self.session.params['api_key'] = API_KEY