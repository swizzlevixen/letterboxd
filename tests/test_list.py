#! /usr/bin/env python3
import logging
import pprint

from _pytest.fixtures import fixture

import letterboxd
from letterboxd.services.list import Lists
from tests.test_letterboxd import load_user_pass


@fixture
def lists_response_keys():
    return ["next", "items"]


def list_summary_keys():
    """
    Returns the keys for ListSummary. The commented items may not exist
    :return:
    """
    return [
        "id",
        "name",
        "filmCount",
        "published",
        "ranked",
        # "descriptionLbml",
        # "descriptionTruncated",
        "owner",
        # "clonedFrom",
        "previewEntries",
        # "description",
    ]


def test_lists():
    """Tests API call to get a film's details"""

    # Assume use of environment variables for api key and secret
    lbxd = letterboxd.new()
    # Login as a user
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    # FIXME: Adjust this so it actually returns some lists
    lists_request = {
        "perPage": 20,
        "sort": "ListName",
        "film": "2bbs",
        "clonedFrom": None,
        "tagCode": None,
        "tagger": None,
        # "includeTaggerFriends": "All",
        # "member": "u7kj",
        # "memberRelationship": "Owner",
        # "includeFriends": "All",
        "where": "Published",
        "filter": None,
    }
    lists = lbxd.lists(lists_request=lists_request)
    assert isinstance(lists, dict)
    # logging.debug("-------------------------\nlists:")
    # logging.debug(pprint.pformat(lists))
    assert set(lists_response_keys()).issubset(
        lists.keys()
    ), "All keys should be in the lists_response."

    list_summary = lists["items"][0]
    assert isinstance(list_summary, dict)
    # logging.debug("-------------------------\nlist_summary:")
    # logging.debug(pprint.pformat(list_summary))
    assert set(list_summary_keys()).issubset(
        list_summary.keys()
    ), "All keys should be in list_summary."
