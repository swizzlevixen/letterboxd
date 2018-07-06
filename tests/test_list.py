#! /usr/bin/env python3
import logging

from _pytest.fixtures import fixture

import letterboxd
from letterboxd.services.list import Lists
from tests.test_letterboxd import load_user_pass


@fixture
def lists_response_keys():
    pass


def test_lists():
    """Tests API call to get a film's details"""

    # Assume use of environment variables for api key and secret
    lbxd = letterboxd.new()
    # Login as a user
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    lists_request = {
        "perPage": 20,
        "sort": "ListName",
        "film": "2bbs",
        "clonedFrom": None,
        "tagCode": None,
        "tagger": None,
        "includeTaggerFriends": "All",
        "member": "u7kj",
        "memberRelationship": "Owner",
        "includeFriends": "None",
        "where": "Published",
        "filter": None,
    }
    lists = lbxd.lists(lists_request)
    assert isinstance(lists, Lists)
    # FIXME: This is copied from another test.
    # response_json = film_instance.details()
    # logging.debug(f"response_json: {response_json}")
    # assert isinstance(response_json, dict)
    # assert response_json["id"] == "2bbs", "The ID should be in the response"
    # assert set(film_keys()).issubset(
    #     response_json.keys()
    # ), "All keys should be in the response"
