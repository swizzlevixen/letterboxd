"""
Python 3 wrapper for
Version 0 of the Letterboxd API
"""

import os

from letterboxd.config import *
from letterboxd.api import API
from letterboxd.user import User
from .services.auth import Authentication
from .services.film import Film
from .services.member import Member

# TODO: Write these modules
# from .services.comment import Comment
# from .services.list import List
# from .services.log_entry import LogEntry
# from .services.search import Search


class Letterboxd(object):
    """
    Loads the API base URL, API key, and API shared secret, and connects with
    all of the other classes.

    If the key and secret are not passed as arguments, it looks for them as
    environment variables, as LBXD_API_KEY and LBXD_API_SECRET.
    """

    # noinspection PyPep8Naming
    def __init__(self, api_base=API_BASE_URL, api_key="", api_secret=""):
        """

        :param api_base: str - the base URL of the API, including version number
        :param api_key: str
        :param api_secret: str
        """
        self.api_base = api_base
        self.api_key = api_key
        self.api_secret = api_secret

        if self.api_key == "":
            # If the variable wasn't passed in,
            # try to get the environment variable instead
            LBXD_API_KEY = os.environ.get("LBXD_API_KEY", None)

            class APIKeyMissingError(Exception):
                pass

            if LBXD_API_KEY is None:
                raise APIKeyMissingError(
                    "All methods require an API key. See "
                    "https://letterboxd.com/api-coming-soon/ "
                    "for more information"
                )
            else:
                self.api_key = LBXD_API_KEY

        if self.api_secret == "":
            # If the variable wasn't passed in,
            # try to get the environment variable instead
            LBXD_API_SECRET = os.environ.get("LBXD_API_SECRET", None)

            class APISecretMissingError(Exception):
                pass

            if LBXD_API_SECRET is None:
                raise APISecretMissingError(
                    "All methods require an API secret. See "
                    "https://letterboxd.com/api-coming-soon/ "
                    "for more information"
                )
            else:
                self.api_secret = LBXD_API_SECRET

        self.api = API(self.api_base, self.api_key, self.api_secret)

    def auth(self):
        """
        :return: services.auth.Authentication object
        """
        # noinspection PyArgumentList
        return Authentication(api=self.api)

    def user(self, username, password):
        """
        Signs in the user, and adds the oAuth token to future API calls

        :param username: str
        :param password: str
        :return: user.User object
        """
        user = User(api=self.api, username=username, password=password)
        self.api.user = user
        return user

    def film(self, film_id):
        """

        :param film_id: str - the LID of a film on Letterboxd
        :return: services.film.Film object
        """
        return Film(film_id=film_id, api=self.api)

    def films(self):
        """

        :return: services.film.Films object
        """
        films = Films(api=self.api)
        return films

    def member(self, member_id):
        """

        :param member_id: str - LID for Letterboxd member
        :return: services.member.Member object
        """
        member = Member(api=self.api, member_id=member_id)
        return member
