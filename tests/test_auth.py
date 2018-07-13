#! /usr/bin/env python3

from random import randint

import letterboxd
from letterboxd.services.auth import Authentication


def test_forgotten_password_request():
    lbxd = letterboxd.new()
    status_code = Authentication.forgotten_password_request(
        api=lbxd.api, forgotten_password_request={"emailAddress": "user@example.com"}
    )
    assert status_code is 204


def test_username_check():
    lbxd = letterboxd.new()
    # Hopefully this random username is available; not actually guaranteed
    sort_of_random_username = f"taco{randint(100, 999)}cat"
    username_check_response = Authentication.username_check(
        api=lbxd.api, username=sort_of_random_username
    )
    assert username_check_response["result"] is "Available"
