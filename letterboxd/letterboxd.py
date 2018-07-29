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
from .services.list import List, Lists
from .services.member import Member
from .services.search import Search


# TODO: Write these modules
# from .services.comment import Comment
# from .services.log_entry import LogEntry
# from .services.news import News


class Letterboxd(object):
    """
    Loads the API base URL, API key, and API shared secret, and connects with
    all of the other classes.

    If the key and secret are not passed as arguments, it looks for them as
    environment variables, as LBXD_API_KEY and LBXD_API_SECRET.
    """

    def __init__(
        self, api_base: str = API_BASE_URL, api_key: str = "", api_secret: str = ""
    ) -> None:
        """Load in the API information

        :param api_base: The base URL of the API, including version number,
            with no trailing slash
        :type api_base: str
        :param api_key: Letterboxd API key
        :type api_key: str
        :param api_secret: Letterboxd API secret
        :type api_secret: str
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

    def auth(self) -> Authentication:
        """
        :return: Authentication object
        :rtype: Authentication
        """
        auth = Authentication(api=self.api)
        return auth

    def user(self, username: str, password: str) -> User:
        """Sign in the user, and add the oAuth token to future API calls

        :param username: Letterboxd user name
        :type username: str
        :param password: Password
        :type password: str
        :return: User object
        :rtype: User
        """
        user = User(api=self.api, username=username, password=password)
        self.api.user = user
        return user

    def film(self, film_id: str) -> Film:
        """Instantiate a fim object

        :param film_id: LID of a film on Letterboxd
        :type film_id: str
        :return: Film object
        :rtype: Film
        """
        film = Film(film_id=film_id, api=self.api)
        return film

    def films(self) -> Films:
        """Instantiate a Films object

        :return: Films object
        :rtype: Films
        """
        films = Films(api=self.api)
        return films

    def film_collection(
        self, film_collection_id: str, film_collection_request: dict
    ) -> FilmCollection:
        """Instantiate a FilmCollection object, return one item

        :return: FilmCollection item
        :rtype: dict
        """
        film_collection_object = FilmCollection(api=self.api)
        film_collection_item = film_collection_object.film_collection(
            film_collection_id=film_collection_id,
            film_collection_request=film_collection_request,
        )
        return film_collection_item

    def member(self, member_id: str) -> Member:
        """instantiate a Member object

        :param member_id: LID for Letterboxd member
        :type member_id: str
        :return: Member object
        :rtype: Member
        """
        member = Member(api=self.api, member_id=member_id)
        return member

    def search(self, search_request: dict) -> dict:
        """
        /search

        :param search_request: SearchRequest
        :type search_request: dict
        :return: SearchResponse
        :rtype: dict
        """
        search = Search(self.api)
        search_response = search.search(search_request=search_request)
        return search_response

    def list(self, list_id) -> List:
        """Instantiate a List object

        :param list_id: LID of a list on Letterboxd
        :type list_id: str
        :return: List object
        :rtype: List
        """
        list = List(list_id=list_id, api=self.api)
        return list

    def lists(self, lists_request: dict) -> dict:
        """Get a ListsResponse

        :param lists_request: ListsRequest
        :type lists_request: dict
        :return: ListsResponse
        :rtype: dict
        """
        lists = Lists(self.api)
        lists_response = lists.lists(lists_request=lists_request)
        return lists_response

    def create_list(self, list_creation_request: dict) -> dict:
        """Create a list

        :param list_creation_request: ListCreationRequest
        :type list_creation_request: dict
        :return: ListCreateResponse
        :rtype: dict
        """
        lists = Lists(self.api)
        list_create_response = lists.create_list(
            list_creation_request=list_creation_request
        )
        return list_create_response
