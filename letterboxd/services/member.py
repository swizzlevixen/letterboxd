import logging

logging.getLogger(__name__)


class Member(object):
    """
    /member/* services for the Letterboxd API
    """

    def __init__(self, api, member_id=None):
        """
        Initializes a Member object with a specific member by LID.

        :param api: API object
        :param member_id: str - LID of the member
        """
        self._api = api
        self._member_id = member_id

    def details(self, member_id=None):
        """
        /member/{id}

        Get details about a member by ID.

        # TODO: Write this function

        :param member_id: str - The LID of the member.
        :return: dict - Member
        """
        pass

    def watchlist(self, member_id=None, watchlist_request={}):
        """
        /member/{id}/watchlist

        Get details of a member’s public watchlist by ID.

        The response will include the film relationships for the signed-in
        member, the watchlist’s owner, and the member indicated by the member
        LID if specified (the member and memberRelationship parameters are
        optional, and can be used to perform comparisons between the watchlist
        owner and another member). Use the /film/{id}/me endpoint to add or
        remove films from a member’s watchlist.

        :param member_id: str - The LID of the member.
        :param watchlist_request: dict - WatchlistRequest
        :return: dict - FilmsResponse
        """
        if member_id is None:
            member_id = self._member_id
        response = self._api.api_call(
            path=f"member/{member_id}/watchlist", params=watchlist_request
        )
        films_response = response.json()
        return films_response

    # TODO: Write the rest of Member / Members functions
