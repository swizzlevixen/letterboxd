"""
Convenience module for user-based features of the Letterboxd API

API Documentation:
http://api-docs.letterboxd.com/
"""
import logging
from letterboxd.services.auth import Authentication

logging.getLogger(__name__)


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
        self._me = None

    def token(self):
        """
        Make _auth get a token, and return the token string
        :return: str
        """
        return self._auth.token

    @property
    def me(self):
        """
        /me
        Get details about the authenticated member.
        http://api-docs.letterboxd.com/#path--me
        :return: dict - JSON response
        """
        auth_token_header = self.__token_header()
        response = self._api.api_call(path="me", headers=auth_token_header)
        data = response.json()
        self.me = data
        return self._me

    @me.setter
    def me(self, value):
        self._me = value

    # -------------------------
    # Private methods

    def __token_header(self):
        auth_token_header = {"Authorization": "Bearer {}".format(self.token())}
        logging.debug("auth_token_header: {}".format(auth_token_header))
        return auth_token_header
