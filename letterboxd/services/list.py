import logging

logging.getLogger(__name__)


class Lists(object):
    """
    /lists service for the Letterboxd API
    """

    def __init__(self, api):
        """

        :param api: API object
        """
        self._api = api

    def lists(self, lists_request=None):
        """
        [GET] /lists

        A cursored window over a list of lists.

        Use the ‘next’ cursor to move through the list.

        :param lists_request: dict - ListsRequest
        :return: dict - ListsResponse
        """
        response = self._api.api_call(path="lists", params=lists_request)
        lists_response = response.json()
        logging.debug(lists_response)
        return lists_response

    def create_list(self, list_creation_request=None):
        """
        [POST] /lists

        Create a list.

        Calls to this endpoint must include the access token
        for an authenticated member.

        :param list_creation_request: dict - ListCreationRequest
        :return: dict - ListCreateResponse
        """
        response = self._api.api_call(
            path="lists", params=list_creation_request, method="POST"
        )
        list_create_response = response.json()
        logging.debug(list_create_response)
        return list_create_response


# TODO: Implement /list/* endpoints
