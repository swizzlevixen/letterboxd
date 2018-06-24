#! /usr/bin/env python3
import logging

from letterboxd.letterboxd import Letterboxd
from letterboxd.services.member import Member
from tests.test_letterboxd import load_user_pass


def test_member_watchlist():
    # set up
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    # get the watchlist
    member_id = test_user.me["member"]["id"]
    assert isinstance(member_id, str)
    member = lbxd.member(member_id=member_id)
    assert isinstance(member, Member)
    watchlist_response = member.watchlist()
    assert isinstance(response, requests.Response)
    assert response.status_code == 200
    watchlist = watchlist_response.json
    logging.debug("me_dict: {}".format(watchlist))
    assert isinstance(watchlist, dict)
    # assert set(watchlist_keys()).issubset(
    #         watchlist.keys()
    # ), "All keys should be in the response"
