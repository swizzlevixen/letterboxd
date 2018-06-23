from pytest import fixture
from letterboxd.letterboxd import Letterboxd
import logging
import os
import requests

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


def test_film_info():
    """Tests API call to get a film's info"""

    # Assume use of environment variables for api key and secret
    lbxd = Letterboxd()

    film_instance = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    response = film_instance.info()
    logging.debug("response: {}".format(response))
    assert isinstance(response, requests.Response)
    assert response.status_code == 200

    response_json = response.json()
    logging.debug("response_json: {}".format(response_json))
    assert isinstance(response_json, dict)
    assert response_json["id"] == "2bbs", "The ID should be in the response"
    assert set(film_keys()).issubset(
        response_json.keys()
    ), "All keys should be in the response"


def test_user_auth():
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    # make login
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    test_token = test_user.token()
    logging.debug("test_user.token: {}".format(test_token))
    assert isinstance(test_token, str)


def test_user_me():
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    # make login
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    me_dict = test_user.me
    logging.debug("me_dict: {}".format(me_dict))
    assert isinstance(me_dict, dict)
