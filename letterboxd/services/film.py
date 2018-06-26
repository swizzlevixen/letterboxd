import logging

logging.getLogger(__name__)


class Film(object):
    """
    /film/* services for the Letterboxd API
    """

    def __init__(self, api, film_id=None):
        """

        :param api: API object
        :param film_id: str - the LID for the film on Letterboxd
        """
        self._api = api
        self._film_id = film_id

    def details(self, film_id=None):
        """
        /film/{id}
        Get details about a film by ID.
        http://api-docs.letterboxd.com/#path--film--id-

        :param film_id: str - LID of the film
        :return: dict - Film
        """
        if film_id is None:
            film_id = self._film_id
        # TODO Return dict instead of Response
        return self._api.api_call(path=f"film/{film_id}")

    def availability(self, film_id=None):
        """
        /film/{id}/availability
        Get availability data about a film by ID.
        This data is currently available to first-party only.

        :param film_id: str - LID of the film
        :return: dict - FilmAvailabilityResponse
        """
        if film_id is None:
            film_id = self._film_id
        # TODO Return dict instead of Response
        return self._api.api_call(path=f"film/{film_id}/availability")

    def me(self, film_id=None):
        """
        /film/{id}/me
        Get details of the authenticated member’s relationship with a film by ID.

        :param film_id: str - LID of the film
        :return: dict - FilmRelationship
        """
        if film_id is None:
            film_id = self._film_id
        # TODO Return dict instead of Response
        return self._api.api_call(path=f"film/{film_id}/me")
