"""
User-based features of the Letterboxd API
"""
import logging

from letterboxd.services.auth import Authentication

logging.getLogger(__name__)


class User(object):
    """
    Provices access token and shortcuts to user-focused methods
    """

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
        self.token

    @property
    def token(self):
        """
        Ask services.auth to get a token, and return the token string

        :return: str - oAuth token
        """
        return self._auth.token

    @property
    def me(self):
        """
        /me

        Get details about the authenticated member.

        Calls to this endpoint must include the access token for an
        authenticated member.

        :return: dict - MemberAccount
        """
        response = self._api.api_call(path="me")
        data = response.json()
        self.me = data
        return self._me

    @me.setter
    def me(self, value):
        """

        :param value: dict
        :return: None
        """
        self._me = value
        # TODO: Write /me PATCH call here

    # TODO: Write method for /me/validation-request
