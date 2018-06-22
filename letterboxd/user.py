"""
User-based features for for the Letterboxd API

API Documentation:
http://api-docs.letterboxd.com/
"""

from letterboxd.services.auth import Authentication


class User(object):
    def __init__(self, api, username, password):
        self._auth = Authentication(api=api)
        self._auth.login(username=username, password=password)
