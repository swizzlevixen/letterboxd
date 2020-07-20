#! /usr/bin/env python3
import datetime
import logging
import pprint
from random import randint

import letterboxd
from tests.letterboxd_definitions import *
from tests.test_letterboxd import load_user_pass
logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

# -------------------------
# List
# -------------------------


def test_list_details(list_keys):
    """
    /list/{id}
    """
    lbxd = letterboxd.new()
    list_id = "3kP6"  # AFI 100 Years... 100 Movies (2007)
    list = lbxd.list(list_id=list_id)
    list_details = list.details()
    assert isinstance(list_details, dict)
    logging.debug(f"list_details: {list_details}")
    logging.debug(f"list_details.keys(): {list_details.keys()}")
    assert set(list_keys).issubset(list_details.keys()), "All keys should be in Keys."


def test_list_update(load_user_pass, list_update_response_keys):
    """
    /list/{id} [PATCH]
    """
    lbxd = letterboxd.new()
    # Login
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    list_id = "1UxUo"  # test_optical: "These are Twenty Films to Test With"
    rand_int_str = (
        f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"
    )
    list_update_request = {
        "published": True,
        "name": f"Twenty Films to Test With {rand_int_str}",
        "ranked": True,
        "description": f"API TEST - IGNORE\n\nHere's a description with some <strong>strong</strong> language, <em>emphasized</em>, <b>bold</b>, <i>italics</i>, a <a href=\"http://opticalpodcast.com\">link</a>, and here's a quote:\n\n<blockquote>We have nothing to fear but fear itself. And werewolves.\n\n—FDR, Werewolf Hunter</blockquote>\n\nUpdated {datetime.datetime.now().isoformat()}",
        "tags": ["api", "test", rand_int_str],
        "entries": [
            {
                "film": "1WRy",
                "rank": randint(1, 20),
                "notes": "Random rank the first",
                "containsSpoilers": False,
            },
            {
                "film": "2TRW",
                "rank": randint(1, 20),
                "notes": "Random rank the second",
                "containsSpoilers": True,
            },
        ],
    }

    list = lbxd.list(list_id=list_id)
    list_update_response = list.update(list_update_request=list_update_request)
    logging.debug(f"list_update_response: {list_update_response}")
    assert isinstance(list_update_response, dict)

    logging.debug(f"list_update_response.keys(): {list_update_response.keys()}")
    assert set(list_update_response_keys).issubset(
        list_update_response.keys()
    ), "All keys should be in ListUpdateResponse"


def test_list_comments(list_comments_response_keys, list_comment_keys):
    """
    /list/{id}/comments
    """
    lbxd = letterboxd.new()
    list_id = "lITC"  # Films Directed by Women
    comments_request = {"perPage": 25, "sort": "Updates", "includeDeletions": True}
    list = lbxd.list(list_id=list_id)
    list_comments_response = list.comments(comments_request=comments_request)
    assert isinstance(list_comments_response, dict)
    logging.debug(f"list_comments_response: {list_comments_response}")
    assert set(list_comments_response_keys).issubset(
        list_comments_response.keys()
    ), "All keys should be in ListCommentsResponse"

    list_comment = list_comments_response["items"][0]
    assert list_comment["list"]["id"] == list_id
    logging.debug(f"list_comment: {list_comment}")
    logging.debug(f"list_comment.keys(): {list_comment.keys()}")
    assert set(list_comment_keys).issubset(
        list_comment.keys()
    ), "All keys should be in ListComment"


def test_list_create_comment(load_user_pass, list_comment_keys):
    lbxd = letterboxd.new()
    # Login
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    comment_creation_request = {
        "comment": "API TEST - IGNORE\n\nHere's a comment with some <strong>strong</strong> language, <em>emphasized</em>, <b>bold</b>, <i>italics</i>, a <a href=\"http://opticalpodcast.com\">link</a>, and here's a quote:\n\n<blockquote>We have nothing to fear but fear itself. And werewolves.\n\n—FDR, Werewolf Hunter</blockquote>"
    }
    list_id = "1UxUo"

    list = lbxd.list(list_id=list_id)
    list_comment = list.create_comment(
        comment_creation_request=comment_creation_request
    )
    logging.debug(f"list_comment: {list_comment}")
    assert isinstance(list_comment, dict)

    logging.debug(f"list_comment.keys(): {list_comment.keys}")
    assert set(list_comment_keys).issubset(
        list_comment.keys()
    ), "All keys should be in ListComment"


