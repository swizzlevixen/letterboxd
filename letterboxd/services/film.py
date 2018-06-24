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

    def info(self, film_id=self._film_id):
        """
        /film/{id}
        Get details about a film by ID.
        http://api-docs.letterboxd.com/#path--film--id-
        :param film_id: str - LID of the film
        :return: dict - Film
        """
        return self._api.api_call(path=f"film/{film_id}")

    def availability(self, film_id=self._film_id):
        """
        /film/{id}/availability
        Get availability data about a film by ID.
        :param film_id: str - LID of the film
        :return: list - FilmAvailabilityResponse
        """
        response = self._api.api_call(path=f"film/{film_id}/availability")
        return response["FilmAvailabilityResponse"]
