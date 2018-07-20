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
    """
    Film definition

    Optional keys: "originalName", "alternativeNames"
    """
    return [
        "id",
        "name",
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
def film_availability_response_keys():
    """FilmAvailabilityResponse definition"""
    return ["FilmAvailability"]


@fixture
def film_availability_keys():
    """
    FilmAvailability definition

    Optional keys: "id"
    """
    return ["service", "displayName", "country", "url"]


@fixture
def film_relationship_keys():
    """
    FilmRelationship definition

    Optional keys: "whenWatched", "whenLiked", "whenAddedToWatchlist",
        "whenCompletedInWatchlist", "rating"
    """
    return ["watched", "liked", "favorited", "inWatchlist", "reviews", "diaryEntries"]


@fixture
def film_relationship_update_response_keys():
    """FilmRelationshipUpdateResponse definition"""
    return ["data", "messages"]


@fixture
def member_film_relationships_response_keys():
    """
    MemberFilmRelationshipsResponse definition

    Optional keys: "next"
    """
    return ["items"]


@fixture
def member_film_relationship_keys():
    """MemberFilmRelationship definition"""
    return ["member", "relationship"]


@fixture
def member_summary_keys():
    """
    MemberSummary definition

    Optional keys:  "givenName", "familyName"
    """
    return [
        "id",
        "username",
        "displayName",
        "shortName",
        "pronoun",
        "avatar",
        "memberStatus",
    ]


@fixture
def film_statistics_keys():
    """
    FilmStatistics definition

    Optional keys: "rating" (I suspect "ratingsHistogram" might be?)
    """
    return ["film", "counts", "ratingsHistogram"]


@fixture
def film_summary_keys():
    """
    FilmSummary definition

    Optional keys: "originalName", "alternativeNames", "filmCollectionId",
        "releaseYear", "poster",
    """
    return ["id", "name", "directors", "links", "relationships"]


# -------------------------
# Films
# -------------------------


@fixture
def films_response_keys():
    """FilmsResponse definition"""
    return ["next", "items"]


@fixture
def film_services_response_keys():
    """FilmServicesResponse definition"""
    return ["items"]


@fixture
def service_keys():
    """Service definition"""
    return ["id", "name"]


@fixture
def genres_response_keys():
    """GenresResponse definition"""
    return ["items"]


@fixture
def genre_keys():
    """Genre definition"""
    return ["id", "name"]


@fixture
def link_keys():
    """Link definition"""
    return ["type", "id", "url"]


# -------------------------
# User (/me)
# -------------------------


@fixture
def member_settings_update_response_keys():
    """
    MemberSettingsUpdateResponse definition
    """
    return ["data", "messages"]
