import logging

logging.getLogger(__name__)


class Member(object):
    """
    /member services for the Letterboxd API
    """

    def __init__(self, api, member_id=None):
        """

        :param api: API object
        :param member_id: str - the LID of the member
        """
        self._api = api
        self._member_id = member_id

    def details(self, member_id=None):
        """
        /member
        http://api-docs.letterboxd.com/#path--member--id-
        TODO: Write this function

        :param member_id: str - member LID
        :return:
        """
        pass

    def watchlist(self, member_id=None, watchlist_request={}):
        """
        /member/{id}/watchlist
        http://api-docs.letterboxd.com/#path--member--id--watchlist

        :param member_id: str - LID of member to get
        :param watchlist_request: dict - WatchlistRequest
        :return: dict - FilmsResponse
        """
        if member_id is None:
            member_id = self._member_id
        return self._api.api_call(
            path=f"member/{member_id}/watchlist", params=watchlist_request
        )