def test_list_entries(list_entries_response_keys):
    lbxd = letterboxd.new()
    list_id = "1UxUo"  # test_optical: "These are Twenty Films to Test With"
    list_entries_request = {
        "perPage": 10,
        "sort": "AverageRatingHighToLow",
        "decade": 1990,
        "service": "amazon",
        "where": "Released",
    }
    list = lbxd.list(list_id=list_id)
    list_entries_response = list.entries(list_entries_request=list_entries_request)
    logging.debug(f"list_entries_response: {list_entries_response}")
    assert isinstance(list_entries_response, dict)

    logging.debug(f"list_entries_response.keys(): {list_entries_response.keys()}")
    assert set(list_entries_response_keys).issubset(
        list_entries_response.keys()
    ), "All keys should be in ListEntriesResponse."


def test_list_me(load_user_pass, list_relationship_keys):
    lbxd = letterboxd.new()
    # Login
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)

    list_id = "1UxUo"  # test_optical: "These are Twenty Films to Test With"
    list = lbxd.list(list_id=list_id)
    list_relationship = list.me()
    logging.debug(f"list_relationship: {list_relationship}")
    assert isinstance(list_relationship, dict)

    logging.debug(f"list_relationship.keys(): {list_relationship.keys()}")
    assert set(list_relationship_keys).issubset(
        list_relationship.keys()
    ), "All keys should be in ListRelationship."


def test_list_me_update(load_user_pass, list_relationship_update_response_keys):
    lbxd = letterboxd.new()
    # Login
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    list_id = "j4lQ"  # bobtiki: "Personal Top 100"
    list_relationship_update_request = {"liked": True, "subscribed": True}

    list = lbxd.list(list_id=list_id)
    list_relationship_update_response = list.me_update(
        list_relationship_update_request=list_relationship_update_request
    )
    logging.debug(
        f"list_relationship_update_response: {list_relationship_update_response}"
    )
    assert isinstance(list_relationship_update_response, dict)

    logging.debug(
        f"list_relationship_update_response.keys(): {list_relationship_update_response.keys()}"
    )
    assert set(list_relationship_update_response_keys).issubset(
        list_relationship_update_response.keys()
    ), "All keys should be in ListRelationshipUpdateResponse"


def test_list_report(load_user_pass):
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd = letterboxd.new()
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    list_id = "1UxUo"  # test_optical: "These are Twenty Films to Test With"
    report_list_request = {"reason": "Other", "message": "TEST — IGNORE"}

    list = lbxd.list(list_id=list_id)
    success = list.report(list_id=list_id, report_list_request=report_list_request)
    logging.debug(f"success: {success}")
    assert success is True


def test_list_statistics(list_statistics_keys):
    lbxd = letterboxd.new()
    list_id = "1UxUo"  # test_optical: "These are Twenty Films to Test With"

    list = lbxd.list(list_id=list_id)
    list_statistics = list.statistics()
    logging.debug(f"list_statistics: {list_statistics}")
    assert isinstance(list_statistics, dict)

    logging.debug(f"list_statistics.keys(): {list_statistics.keys()}")
    assert set(list_statistics_keys).issubset(
        list_statistics.keys()
    ), "All keys should be in ListStatistics"
    assert list_statistics["list"]["id"] == list_id


# -------------------------
# Lists
# -------------------------


def test_lists(load_user_pass, lists_response_keys, list_summary_keys):
    """
    /lists

    Assume use of environment variables for api key and secret
    """
    lbxd = letterboxd.new()
    # Login
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
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
    assert set(lists_response_keys).issubset(
        lists.keys()
    ), "All keys should be in the lists_response."

    list_summary = lists["items"][0]
    assert isinstance(list_summary, dict)
    # logging.debug("-------------------------\nlist_summary:")
    # logging.debug(pprint.pformat(list_summary))
    assert set(list_summary_keys).issubset(
        list_summary.keys()
    ), "All keys should be in list_summary."


def test_create_and_delete_list(load_user_pass, list_create_response_keys):
    """
    /lists [POST]
    """
    lbxd = letterboxd.new()
    # Login
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    list_creation_request = {
        "published": True,
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
    assert set(list_create_response_keys).issubset(
        list_create_response.keys()
    ), "All keys should be in the lists_response."

    # Clean up and delete this list
    created_list_id = list_create_response["data"]["id"]
    logging.debug(f"created_list_id: {created_list_id}")
    list = lbxd.list(created_list_id)
    success = list.delete(created_list_id)
    assert success == True
