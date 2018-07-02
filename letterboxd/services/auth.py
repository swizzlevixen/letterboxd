"""
User authentication services for the Letterboxd API

Authentication API Documentation:
http://api-docs.letterbotokend.com/#auth
"""

import datetime
import logging

logging.getLogger(__name__)


class Authentication:
    """
    User authentication services for Letterboxd

    This token business mostly takes care of itself. Instantiate authentication
    with username and password, then call token(), and if there isn't a token
    already, or if it's expired, it will go and get one.
    """

    def __init__(self, api, username, password):
        """
        Initializer

        :param api: Letterboxd.API class instance
        :param username: str - user name
        :param password: str - user password
        """
        self._token_dict = None
        self._api = api
        self._username = username
        self._password = password
        self._token_expiration = datetime.datetime.now()

    @property
    def token(self):
        """

        :return: str - user token
        """
        logging.debug("getter of token called")
        if self._token_dict == None:
            # We don't have a token yet
            self._token_dict = self.login(self._username, self._password)
        elif self._token_expiration < datetime.datetime.now():
            # Our current token has expired, get a new one
            self._token_dict = self.login(self._username, self._password)
        # return just the access token string
        return self._token_dict["access_token"]

    @token.setter
    def token(self, value):
        """

        :param value: dict - expects 'access_token', 'token_type', 'expires_in', and 'refresh_token' keys
        :return: None
        """
        logging.debug("setter of token called")
        # set with the whole token dictionary, e.g.:
        # {'access_token' : str,
        #  'token_type': 'Bearer',
        #  'expires_in': int,
        #  'refresh_token': str}
        self._token_dict = value
        # Calculate the expiration datetime
        self._token_expiration = datetime.datetime.now() + datetime.timedelta(
            seconds=self._token_dict["expires_in"]
        )

    @token.deleter
    def token(self):
        """

        :return: None
        """
        logging.debug("deleter of token called")
        del self._token_dict
        # Reset the expiration to now (i.e., 'expired')
        self._token_expiration = datetime.datetime.now()

    def refresh_token(self):
        """
        Uses the current single-use refresh_token to request a new access token
        for the user

        :return:
        """
        grant_type = "refresh_token"
        form_str = (
            f"grant_type={grant_type}&refresh_token={self._token_dict['refresh_token']}"
        )
        logging.debug(f"form: {form_str}")
        try:
            response = self._api.api_call(
                path="auth/token", method="post", form=form_str
            )
        except:
            raise
        response_data = response.json()
        logging.debug(response_data)
        if not response_data["access_token"]:
            raise ConnectionRefusedError("Failed to retrieve access token")
        else:
            self.token = response_data
        return response_data

    def login(self, username, password):
        """
        User access to the Letterboxd API. Grabs a token for the user.
        http://api-docs.letterboxd.com/#path--auth-token

        :param username: str
        :param password: str
        :return: dict - either an AccessToken or OAuthError
        """
        grant_type = "password"
        form_str = f"grant_type={grant_type}&username={username}&password={password}"
        logging.debug(f"form: {form_str}")
        response = self._api.api_call(path="auth/token", method="post", form=form_str)
        response_data = response.json()
        logging.debug(response_data)
        if not response_data["access_token"]:
            # TODO: There's probably a better error we can throw instead
            raise ConnectionRefusedError("No token received")
        else:
            self.token = response_data
        return response_data
