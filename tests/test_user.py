#! /usr/bin/env python3
import logging

from letterboxd.letterboxd import Letterboxd
from letterboxd.user import User
from tests.test_letterboxd import load_user_pass


def test_user_auth():
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    # make login
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    assert isinstance(test_user, User)
    test_token = test_user.token
    logging.debug(f"test_user.token: {test_token}")
    assert isinstance(test_token, str)
    assert lbxd.api.user.token is test_token


def test_user_auth_bad():
    LBXD_USERNAME = "Butts McGee"
    LBXD_PASSWORD = "123456"
    lbxd = Letterboxd()
    # make login
    try:
        test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    except Exception as e:
        logging.error(e.args)


def test_user_me():
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    # make login
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    me_dict = test_user.me
    logging.debug(f"me_dict: {me_dict}")
    assert isinstance(me_dict, dict)
