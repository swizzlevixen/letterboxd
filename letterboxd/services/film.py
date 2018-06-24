"""
Film(s) services for the Letterboxd API

/films endpoints documentation
http://api-docs.letterboxd.com/#path--films

/film endpoints documentation
http://api-docs.letterboxd.com/#path--film--id-
"""
import logging

logging.getLogger(__name__)


class Film(object):
    def __init__(self, api, film_id=None):
        self._api = api
        self._film_id = film_id

    def info(self):
        """
        /film/{id}
        Get details about a film by ID.
        http://api-docs.letterboxd.com/#path--film--id-
        :return: dict - JSON data
        """
        return self._api.api_call(path="film/{}".format(self._film_id))
