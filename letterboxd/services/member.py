"""
Member(s) services for the Letterboxd API

/member endpoints documentation
http://api-docs.letterboxd.com/#path--member--id-

/members endpoints documentation
http://api-docs.letterboxd.com/#path--members
"""
import logging

logging.getLogger(__name__)


class Member(object):
    def __init__(self, api, member_id=None):
        self._api = api
        self._member_id = member_id

    def details(self, member_id=None):
        pass

    def watchlist(self, member_id=None, watchlist_request={}):
        """
        /member/{id}/watchlist
        http://api-docs.letterboxd.com/#path--member--id--watchlist
        :param member_id: str - LID of member to compare to?
        :param watchlist_request: dict - WatchlistRequest
        :return: dict - FilmsResponse
        """
        return self._api.api_call(
            path=f"member/{member_id}/watchlist", params=watchlist_request
        )
