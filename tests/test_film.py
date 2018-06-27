#! /usr/bin/env python3
import logging

import requests

from letterboxd.letterboxd import Letterboxd
from letterboxd.services.film import Film
from tests.test_letterboxd import film_keys, load_user_pass


def test_film_details():
    """Tests API call to get a film's details"""

    # Assume use of environment variables for api key and secret
    lbxd = Letterboxd()
    film_instance = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    assert isinstance(film_instance, Film)
    response_json = film_instance.details()
    logging.debug(f"response_json: {response_json}")
    assert isinstance(response_json, dict)
    assert response_json["id"] == "2bbs", "The ID should be in the response"
    assert set(film_keys()).issubset(
        response_json.keys()
    ), "All keys should be in the response"


def test_film_availability():
    lbxd = Letterboxd()
    film_instance = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    response_json = film_instance.availability()
    logging.debug(f"response_json: {response_json}")
    assert isinstance(response_json, dict)


def test_film_me():
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    # login
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    film_instance = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    response_json = film_instance.me()
    logging.debug(f"response_json: {response_json}")
    assert isinstance(response_json, dict)


def test_film_member():
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    # login
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    film_instance = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    response_json = film_instance.member()
    logging.debug(f"response_json: {response_json}")
    assert isinstance(response_json, dict)
