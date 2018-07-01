import logging

logging.getLogger(__name__)


class Search(object):
    """
    /search for the Letterboxd API
    """

    def __init__(self, api):
        """

        :param api: API object
        """
        self._api = api

    def search(self, search_request={}):
        """
        /search

        :param search_request: dict - SearchRequest
        :return: dict - SearchResponse
        """
        # TODO handle status code errors
        response = self._api.api_call(path="search", params=search_request)
        search_response = response.json()
        return search_response
