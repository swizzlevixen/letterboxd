#! /usr/bin/env python3
import logging

import requests

from letterboxd.letterboxd import Letterboxd
from letterboxd.services.member import Member
from tests.test_letterboxd import film_summary_keys, films_response_keys, load_user_pass


def test_member_watchlist():
    # set up
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    # get the watchlist
    member_id = test_user.me["member"]["id"]
    logging.debug(f"member_id: {member_id}")
    assert isinstance(member_id, str)
    member = lbxd.member(member_id=member_id)
    logging.debug(f"member: {member}")
    assert isinstance(member, Member)
    watchlist_response = member.watchlist()
    logging.debug(f"watchlist_response: {watchlist_response}")
    assert isinstance(watchlist_response, requests.Response)
    assert watchlist_response.status_code == 200
    watchlist = watchlist_response.json()
    logging.debug(f"watchlist: {watchlist}")
    assert isinstance(watchlist, dict)
    assert set(films_response_keys()).issubset(
        watchlist.keys()
    ), "All keys should be in the response"
    # Test the first movie in the watchlist
    assert set(film_summary_keys()).issubset(
        watchlist["items"][0].keys()
    ), "All keys should be in the response"
