"""
User authentication services for the Letterboxd API

Authentication API Documentation:
http://api-docs.letterbotokend.com/#auth
"""

import json
import logging
import requests
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

logging.getLogger(__name__)

# TODO: This token business should just take care of itself. Instantiate with user & pass, call token, and if there isn't a token already. If it's about to expire, renew it; if it's expierd, get a new token. The other code should just ask for the token, and this auth takes care of the rest.


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

    # TODO: Hopefully remove this in favor of `get_token`?
    def login(self, username, password):
        form = {"grant_type": "password", "username": username, "password": password}
        form_str = "grant_type={}&username={}&password={}".format(
            form["grant_type"], form["username"], form["password"]
        )
        logging.debug("form: {}".format(form_str))
        response = self._api.api_call(path="auth/token", method="post", form=form_str)
        response_data = response.json()
        logging.debug(response_data)
        if response.status_code != 200:
            status_code = str(response.status_code)
            error_type = response_data["type"]
            error_message = response_data["message"]
            raise ConnectionRefusedError(
                "Error {}: {} \n{}".format(status_code, error_type, error_message)
            )
        else:
            self.token = response_data["access_token"]
        if not token:
            # TODO: There's probably a better error we can throw instead
            raise ConnectionRefusedError("No token received")
        return self.token

    def get_token(self, username, password):
        client = LegacyApplicationClient(client_id=self._api.api_key)
        oauth = OAuth2Session(client=client)
        token_url = "{}/auth/token".format(self._api.api_base)
        # FIXME: I believe I need to sign this request and add it as a header, as:
        # headers["Authorization"] = "Signature {}".format(signature)
        # How can I get the prepared_request for this token request?
        token = oauth.fetch_token(
            token_url=token_url,
            username=username,
            password=password,
            client_id=self._api.api_key,
            client_secret=self._api.api_secret,
        )
        return self.token
