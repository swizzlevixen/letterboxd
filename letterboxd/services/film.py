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
        # TODO handle status code errors
        details = self._api.api_call(path=f"film/{film_id}")
        return details.json()

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
        # TODO handle status code errors
        availability = self._api.api_call(path=f"film/{film_id}/availability")
        film_availability_response = availability.json()
        return film_availability_response

    def me(self, film_id=None):
        """
        /film/{id}/me
        Get details of the authenticated member’s relationship with a film by ID.

        :param film_id: str - LID of the film
        :return: dict - FilmRelationship
        """
        if film_id is None:
            film_id = self._film_id
        # TODO handle status code errors
        response = self._api.api_call(path=f"film/{film_id}/me")
        film_relationship = response.json()
        return film_relationship

    def member(self, film_id=None, member_film_relationships_request={}):
        """
        film/{id}/members
        Get details of members’ relationships with a film by ID.

        :param film_id: str - LID of the film
        :param member_film_relationships_request: dict - MemberFilmRelationshipsRequest
        :return: dict - MemberFilmRelationshipsResponse
        """
        if film_id is None:
            film_id = self._film_id
            # TODO handle status code errors
        response = self._api.api_call(
            path=f"film/{film_id}/members", params=member_film_relationships_request
        )
        member_film_relationships_response = response.json()
        return member_film_relationships_response
