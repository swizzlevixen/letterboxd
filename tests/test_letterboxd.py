from pytest import fixture
import logging
import os
from letterboxd.letterboxd import Letterboxd

logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


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
    # Responsible only for returning the test data
    # A film could also include 'originalName', but does not apply here
    return [
        "id",
        "name",
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


def test_letterboxd():
    lbxd = Letterboxd()
    assert isinstance(lbxd, Letterboxd)
