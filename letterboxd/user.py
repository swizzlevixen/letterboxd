"""
User-based features of the Letterboxd API
"""
import logging

from letterboxd.services.auth import Authentication

logging.getLogger(__name__)


class User(object):
    """Provices access token and shortcuts to user-focused methods"""

    def __init__(self, api, username: str, password: str) -> None:
        """Set up authentication for this user.

        :param api: API class instance
        :type api: Letterboxd.API
        :param username: Letterboxd user name
        :type username: str
        :param password: Password
        :type password: str
        """
        self._api = api
        self._auth = Authentication(api=api, username=username, password=password)
        self._me = None
        self.token

    @property
    def token(self) -> str:
        """Ask services.auth to get a token, and return the token string

        :return: oAuth token
        :rtype: str
        """
        return self._auth.token

    @property
    def me(self) -> dict:
        """
        /me

        Get details about the authenticated member.

        Calls to this endpoint must include the access token for an
        authenticated member.

        :return: MemberAccount
        :rtype: dict
        """
        response = self._api.api_call(path="me")
        member_account = response.json()
        self._me = member_account
        return self._me

    def me_update(self, member_settings_update_request: dict) -> dict:
        """
        /me

        Update the profile settings for the authenticated member.

        Calls to this endpoint must include the access token for an authenticated member

        :param member_settings_update_request: MemberSettingsUpdateRequest
        :type member_settings_update_request: dict
        :return: MemberSettingsUpdateResponse
        :rtype: dict
        """
        response = self._api.api_call(
            path="me", method="PATCH", params=member_settings_update_request
        )
        member_settings_update_response = response.json()
        return member_settings_update_response

    # TODO: Write method for /me/validation-request
