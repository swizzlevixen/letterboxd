"""
Convenience module for user-based features of the Letterboxd API

API Documentation:
http://api-docs.letterboxd.com/
"""

from letterboxd.services.auth import Authentication


class User(object):
    def __init__(self, api, username, password):
        """
        Set up authentication for this user.
        :param api: Letterboxd.API - class instance
        :param username: str
        :param password: str
        """
        self._auth = Authentication(api=api, username=username, password=password)

    def token(self):
        """
        Make _auth get a token, and return the token string
        :return: str
        """
        return self._auth.token
