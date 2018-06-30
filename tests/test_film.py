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
    # This data is first-party only, so it doesn't return any data for me.
    lbxd = Letterboxd()
    film_instance = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    response_json = film_instance.availability()
    logging.debug(f"response_json: {response_json}")
    assert isinstance(response_json, dict)


def test_film_me():
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    # login, even though we don't use this value
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    film_instance = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    response_json = film_instance.me()
    logging.debug(f"response_json: {response_json}")
    assert isinstance(response_json, dict)
    # TODO: test returned keys


def test_film_member():
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    # login, even though we don't use this value
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    film_instance = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    member_film_relationships_request = {
        "perPage": 100,
        "sort": "Name",
        "member": "11Ht",
        "memberRelationship": "IsFollowedBy",
        "filmRelationship": "Liked",
    }
    member_film_relationships_response = film_instance.member(
        member_film_relationships_request=member_film_relationships_request
    )
    logging.debug(f"response_json: {member_film_relationships_response}")
    assert isinstance(member_film_relationships_response, dict)
    # TODO: test returned keys


def test_film_report():
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    # login, even though we don't use this value
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    film_instance = lbxd.film(film_id="9mMS")  # Kirk Cameron’s Saving Christmas
    report_film_request = {"reason": "Other", "message": "TEST — IGNORE"}
    response_status_code = film_instance.report(
        film_id="9mMS", report_film_request=report_film_request
    )
    logging.debug(f"response_status_code: {response_status_code}")
    assert response_status_code is 204


def test_film_statistics():
    """Tests API call to get a film's statistics"""

    # Assume use of environment variables for api key and secret
    lbxd = Letterboxd()
    film_instance = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    assert isinstance(film_instance, Film)
    film_statistics = film_instance.statistics()
    logging.debug(f"film_statistics: {film_statistics}")
    assert isinstance(film_statistics, dict)
    assert film_statistics["film"]["id"] == "2bbs", "The ID should be in the response"
    # TODO: test returned keys


def test_films():
    """
    Test API call to /films
    """
    lbxd = Letterboxd()
    # FIXME: This doesn't seem to be constraining the list as expected
    films_request = {
        "perPage": 10,
        "tagger": "11Ht",
        "tagCode": "caitlandia",
        "decade": 1990,
    }
    films = lbxd.films()
    # FIXME: I shouldn't have to pass the api here
    films_response = films.films(films_request=films_request)
    # logging.debug(f"films_response: {films_response}")
    assert isinstance(films_response, dict)
    # Debug print a simple list of the movies
    film_num = 1
    for film in films_response["items"]:
        logging.debug(f"{film_num}. {film['name']}")
        film_num += 1
    # assert films_response ... something
    # TODO: test returned keys
