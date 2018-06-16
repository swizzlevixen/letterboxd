import json
import logging
import requests
import time
import urllib
import uuid
##### Ruby implementation
#
# require 'net/http'
# require 'rubygems'
# require 'rest-client'
# require 'date'
# require 'uri'
# require 'securerandom'
# require 'openssl'
# require 'base64'

CHARLES_PROXY = "http://localhost:8888/"

class API():
    """
    Letterboxd API helpers
    """
    def __init__(self, api_base, api_key, api_secret):
        self.api_base = api_base
        self.api_key = api_key
        self.api_secret = api_secret

        # Start the shared requests session
        self.session = requests.Session()
        self.session.params = {}
        self.session.params['api_key'] = self.api_key

        # TODO: Put the auth.py call here, if we have a user/pass
        self.token = ''

    def api_call(self, path, params = {}, form = None, headers = {}, method = "get"):
        """
        :param path: string - The endpoint for the service
        :param params: dictionary - of parameters
        :param form: string - the form information from the auth.py call
        :param headers: dictionary - JSON object
        :param method: string - HTML methods get, post, put, patch
        :return: 
        """

        # If we have an oAuth token
        if self.token:
            headers["Authorization"] = 'Bearer {}'.format(self.token)

        url = self.__add_metadata("{}/{}".format(self.api_base, path))
        logging.debug('url: {}'.format(url))

        if form:
            params['form'] = form
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            signature = self.__sign(method.upper(), url, body)
            headers["Authorization"] = "Signature {}".format(signature)
        elif method.lower() in ['post', 'put', 'patch']:
            params = self.__remove_nil_params(params)
            body = json_data = json.dumps(params)
            signature = self.__sign(method.upper(), url, body)
            url = self.__add_params(url, signature)
        else:
            body = ""
            url = self.__add_params(url, params)
            signature = self.__sign(method.upper(), url)
            url = self.__add_params(url, signature)

    # Methods after this should be private

    # Remove empty params
    def __remove_nil_params(self, params):
        result = {k: v for k, v in params.items() if v is not None}
        return result

    # Do the rest call
    def __rest_call(self, method, url, body, headers):
        try:
            if method.lower() == 'post':
                self.session.post(url, json=body, headers=headers)
            elif method.lower() == 'put':
                self.session.put(url, json = body, headers = headers)
            elif method.lower() == 'patch':
                self.session.patch(url, json = body, headers = headers)
            else:
                self.session.get(url, headers = headers)
        except Exception as e:
            logging.error("__rest_call: {}".format(e))


    def __add_params(self, url, params):
        pass

#   def add_params(url, params)
#     uri = URI(url)
#     query = URI.decode_www_form(uri.query || "")
#     params.each { |k,v| query << [k,v == :null ? nil : v] unless v.nil? || ( v.is_a?(Array) && v.empty? ) }
#     uri.query = URI.encode_www_form(query)
#     uri.to_s
#   end

    def __add_metadata(self, url):
        # nonce: UUID string, must be unique for each API request
        nonce = uuid.uuid4()
        # timestamp: number of seconds since epoch, Jan 1, 1970 (UTC)
        timestamp = int(time.time())
        self.__add_params(url, {'apikey': self.api_key, 'nonce': nonce, 'timestamp': timestamp})

#   def add_metadata url
#     add_params url, {:apikey => @api_key, :nonce => SecureRandom.uuid, :timestamp => Time.now.to_i}
#   end

    def __sign(self, method, url, body=""):
            pass

#   def sign method, url, body = ""
#     str = "#{method}\u0000#{url}\u0000#{body}"
#     signature = OpenSSL::HMAC.digest("sha256", @api_secret, str).unpack("H*")[0].downcase
#   end
