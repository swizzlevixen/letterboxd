#! /usr/bin/env python3
import logging

from letterboxd.letterboxd import Letterboxd
from tests.test_letterboxd import load_user_pass


def test_member_watchlist():
    # set up
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    # get the watchlist
    member_id = test_user.me["member"]["id"]
    member = lbxd.member(member_id=member_id)
    watchlist_response = member.watchlist()
    watchlist = watchlist_response.json
    logging.debug("me_dict: {}".format(me_dict))
    assert isinstance(me_dict, dict)
