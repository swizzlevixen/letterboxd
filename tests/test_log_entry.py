import logging
import letterboxd

logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


# I have combined some of the tests into one in order to be able to delete the entry after.
# This way there is no data left by the tests on letterboxd.

def test_create_edit_comment_delete_entry(load_user_pass, log_entries_response_keys, log_entry_keys,
                                          review_update_response_keys, review_comment_keys, review_comments_response_keys):
    lbxd = letterboxd.new()
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)

    # create a entry
    log_entry_creation_request = {
        "filmId": "H4Y",  # Cars 2
        "diaryDetails": {
            "diaryDate": "2020-07-20"
        },
        "review": {
            "text": "API_TEST - IGNORE",
            "containsSpoilers": False
        }
    }
    log_entries_instance = lbxd.entries(log_entry_creation_request)
    log_entries_response = log_entries_instance.post(log_entry_creation_request)
    assert isinstance(log_entries_response, dict)
    logging.debug(f"create_post_response_details: {log_entries_response}")
    logging.debug(f"create_post_response_details.keys(): {log_entries_response.keys()}")
    assert set(log_entry_keys).issubset(log_entries_response.keys()), "All keys should be in Keys."

    # remember this log-entry
    entry_id = log_entries_response["id"]

    # edit log entry
    log_entry_update_request = {
        "diaryDetails": {
            "diaryDate": "2020-07-21",
            "rewatch": True
        },
        "review": {
            "text": "API_TEST - IGNORE"
        },
        "rating": 5.0
    }
    update_log_entry_instance = lbxd.update_entry(entry_id=entry_id, log_entry_request=log_entry_update_request)
    review_update_response = update_log_entry_instance.update()
    assert isinstance(review_update_response, dict)
    logging.debug(f"review_update_response: {review_update_response}")
    logging.debug(f"review_update_response.keys(): {review_update_response.keys()}")
    assert set(review_update_response_keys).issubset(review_update_response.keys()), "All keys should be in Keys."

    # comment on entry
    comment_creation_request = {
        "comment": "This is just an API-test, no need to get exited!122!!!"
    }
    comment_on_log_entry_instance = lbxd.update_entry(entry_id=entry_id, log_entry_request=comment_creation_request)
    review_comment = comment_on_log_entry_instance.create_comment()
    assert isinstance(review_comment, dict)
    logging.debug(f"review_comment: {review_comment}")
    logging.debug(f"review_comment.keys(): {review_comment.keys()}")
    assert set(review_comment_keys).issubset(review_comment.keys()), "All keys should be in Keys."

    # get comments on entry
    comments_request = {
        "perPage": 1,
        "includeDeletions": False
    }
    commments_on_entry_instance = lbxd.update_entry(entry_id=entry_id, log_entry_request=comments_request)
    review_comments_response = commments_on_entry_instance.comments()
    assert isinstance(review_comments_response, dict)
    logging.debug(f"review_comments_response: {review_comments_response}")
    logging.debug(f"review_comments_response.keys(): {review_comments_response.keys()}")
    assert set(review_comments_response_keys).issubset(review_comments_response.keys()), "All keys should be in Keys."

    # get entry
    get_log_entry_instance = lbxd.entry(entry_id=entry_id)
    get_log_entry = get_log_entry_instance.get_id()
    assert isinstance(get_log_entry, dict)
    logging.debug(f"get_log_entry: {get_log_entry}")
    logging.debug(f"get_log_entry.keys(): {get_log_entry.keys()}")
    assert set(log_entry_keys).issubset(get_log_entry.keys()), "All keys should be in Keys."

    # delete entry
    delete_log_entry_instance = lbxd.entry(entry_id=entry_id)
    delete_log_entry = delete_log_entry_instance.delete()
    logging.debug(f"success: {delete_log_entry}")
    assert delete_log_entry is True


def test_get_entries(load_user_pass, log_entries_response_keys):
    lbxd = letterboxd.new()
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)

    log_entries_request = {} # get random entry

    log_entries_instance = lbxd.entries(log_entries_request)
    log_entries_response = log_entries_instance.get()
    assert isinstance(log_entries_response, dict)
    logging.debug(f"log_entries_response: {log_entries_response}")
    logging.debug(f"log_entries_response.keys(): {log_entries_response.keys()}")
    assert set(log_entries_response_keys).issubset(log_entries_response.keys()), "All keys should be in Keys."


def test_relationship(load_user_pass, review_relationship_keys):
    lbxd = letterboxd.new()
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    review_id = "1g6otb"
    log_entry_instance = lbxd.entry(entry_id=review_id)
    review_relationship = log_entry_instance.get_relationship()
    assert isinstance(review_relationship, dict)
    logging.debug(f"review_relationship: {review_relationship}")
    logging.debug(f"review_relationship.keys(): {review_relationship.keys()}")
    assert set(review_relationship_keys).issubset(review_relationship.keys()), "All keys should be in Keys."


def test_change_relationship(load_user_pass, review_relationship_update_response_keys):
    lbxd = letterboxd.new()
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    review_id = "1g6otb"
    review_relationship_update_request = {
        "liked": False,
        "subscribed": False
    }
    change_relationship_of_entry_instance = lbxd.update_entry(entry_id=review_id,
                                                              log_entry_request=review_relationship_update_request)
    review_relationship_update_response = change_relationship_of_entry_instance.update_relationship()
    assert isinstance(review_relationship_update_response, dict)
    logging.debug(f"review_relationship_update_response: {review_relationship_update_response}")
    logging.debug(f"review_relationship_update_response.keys(): {review_relationship_update_response.keys()}")
    assert set(review_relationship_update_response_keys)\
        .issubset(review_relationship_update_response.keys()), "All keys should be in Keys."


def test_report_entry(load_user_pass):
    lbxd = letterboxd.new()
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    review_id = "1g6otb"
    report_review_request = {"reason": "Other", "message": "API TEST — IGNORE :)"}
    report_entry_instance = lbxd.update_entry(entry_id=review_id, log_entry_request=report_review_request)
    report_status = report_entry_instance.report()
    assert report_status is True


def test_statistics(load_user_pass, review_statistics_keys):
    lbxd = letterboxd.new()
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    review_id = "1g6otb"
    statistics_entry_instance = lbxd.entry(entry_id=review_id)
    review_statistics = statistics_entry_instance.statistics()
    assert isinstance(review_statistics, dict)
    logging.debug(f"review_statistics: {review_statistics}")
    logging.debug(f"review_statistics.keys(): {review_statistics.keys()}")
    assert set(review_statistics_keys).issubset(
        review_statistics.keys()), "All keys should be in Keys."



