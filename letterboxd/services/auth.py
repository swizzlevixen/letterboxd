"""
Authentication services for the Letterboxd API
"""

import requests
from requests_oauthlib import oauth2_auth

def token(username, password):


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
