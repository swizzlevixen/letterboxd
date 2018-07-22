#! /usr/bin/env python3
import datetime
import logging
import pprint

import letterboxd
from tests.letterboxd_definitions import *
from tests.test_letterboxd import load_user_pass

logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

# -------------------------
# List
# -------------------------


def test_list_details():
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
    assert set(list_keys()).issubset(list_details.keys()), "All keys should be in Keys."


def test_list_comments():
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
    assert set(list_comments_response_keys()).issubset(
        list_comments_response.keys()
    ), "All keys should be in ListCommentsResponse"

    list_comment = list_comments_response["items"][0]
    assert list_comment["list"]["id"] == list_id
    logging.debug(f"list_comment: {list_comment}")
    logging.debug(f"list_comment.keys(): {list_comment.keys()}")
    assert set(list_comment_keys()).issubset(
        list_comment.keys()
    ), "All keys should be in ListComment"


def test_list_create_comment():
    lbxd = letterboxd.new()
    # Login
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    comment_creation_request = {
        "comment": "Here's a comment with some <strong>strong</strong> language, <em>emphasized</em>, <b>bold</b>, <i>italics</i>, a <a href=\"http://opticalpodcast.com\">link</a>, and here's a quote:\n\n<blockquote>We have nothing to fear but fear itself. And werewolves.\n\n—FDR, Werewolf Hunter</blockquote>"
    }
    list_id = "1UxUo"

    list = lbxd.list(list_id=list_id)
    list_comment = list.create_comment(
        comment_creation_request=comment_creation_request
    )
    logging.debug(f"list_comment: {list_comment}")
    assert isinstance(list_comment, dict)

    logging.debug(f"list_comment.keys(): {list_comment.keys()}")
    assert set(list_comment_keys()).issubset(
        list_comment.keys()
    ), "All keys should be in ListComment"


# TODO: Test all /list/* endpoints


# -------------------------
# Lists
# -------------------------


def test_lists():
    """
    /lists

    Assume use of environment variables for api key and secret
    """
    lbxd = letterboxd.new()
    # Login
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


def test_create_list():
    """
    /lists [POST]
    """
    lbxd = letterboxd.new()
    # Login
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
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
    assert set(list_create_response_keys()).issubset(
        list_create_response.keys()
    ), "All keys should be in the lists_response."
    # I can't clean up and delete the list after creation,
    # because there is no API for deleting a list.
