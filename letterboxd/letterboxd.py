"""
Python 3 wrapper for
Version 0 of the Letterboxd API
"""

import os

from letterboxd.api import API
from letterboxd.config import API_BASE_URL
from letterboxd.user import User
from .services.auth import Authentication
from .services.film import Film, FilmCollection, Films
from .services.member import Member
from .services.search import Search
from .services.list import Lists


# TODO: Write these modules
# from .services.comment import Comment
# from .services.list import List
# from .services.log_entry import LogEntry
# from .services.news import News


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
        auth = Authentication(api=self.api)
        return auth

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
        film = Film(film_id=film_id, api=self.api)
        return film

    def films(self):
        """

        :return: services.film.Films object
        """
        films = Films(api=self.api)
        return films

    def film_collection(self, film_collection_id, film_collection_request):
        """
        /film-collection/{id}

        Get details about a film collection by ID. The response will include the
        film relationships for the signed-in member and the member indicated by
        the member LID if specified.

        :param film_collection_id: str - LID of the FilmCollection
        :param film_collection_request: dict - FilmCollectionRequest
        :return: dict - FilmCollection
        """
        film_collection_object = FilmCollection(api=self.api)
        film_collection_item = film_collection_object.film_collection(
            film_collection_id=film_collection_id,
            film_collection_request=film_collection_request,
        )
        return film_collection_item

    def member(self, member_id):
        """

        :param member_id: str - LID for Letterboxd member
        :return: services.member.Member object
        """
        member = Member(api=self.api, member_id=member_id)
        return member

    def search(self, search_request):
        """
        /search

        :param search_request: dict - SearchRequest
        :return: dict - SearchResponse
        """
        search = Search(self.api)
        search_response = search.search(search_request=search_request)
        return search_response

    def lists(self, lists_request):
        lists = Lists(self.api)
        lists_response = lists.lists(lists_request=lists_request)
        return lists_response

    def create_list(self, list_creation_request):
        lists = Lists(self.api)
        list_create_response = lists.create_list(
            list_creation_request=list_creation_request
        )
        return list_create_response
