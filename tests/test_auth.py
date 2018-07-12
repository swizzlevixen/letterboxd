#! /usr/bin/env python3

import letterboxd
from tests.test_letterboxd import load_user_pass


def test_forgotten_password_request():
    lbxd = letterboxd.new()
    # FIXME: Log in shouldn't be necessary for this
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    status_code = lbxd.auth.forgotten_password_request(
        forgotten_password_request={"emailAddress": "user@example.com"}
    )
    assert status_code is 400
