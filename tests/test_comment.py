import logging

import pytest

import letterboxd
from tests.letterboxd_definitions import *
from tests.test_letterboxd import load_user_pass

logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def test_create_edit_delete_comment(load_user_pass, review_comment_keys, comment_update_response_keys):
    # commenting requires authentication
    lbxd = letterboxd.new()
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)

    # create a entry to test comments on
    log_entry_creation_request = {
        "filmId": "29ho",  # Cars
        "diaryDetails": {
            "diaryDate": "2020-07-20"
        },
        "review": {
            "text": "API_TEST - IGNORE",
            "containsSpoilers": False
        }
    }
    entry_instance = lbxd.entries(log_entry_creation_request)
    log_entry = entry_instance.post() # Not testing this as it is not the meaning of this test

    # set entry_id to refer to this entry so that we only work inside it.
    entry_id = log_entry["id"]

    # post comment on entry
    comment_creation_request = {
        "comment": "This is just an API-test, no need to get exited!122!!!"
    }
    create_comment_instance = lbxd.update_entry(entry_id=entry_id, log_entry_request=comment_creation_request)
    review_comment = create_comment_instance.create_comment()
    assert isinstance(review_comment, dict)
    logging.debug(f"review_comment: {review_comment}")
    logging.debug(f"review_comment.keys(): {review_comment.keys()}")
    assert set(review_comment_keys).issubset(review_comment.keys()), "All keys should be in Keys."

    # set comment_id to refer to this entry so that we only work on it.
    comment_id = review_comment["id"]

    # edit the text of the comment
    comment_update_request = {
        "comment": "This comment was updated using the API"
    }
    comment_update_instance = lbxd.update_comment(comment_id=comment_id, comment_request=comment_update_request)
    comment_update_response = comment_update_instance.update()
    assert isinstance(comment_update_response, dict)
    logging.debug(f"comment_update_response: {comment_update_response}")
    logging.debug(f"comment_update_response.keys(): {comment_update_response.keys()}")
    assert set(comment_update_response_keys).issubset(comment_update_response.keys()), "All keys should be in Keys."

    # delete the comment
    comment_deletion_instance = lbxd.delete_comment(comment_id=comment_id)
    success = comment_deletion_instance.delete()
    logging.debug(f"success: {success}")
    assert success is True

    # delete the entry
    entry_instance = lbxd.entry(entry_id=entry_id)
    delete_log_entry = entry_instance.delete() # Not testing this as it is not the meaning of this test
    logging.debug(f"success: {delete_log_entry}")




