"""
User authentication services for the Letterboxd API

Authentication API Documentation:
http://api-docs.letterbotokend.com/#auth
"""

import logging
import requests
from requests_oauthlib import oauth2_auth

logging.getLogger(__name__)


class Authentication:
    """
    User authentication services for Letterboxd
    """

    def __init__(self, api):
        self._token = None
        self._api = api

    @property
    def token(self):
        logging.debug("getter of token called")
        return self._token

    @token.setter
    def token(self, value):
        logging.debug("setter of token called")
        self._token = value

    @token.deleter
    def token(self):
        logging.debug("deleter of token called")
        del self._token

    def login(self, username, password):
        form = {"grant_type": "password", "username": username, "password": password}
        login_response = self._api.api_call(path="auth/token", method="post", form=form)
        login_response_json = login_response.json()
        self.token = login_response_json["access_token"]
        if not token:
            # TODO: There's probably a JSON response error we can display instead
            raise ConnectionRefusedError("No token received")
        return login_response
