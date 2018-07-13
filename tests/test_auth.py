#! /usr/bin/env python3

import letterboxd
from letterboxd.services.auth import Authentication


def test_forgotten_password_request():
    lbxd = letterboxd.new()
    status_code = Authentication.forgotten_password_request(
        api=lbxd.api, forgotten_password_request={"emailAddress": "user@example.com"}
    )
    assert status_code is 204
