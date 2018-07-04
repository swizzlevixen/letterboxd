import logging

logging.getLogger(__name__)


class Film(object):
    """
    /film/* services for the Letterboxd API
    """

    def __init__(self, api, film_id=None):
        """
        Initializes a Film object with a specific film.

        :param api: API object
        :param film_id: str - LID for the film on Letterboxd
        """
        self._api = api
        self._film_id = film_id

    def details(self, film_id=None):
        """
        /film/{id}

        Get details about a film by ID. If no film ID passed, uses the
        initialized film.

        :param film_id: str - LID of the film
        :return: dict - Film
        """
        if film_id is None:
            film_id = self._film_id
        details = self._api.api_call(path=f"film/{film_id}")
        return details.json()

    def availability(self, film_id=None):
        """
        /film/{id}/availability

        Get availability data about a film by ID.  If no film ID passed, uses
        the initialized film.

        NOTE: This data is currently available to first-party only.

        :param film_id: str - LID of the film
        :return: dict - FilmAvailabilityResponse
        """
        if film_id is None:
            film_id = self._film_id
        availability = self._api.api_call(path=f"film/{film_id}/availability")
        film_availability_response = availability.json()
        return film_availability_response

    def me(self, film_id=None):
        """
        /film/{id}/me

        Get details of the authenticated member’s relationship with a film by ID.
        If no film ID passed, uses the initialized film.

        :param film_id: str - LID of the film
        :return: dict - FilmRelationship
        """
        if film_id is None:
            film_id = self._film_id
        response = self._api.api_call(path=f"film/{film_id}/me")
        film_relationship = response.json()
        return film_relationship

    def members(self, film_id=None, member_film_relationships_request={}):
        """
        film/{id}/members

        Get details of members’ relationships with a film by ID. If no film ID
        passed, uses the initialized film.

        :param film_id: str - LID of the film
        :param member_film_relationships_request: dict - MemberFilmRelationshipsRequest
        :return: dict - MemberFilmRelationshipsResponse
        """
        if film_id is None:
            film_id = self._film_id
        response = self._api.api_call(
            path=f"film/{film_id}/members", params=member_film_relationships_request
        )
        member_film_relationships_response = response.json()
        return member_film_relationships_response

    def report(self, film_id=None, report_film_request={}):
        """
        /film/{id}/report

        Report problems with a film by ID. Does NOT default to the initialized
        Film instance LID, so as to not submit unnecessary reports.

        :param film_id: str - the LID of the film
        :param report_film_request: dict - ReportFilmRequest
        :return: requests.Response.status_code
        """
        try:
            response = self._api.api_call(
                path=f"film/{film_id}/report", params=report_film_request, method="POST"
            )
        except:
            if response.status_code is 204:
                # 204: Success
                pass
            else:
                raise
        if response.status_code is 204:
            # 204: Success
            return True
        else:
            return False

    def statistics(self, film_id=None):
        """
        /film/{id}/statistics

        Get statistical data about a film by ID.

        :param film_id: str - the LID of the film
        :return: dict - FilmStatistics
        """
        if film_id is None:
            film_id = self._film_id
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
        services = response.json()
        return services

    def genres(self):
        """
        /films/genres

        Get a list of genres supported by the /films endpoint.

        Genres are returned in alphabetical order.

        :return: dict - GenresResponse
        """
        response = self._api.api_call(path="films/genres")
        genres_response = response.json()
        return genres_response


class FilmCollection:
    """
    /film-collection service for the Letterboxd API
    """

    def __init__(self, api):
        """

        :param api: API object
        """
        self._api = api

    def film_collection(self, film_collection_id=None, film_collection_request={}):
        """
        /film-collection/{id}

        Get details about a film collection by ID. The response will include the
        film relationships for the signed-in member and the member indicated by
        the member LID if specified.

        :param film_collection_id: str - The LID of the film collection.
        :param film_collection_request: dict - FilmCollectionRequest
        :return: dict - FilmCollection
        """
        response = self._api.api_call(
            path=f"film-collection/{film_collection_id}", params=film_collection_request
        )
        film_collection = response.json()
        return film_collection
