#! /usr/bin/env python3

import logging
from random import randint

import letterboxd
from letterboxd.services.auth import Authentication
from tests.letterboxd_definitions import *
from tests.test_letterboxd import load_user_pass
logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def test_forgotten_password_request():
    lbxd = letterboxd.new()
    status_code = Authentication.forgotten_password_request(
        api=lbxd.api, forgotten_password_request={"emailAddress": "user@example.com"}
    )
    assert status_code == 204


def test_username_check():
    lbxd = letterboxd.new()
    # Hopefully this random username is available; not actually guaranteed
    sort_of_random_username = f"taco{randint(100, 999)}cat"
    logging.debug(f"sort_of_random_username: {sort_of_random_username}")
    username_check_response = Authentication.username_check(
        api=lbxd.api, username=sort_of_random_username
    )
    logging.debug(f"username_check_response: {username_check_response}")
    assert username_check_response["result"] == "Available"
