#! /usr/bin/env python3
import datetime
import logging
import pprint

from _pytest.fixtures import fixture

import letterboxd
from tests.test_letterboxd import load_user_pass

logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


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


def list_create_response_keys():
    """Returns list of keys in ListCreateResponse"""
    return ["data", "messages"]


def test_create_list():
    """Tests API call to get a film's details"""

    # Assume use of environment variables for api key and secret
    lbxd = letterboxd.new()
    # Login as a user
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    list_creation_request = {
        "published": False,
        "name": f"Top Two Movies in this Test List {datetime.datetime.now().isoformat()}",
        "ranked": True,
        "description": "This is the description that I'm testing with.",
        # "clonedFrom": ""
        "tags": ["API", "test"],
        "entries": [
            {
                "film": "2bbs",
                "rank": 2,
                "notes": "Here are the notes for Raiders",
                "containsSpoilers": True,
            },
            {
                "film": "23c8",
                "rank": 1,
                "notes": "This should be #1, KKBB",
                "containsSpoilers": False,
            },
        ],  # ListCreateEntry
        # "share": "Facebook"
    }
    list_create_response = lbxd.create_list(list_creation_request=list_creation_request)
    assert isinstance(list_create_response, dict)
    logging.debug("-------------------------\nlist_create_response:")
    logging.debug(pprint.pformat(list_create_response))
    logging.debug(f"list_create_response.keys() {list_create_response.keys()}")
    assert set(list_create_response_keys()).issubset(
        list_create_response.keys()
    ), "All keys should be in the lists_response."
    # TODO: Clean up: delete the list after creation
    # How do I do this?
