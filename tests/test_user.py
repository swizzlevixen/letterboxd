#! /usr/bin/env python3
import logging

from letterboxd.letterboxd import Letterboxd
from letterboxd.user import User

logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def test_user_auth(load_user_pass):
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
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
        lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    except Exception as e:
        logging.error(e.args)


def test_user_me(load_user_pass):
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd = Letterboxd()
    # login
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    me_dict = test_user.me
    logging.debug(f"me_dict: {me_dict}")
    assert isinstance(me_dict, dict)


def test_user_me_update(load_user_pass, member_settings_update_response_keys):
    """

    :return:
    """
    # login
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd = Letterboxd()
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    # test
    member_settings_update_request = {
        "emailWhenFollowed": True,
        "emailComments": True,
        "emailNews": True,
        "emailRushes": True,
    }
    member_settings_update_response = test_user.me_update(
        member_settings_update_request=member_settings_update_request
    )
    logging.debug(f"member_settings_update_response: {member_settings_update_response}")
    assert isinstance(member_settings_update_response, dict)
    assert set(member_settings_update_response_keys).issubset(
        member_settings_update_response.keys()
    ), "All keys should be in MemberSettingsUpdateResponse"


# TODO: test_refresh_token():
