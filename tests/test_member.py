#! /usr/bin/env python3
import logging

from letterboxd.letterboxd import Letterboxd
from letterboxd.services.member import Member
from tests.letterboxd_definitions import *
from tests.test_letterboxd import load_user_pass

logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def test_member_watchlist(load_user_pass, films_response_keys, film_summary_keys):
    # set up
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd = Letterboxd()
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    # get the watchlist
    member_id = test_user.me["member"]["id"]
    logging.debug(f"member_id: {member_id}")
    assert isinstance(member_id, str)
    member = lbxd.member(member_id=member_id)
    logging.debug(f"member: {member}")
    assert isinstance(member, Member)
    # watchlist_request
    watchlist_request = {"perPage": 20}
    films_response = member.watchlist(watchlist_request=watchlist_request)
    logging.debug(f"films_response (watchlist): {films_response}")
    assert isinstance(films_response, dict)
    assert set(films_response_keys).issubset(
        films_response.keys()
    ), "All keys should be in the FilmsResponse"
    # Test the first movie in the watchlist
    if len(films_response["items"]) > 0:
        film_summary = films_response["items"][0]
        logging.debug(f"film_summary: {film_summary}")
        logging.debug(f"film_summary.keys(): {film_summary.keys()}")
        assert set(film_summary_keys).issubset(
            film_summary.keys()
        ), "All keys should be in the FilmSummary"
