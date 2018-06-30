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

    def report(self, film_id=None, report_film_request={}):
        """
        /film/{id}/report
        Report a film by ID.

        :param film_id: str - the LID of the film
        :param report_film_request: dict - ReportFilmRequest
        :return: requests.Response.status_code
        """
        # Does NOT default to the current Film instance LID,
        #     because I don't want to submit unnecessary reports
        # TODO handle status code errors
        response = self._api.api_call(
            path=f"film/{film_id}/report", params=report_film_request, method="POST"
        )
        return response.status_code

    def statistics(self, film_id=None):
        """
        /film/{id}/statistics
        Get statistical data about a film by ID.

        :param film_id: str - the LID of the film
        :return: dict - FilmStatistics
        """
        if film_id is None:
            film_id = self._film_id
        # TODO handle status code errors
        response = self._api.api_call(path=f"film/{film_id}/statistics")
        film_statistics = response.json()
        return film_statistics


class Films:
    """
    /films/* services for the Letterboxd API
    """

    def __init__(self, api):
        """

        :param api: API object
        """
        self._api = api

    def films(self, films_request={}):
        """
        /films

        A cursored window over the list of films.

        Use the ‘next’ cursor to move through the list. The response will include
        the film relationships for the signed-in member and the member indicated
        by the member LID if specified.

        :param films_request: dict - FilmsRequest
        :return: dict
        """
        response = self._api.api_call(path="films", params=films_request)
        # TODO handle status code errors
        films = response.json()
        return films

    def services(self):
        """
        /films/film-services

        Get a list of services supported by the /films endpoint.

        Services are returned in alphabetical order. Some services are only
        available to paying members, so results will vary based on the
        authenticated member’s status.

        :return: dict - FilmServicesResponse
        """
        response = self._api.api_call(path="films/film-services")
        # TODO handle status code errors
        services = response.json()
        return services

    def genres(self):
        """
        /films/film-services

        Get a list of services supported by the /films endpoint.

        Services are returned in alphabetical order. Some services are only
        available to paying members, so results will vary based on the
        authenticated member’s status.

        :return: dict - FilmServicesResponse
        """
        response = self._api.api_call(path="films/genres")
        # TODO handle status code errors
        genres = response.json()
        return genres
