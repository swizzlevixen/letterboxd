#! /usr/bin/env python3
import logging

from letterboxd.letterboxd import Letterboxd
from tests.letterboxd_definitions import *
from tests.test_letterboxd import load_user_pass

logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def test_search():
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    search_request = {
        "perPage": 5,
        "input": "smith",
        "searchMethod": "FullText",
        "include": "ContributorSearchItem",
        "contributionType": "Director",
    }
    search_response = lbxd.search(search_request=search_request)
    logging.debug(f"search_response: {search_response}")
    assert isinstance(search_response, dict)
    # TODO: test returned keys

    assert set(search_response_keys()).issubset(
        search_response.keys()
    ), "All keys should be in SearchResponse"

    abstract_search_item = search_response["items"][0]
    assert set(abstract_search_item_keys()).issubset(
        abstract_search_item.keys()
    ), "All keys should be in the AbstractSearchItem"
