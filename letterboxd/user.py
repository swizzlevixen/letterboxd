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
        self._api = api
        self._auth = Authentication(api=api, username=username, password=password)

    def token(self):
        """
        Make _auth get a token, and return the token string
        :return: str
        """
        return self._auth.token

    def me(self):
        """
        /me
        Get details about the authenticated member.
        http://api-docs.letterboxd.com/#path--me
        :return: dict - JSON response
        """
        return self._api.api_call(path="me", headers=self.__token_header())

    # -------------------------
    # Private methods

    def __token_header(self):
        return {"Authorization": "Bearer {}".format(self.token())}
