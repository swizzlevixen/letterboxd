import logging

logging.getLogger(__name__)


class List(object):
    """
    /list/* services for the Letterboxd API
    """

    def __init__(self, api, list_id=None):
        """
        Initializes a Film object with a specific film.

        :param api: API object
        :param list_id: str - LID for the film on Letterboxd
        """
        self._api = api
        self._list_id = list_id

    def details(self, list_id=None):
        """
        /list/{id}

        Get details of a list by LID. If no list ID passed, uses the
        initialized list.

        :param list_id: str - LID of the film
        :return: dict - Film
        """
        if list_id is None:
            list_id = self._list_id
        response = self._api.api_call(path=f"list/{list_id}")
        return response.json()

    def comments(self, list_id=None, comments_request=None):
        """
        /list/{id}/comments

        A cursored window over the comments for a list.
        Use the ‘next’ cursor to move through the comments.

        :param list_id: str - LID of the list
        :param comments_request: dict - CommentsRequest
        :return:
        """
        if list_id is None:
            list_id = self._list_id
        response = self._api.api_call(path=f"list/{list_id}/comments")
        list_comments_response = response.json()
        return list_comments_response

    def create_comment(self, list_id=None, comment_creation_request=None):
        """
        /list/{id}/comments

        Create a comment on a list.

        Calls to this endpoint must include the access token for an authenticated member.

        :param list_id: str - LID for the list
        :param comment_creation_request: dict - CommentCreationRequest
        :return: dict - ListComment
        """
        if list_id is None:
            list_id = self._list_id
        response = self._api.api_call(
            path=f"list/{list_id}/comments",
            method="POST",
            params=comment_creation_request,
        )
        list_comment = response.json()
        return list_comment

    def entries(self, list_id=None, list_entries_request=None):
        """
        /list/{id}/entries

        Get entries for a list by ID.

        :param list_id: str - LID of the list
        :param list_entries_request: dict - ListEntriesRequest
        :return: dict - ListEntriesResponse
        """
        if list_id is None:
            list_id = self._list_id
        response = self._api.api_call(
            path=f"list/{list_id}/entries", params=list_entries_request
        )
        list_entries_response = response.json()
        return list_entries_response

    def me(self, list_id=None):
        """
        /list/{id}/me

        Get details of the authenticated member’s relationship with a list by ID.

        Calls to this endpoint must include the access token for an authenticated member.

        :param list_id: str - LID of the list
        :return: dict - ListRelationship
        """
        if list_id is None:
            list_id = self._list_id
        response = self._api.api_call(path=f"list/{list_id}/me")
        list_relationship = response.json()
        return list_relationship

    def me_update(self, list_id=None, list_relationship_update_request=None):
        """
        /list/{id}/me

        Update the authenticated member’s relationship with a list by ID.

        Calls to this endpoint must include the access token for an authenticated member.

        :param list_id: str - LID for the list
        :param list_relationship_update_request: dict - ListRelationshipUpdateRequest
        :return: dict - ListRelationshipUpdateResponse
        """
        if list_id is None:
            list_id = self._list_id
        response = self._api.api_call(
            path=f"list/{list_id}/me",
            method="PATCH",
            params=list_relationship_update_request,
        )
        list_relationship_update_response = response.json()
        return list_relationship_update_response

    def report(self, list_id=None, report_list_request=None):
        """
        /list/{id}/report

        Report a list by ID. Does NOT default to the initialized
        List instance LID, so as to not submit erroneous reports.

        Calls to this endpoint must include the access token for an authenticated member.

        :param list_id: str - LID of the list
        :param report_list_request: dict - ReportListRequest
        :return: bool - Success
        """
        response = self._api.api_call(
            path=f"list/{list_id}/report", params=report_list_request, method="POST"
        )
        if response.status_code is 204:
            # 204: Success
            return True
        else:
            return False

    def statistics(self, list_id=None):
        """
        /list/{id}/statistics

        Get statistical data about a list by ID.

        :param list_id: str - LID of the list
        :return: dict - ListStatistics
        """
        if list_id is None:
            list_id = self._list_id
        response = self._api.api_call(path=f"list/{list_id}/statistics")
        list_statistics = response.json()
        return list_statistics


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
