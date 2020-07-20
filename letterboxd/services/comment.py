import logging

logging.getLogger(__name__)


class Comment(object):
    """
    /comment for the Letterboxd API
    """

    def __init__(self, api, comment_id=None, comment_request=None):
        self._api = api
        self._comment_id = comment_id
        self._comment_request = comment_request

    def update(self, comment_id=None, comment_update_request=None):
        """
        [PATCH]/comment/{id}

        Update the message portion of a comment.
        Calls to this endpoint must include the access token for an authenticated member.
        Comments may only be edited by their owner.

        :param comment_id: string - id
        :param comment_update_request: dict - CommentUpdateRequest

        :return: comment_update_response - dict - CommentUpdateResponse
        """
        if comment_id is None:
            comment_id = self._comment_id
        if comment_update_request is None:
            comment_update_request = self._comment_request
        response = self._api.api_call(
            path=f"comment/{comment_id}",
            method="PATCH",
            params=comment_update_request,
        )
        comment_update_response = response.json()
        return comment_update_response

    def delete(self, comment_id=None):
        """
        [DELETE]/comment/{id}

        Delete a comment.
        Calls to this endpoint must include the access token for an authenticated member.
        Comments may be deleted by their owner, or by the owner of the thread to which they are posted.

        :param comment_id: string - id

        :return: bool - Success
        """
        if comment_id is None:
            comment_id = self._comment_id
        response = self._api.api_call(
            path=f"comment/{comment_id}", method="DELETE", params={}
        )
        if response.status_code == 204:
            # 204: Success
            return True
        else:
            return False

    def report(self, comment_id=None, report_comment_request=None):
        """
        [PATCH]/comment/{id}

        Update the message portion of a comment.
        Calls to this endpoint must include the access token for an authenticated member.
        Comments may only be edited by their owner.

        :param comment_id: string - id
        :param report_comment_request: dict - ReportCommentRequest

        :return: comment_update_response - dict - CommentUpdateResponse
        """
        if comment_id is None:
            comment_id = self._comment_id
        if report_comment_request is None:
            report_comment_request = self._comment_request
        response = self._api.api_call(
            path=f"comment/{comment_id}/report",
            method="PATCH",
            params=report_comment_request,
        )
        if response.status_code == 204:
            # 204: Success
            return True
        else:
            return False
