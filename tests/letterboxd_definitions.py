#! /usr/bin/env python3
"""
Letterboxd API definitions for testing
"""

from _pytest.fixtures import fixture


# -------------------------
# Film-collection
# -------------------------


@fixture
def film_collection_keys():
    # FilmCollection definition
    return ["id", "name", "films", "links"]


# -------------------------
# Film
# -------------------------


@fixture
def film_keys():
    # Film definition
    # http://api-docs.letterboxd.com/#/definitions/Film
    # Commented lines may not be returned by every film
    return [
        "id",
        "name",
        # "originalName",
        # "alternativeNames",
        "releaseYear",
        "tagline",
        "description",
        "runTime",
        "poster",
        "backdrop",
        "backdropFocalPoint",
        "trailer",
        "genres",
        "contributions",
        "filmCollectionId",
        "links",
    ]


@fixture
def film_summary_keys():
    # FilmSummary definition
    # http://api-docs.letterboxd.com/#/definitions/FilmSummary
    # Commented lines may not be returned by every film
    return [
        "id",
        "name",
        # "originalName",
        # "alternativeNames",
        "releaseYear",
        "directors",
        "poster",
        # "filmCollectionId",
        "links",
        "relationships",
    ]


# -------------------------
# Films
# -------------------------


@fixture
def films_response_keys():
    # FilmsResponse definition
    # http://api-docs.letterboxd.com/#/definitions/FilmsResponse
    # Responsible only for returning the test data
    return ["next", "items"]


# -------------------------
# User (/me)
# -------------------------


@fixture
def member_settings_update_response_keys():
    """
    MemberSettingsUpdateResponse keys definition
    """
    return ["data", "messages"]
