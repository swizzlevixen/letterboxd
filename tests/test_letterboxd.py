from pytest import fixture
import logging
import os
from letterboxd.letterboxd import Letterboxd

logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def test_letterboxd():
    lbxd = Letterboxd()
    assert isinstance(lbxd, Letterboxd)


# -------------------------
# Letterboxd API Definitions
# -------------------------


@fixture
def load_user_pass():
    """
    Loads the username and password from the environment
    :return: tuple - [username, password]
    """
    # try to get the username from environment variable
    LBXD_USERNAME = os.environ.get("LBXD_USERNAME", None)

    class UsernameMissingError(Exception):
        pass

    if LBXD_USERNAME is None:
        raise UsernameMissingError("Auth methods require a Letterboxd username.")
    # try to get the user password from environment variable
    LBXD_PASSWORD = os.environ.get("LBXD_PASSWORD", None)

    class PasswordMissingError(Exception):
        pass

    if LBXD_PASSWORD is None:
        raise PasswordMissingError("Auth methods require a Letterboxd password.")
    return (LBXD_USERNAME, LBXD_PASSWORD)


@fixture
def film_keys():
    # Film definition
    # http://api-docs.letterboxd.com/#/definitions/Film
    # Responsible only for returning the test data
    # A film could also include 'originalName', but does not apply here
    return [
        "id",
        "name",
        # "originalName",  # if it was if it was first released with a non-English title; does not apply to our test case
        "alternativeNames",
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


@fixture
def films_response_keys():
    # FilmsResponse definition
    # http://api-docs.letterboxd.com/#/definitions/FilmsResponse
    # Responsible only for returning the test data
    return ["next", "items"]
