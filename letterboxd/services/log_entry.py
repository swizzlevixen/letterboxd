import logging

logging.getLogger(__name__)


class LogEntry(object):
    """
    /log-entries for the Letterboxd API
    """

    def __init__(self, api, entry_id=None, log_entry_request=None):
        self._api = api
        self._entry_id = entry_id
        self._log_entry_request = log_entry_request

    def get(self, log_entry_request=None):
        """
        [GET]/log-entries

        A cursored window over the log entries for a film or member.

        :param log_entry_request: dict - LogEntriesRequest

        :return: log_entries_response - dict - LogEntriesResponse
        """
        if log_entry_request is None:
            log_entry_request = self._log_entry_request
        response = self._api.api_call(path="log-entries", params=log_entry_request)
        log_entries_response = response.json()
        return log_entries_response

    def post(self, log_entry_request=None):
        """
        [POST]/log-entries

        Create a log entry. A log entry is either a diary entry (must have a date) or a review (must have review text).
        Log entries can be both a diary entry and a review if they satisfy both criteria.

        :param log_entry_request: dict - LogEntryCreationRequest

        :return: log_entry_response - dict - LogEntry
        """
        if log_entry_request is None:
            log_entry_request = self._log_entry_request

        response = self._api.api_call(
            path="log-entries", method="POST", params=log_entry_request
        )
        log_entry_response = response.json()
        return log_entry_response

    def get_id(self, log_entry_id):
        """
        [GET]/log-entry/{id}

        Get details about a log entry by ID.

        :param log_entry_id: string - id

        :return: log_entry_response - dict - LogEntry
        """
        if log_entry_id is None:
            log_entry_id = self._entry_id
        response = self._api.api_call(path=f"log-entry/{log_entry_id}")
        log_entry_response = response.json()
        return log_entry_response

    def update(self, entry_id=None, log_entry_update_request=None):
        """
        [PATCH]/log-entry/{id}

        Update a log entry by ID.
        Calls to this endpoint must include the access token for an authenticated member

        :param entry_id: string - id
        :param log_entry_update_request: dict - LogEntryUpdateRequest

        :return: review_update_response - dict - ReviewUpdateResponse
        """
        if entry_id is None:
            entry_id = self._entry_id
        if log_entry_update_request is None:
            log_entry_update_request = self._log_entry_request
        response = self._api.api_call(
            path=f"log-entry/{entry_id}",
            method="PATCH",
            params=log_entry_update_request,
        )
        log_entry_response = response.json()
        return log_entry_response

    def delete(self, entry_id=None):
        """
        [DELETE]/log-entry/{id}

        Delete a log entry by ID.
        Calls to this endpoint must include the access token for an authenticated member

        :param entry_id: string - id

        :return: bool - Success
        """
        if entry_id is None:
            entry_id = self._entry_id
        response = self._api.api_call(
            path=f"log-entry/{entry_id}", method="DELETE", params={}
        )
        if response.status_code == 204:
            # 204: Success
            return True
        else:
            return False

    def comments(self, entry_id=None, comments_request=None):
        """
        [GET]/log-entry/{id}/comments

        A cursored window over the comments for a log entry’s review.
        Use the ‘next’ cursor to move through the comments.

        :param entry_id: string - id
        :param comments_request: dict - CommentsRequest

        :return: review_comments_response - dict - ReviewCommentsResponse
        """
        if entry_id is None:
            entry_id = self._entry_id
        if comments_request is None:
            comments_request = self._log_entry_request
        response = self._api.api_call(
            path=f"log-entry/{entry_id}/comments", params=comments_request
        )
        review_comments_response = response.json()
        return review_comments_response

    def create_comment(self, entry_id=None, comment_creation_request=None):
        """
        [POST]/log-entry/{id}/comments

        Create a comment on a review.
        Calls to this endpoint must include the access token for an authenticated member

        :param entry_id: string - id
        :param comment_creation_request: dict - CommentCreationRequest

        :return: review_comments_response - dict - ReviewComment
        """
        if entry_id is None:
            entry_id = self._entry_id
        if comment_creation_request is None:
            comment_creation_request = self._log_entry_request
        response = self._api.api_call(
            path=f"log-entry/{entry_id}/comments",
            params=comment_creation_request,
            method="POST",
        )
        review_comments_response = response.json()
        return review_comments_response

    def get_relationship(self, entry_id=None):
        """
        [GET]/log-entry/{id}/me

        Get details of the authenticated member’s relationship with a log entry’s review by ID.
        Calls to this endpoint must include the access token for an authenticated member

        :param entry_id: string - id

        :return: review_relationship - dict - ReviewRelationship
        """
        if entry_id is None:
            entry_id = self._entry_id
        response = self._api.api_call(path=f"log-entry/{entry_id}/me")
        review_relationship = response.json()
        return review_relationship

    def update_relationship(
        self, entry_id=None, review_relationship_update_request=None
    ):
        """
        [PATCH]/log-entry/{id}/me

        Update the authenticated member’s relationship with a log entry’s review by ID.
        Calls to this endpoint must include the access token for an authenticated member

        :param review_relationship_update_request: dict - ReviewRelationshipUpdateRequest
        :param entry_id: string - id

        :return: review_relationship - dict - ReviewRelationshipUpdateResponse
        """
        if entry_id is None:
            entry_id = self._entry_id
        if review_relationship_update_request is None:
            review_relationship_update_request = self._log_entry_request
        response = self._api.api_call(
            path=f"log-entry/{entry_id}/me",
            params=review_relationship_update_request,
            method="PATCH",
        )
        review_relationship = response.json()
        return review_relationship

    def report(self, entry_id=None, report_review_request=None):
        """
        [POST]/log-entry/{id}/report

        Report a log entry’s review by ID.
        Calls to this endpoint must include the access token for an authenticated member

        :param report_review_request: dict - ReportReviewRequest
        :param entry_id: string - id

        :return: :return: bool - Success
        """
        if entry_id is None:
            entry_id = self._entry_id
        if report_review_request is None:
            report_review_request = self._log_entry_request
        response = self._api.api_call(
            path=f"log-entry/{entry_id}/report",
            params=report_review_request,
            method="POST",
        )
        if response.status_code == 204:
            # 204: Success
            return True
        else:
            return False

    def statistics(self, entry_id=None):
        """
        [GET]/log-entry/{id}/statistics

        Get statistical data about a log-entry’s review by ID.

        :param entry_id: string - id

        :return: review_statistics_response - dict - ReviewStatistics
        """
        if entry_id is None:
            entry_id = self._entry_id
        response = self._api.api_call(path=f"log-entry/{entry_id}/statistics")
        review_statistics_response = response.json()
        return review_statistics_response
