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

    def watchlist(self, member_id=None):
        """
        /film/{id}
        Get details about a film by ID.
        http://api-docs.letterboxd.com/#path--film--id-
        :param film_id: str - LID of the film
        :return: dict - Film
        """
        if member_id is None:
            member_id = self._member_id
        return self._api.api_call(path=f"film/{member_id}/watchlist")
