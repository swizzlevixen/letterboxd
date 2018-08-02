"""
User authentication services for the Letterboxd API

Authentication API Documentation:
http://api-docs.letterbotokend.com/#auth
"""

import datetime
import logging

logging.getLogger(__name__)


class Authentication:
    """User authentication services for Letterboxd

    This token business mostly takes care of itself. Instantiate authentication
    with username and password, then call token(), and if there isn't a token
    already, or if it's expired, it will go and get one.
    """

    def __init__(self, api, username: str, password: str) -> None:
        """Initializer

        :param api: Letterboxd.API class instance
        :type api: API
        :param username: Letterboxd user name
        :type username: str
        :param password: Password
        :type password: str
        """
        self._token_dict = None
        self._api = api
        self._username = username
        self._password = password
        self._token_expiration = datetime.datetime.now()

    @property
    def token(self) -> str:
        """Gets and returns a user authentication token

        Checks if the user authentication token already exists. If not, it tries
        to get one. If it does exist, it checks to see if it is expired, and if
        so, it attempts to refresh the token.

        :return: User authentication token
        :rtype: str
        """
        logging.debug("getter of token called")
        if self._token_dict is None:
            # We don't have a token yet
            self._token_dict = self.login(self._username, self._password)
        elif self._token_expiration < datetime.datetime.now():
            # Our current token has expired, get a new one
            self._token_dict = self.login(self._username, self._password)
        # return just the access token string
        return self._token_dict["access_token"]

    @token.setter
    def token(self, value: dict) -> None:
        """Set the value of the token, and calculate the expiration time.

        :param value: expects 'access_token', 'token_type', 'expires_in',
            and 'refresh_token' keys
        :type value: dict
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
    def token(self) -> None:
        """Deletes the user authentication token."""
        logging.debug("deleter of token called")
        del self._token_dict
        # Reset the expiration to now (i.e., 'expired')
        self._token_expiration = datetime.datetime.now()

    def refresh_token(self) -> dict:
        """
        Uses the current single-use refresh_token to request a new access token
        for the user

        :return: Either an AccessToken or OAuthError
        :rtype: dict
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
        except Exception as e:
            raise e
        response_data = response.json()
        logging.debug(response_data)
        if not response_data["access_token"]:
            raise ConnectionRefusedError("Failed to retrieve access token")
        else:
            self.token = response_data
        return response_data

    def login(self, username: str, password: str) -> dict:
        """Sends user credentials to get user access token.

        :param username: Letterboxd user name
        :type username: str
        :param password: Password
        :type password: str
        :return: Either an AccessToken or OAuthError
        :rtype: dict
        """
        grant_type = "password"
        form_str = f"grant_type={grant_type}&username={username}&password={password}"
        logging.debug(f"form: {form_str}")
        response = self._api.api_call(path="auth/token", method="post", form=form_str)
        response_data = response.json()
        logging.debug(response_data)
        if not response_data["access_token"]:
            raise ConnectionRefusedError("Failed to retrieve access token")
        else:
            self.token = response_data
        return response_data

    @staticmethod
    def forgotten_password_request(api, forgotten_password_request: dict) -> int:
        """
        /auth/forgotten-password-request

        Request a link via email to reset the password for a member’s account.

        :param forgotten_password_request: ForgottenPasswordRequest
        :type forgotten_password_request: dict
        :return: HTTP status code
        :rtype: int
        """
        response = api.api_call(
            path="auth/forgotten-password-request",
            params=forgotten_password_request,
            method="POST",
        )
        status_code = response.status_code
        logging.debug(f"status_code: {status_code}")
        return status_code

    @staticmethod
    def username_check(api, username: str) -> dict:
        """/auth/username-check

        Check if a username is available to register.

        Use this endpoint to check the validity and availability of a given
        username. Usernames must be between 2 and 15 characters long and may
        only contain upper or lowercase letters, numbers or the underscore (_)
        character. Usernames associated with deactivated accounts are not
        automatically released to the pool of available names (members will need
        to contact Letterboxd Support for assistance).

        :param api: API object
        :type api: API
        :param username: Letterboxd user name
        :type username: str
        :return: UsernameCheckResponse
        :rtype: dict
        """
        response = api.api_call(
            path="auth/username-check", params={"username": username}
        )
        username_check_response = response.json()
        logging.debug(f"username_check_response: {username_check_response}")
        return username_check_response
