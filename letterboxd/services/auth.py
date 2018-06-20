"""
User authentication services for the Letterboxd API

Authentication API Documentation:
http://api-docs.letterbotokend.com/#auth
"""

import logging
import requests
from requests_oauthlib import oauth2_auth

logging.getLogger(__name__)


class Authentication:
    """
    User authentication services for Letterboxd
    """

    def __init__(self):
        self._token = None

    @property
    def token(self):
        logging.debug("getter of token called")
        return self._token

    @token.setter
    def token(self, value):
        logging.debug("setter of token called")
        self._token = value

    @token.deleter
    def token(self):
        logging.debug("deleter of token called")
        del self._token

    def login(username, password):
        pass


##### The Ruby implementation:
#
# module Auth
#
#   attr_reader :token
#
#   def login username, password
#     login_response = api "auth/token", method: "post", form: [["grant_type", "password"], ["username", username], ["password", password]]
#     # login_response = api "auth/token", method: "post", params: {grant_type: "password", username: username, password: password}
#     json = JSON.parse(login_response.to_s)
#     @token = json["access_token"]
#     raise "Unable to log in" unless @token
#     login_response
#   end
#
# end
