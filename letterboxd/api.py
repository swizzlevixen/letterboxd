import json
import requests
import time
import uuid
from letterboxd.letterboxd import Letterboxd
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

    def api(self, path, params = {}, form = None, headers = {}, method = "get"):
        """
        :param path: The endpoint for the service
        :param params: dictionary of parameters
        :param form: ???
        :param headers: dictionary - JSON object
        :param method: string - HTML methods get, post, put, patch
        :return: 
        """

        if self.token:
            headers["Authorization"] = 'Bearer {}'.format(self.token)

        url = self.add_metadata("{}/{}".format(self.api_base, self.path))

        if form:
            pass
        elif method.lower() in ['post', 'put', 'patch']:
            params = self.remove_nil_params(params)
            body = json_data = json.dumps(params)
            signature = self.sign(method.upper(), url, body)
            url = self.add_params(url, signature)
        else:
            body = ""
            url = self.add_params(url, params)
            signature = self.sign(method.upper(), url)
            url = self.add_params(url, signature)

    # Remove nil params, and replace :null with nil
    def remove_nil_params(self, params):
        pass

    def rest_call (self, method, url, body, headers):
        pass

    def add_params(self, url, params):
        pass

    def add_metadata(self, url):
        # nonce: UUID string, must be unique for each API request
        nonce = uuid.uuid4()
        # timestamp: number of seconds since epoch, Jan 1, 1970 (UTC)
        timestamp = int(time.time())
        self.add_params(url, {'apikey': self.api_key, 'nonce': nonce, 'timestamp': timestamp})

    def sign(self, method, url, body=""):
            pass


# Ruby implementation
#
#   private

    def __remove_nil_params(self, params):
        result = {k: v for k, v in params.items() if v is not None}
        return result


    def __rest_call(self, method, url, body, headers):
        if method.lower() in ['post', 'put', 'patch']:



#
#   def rest_call method, url, body, headers
#     begin
#       if method.downcase =~ /(post|put|patch)/
#         RestClient.send method.downcase, url, body, headers
#       else
#         RestClient.send method.downcase, url, headers
#       end
#     rescue RestClient::ExceptionWithResponse => e
#       e.response
#     end
#   end
#
#   def add_params(url, params)
#     uri = URI(url)
#     query = URI.decode_www_form(uri.query || "")
#     params.each { |k,v| query << [k,v == :null ? nil : v] unless v.nil? || ( v.is_a?(Array) && v.empty? ) }
#     uri.query = URI.encode_www_form(query)
#     uri.to_s
#   end
#
#   def add_metadata url
#     add_params url, {:apikey => @api_key, :nonce => SecureRandom.uuid, :timestamp => Time.now.to_i}
#   end
#
#   def sign method, url, body = ""
#     str = "#{method}\u0000#{url}\u0000#{body}"
#     signature = OpenSSL::HMAC.digest("sha256", @api_secret, str).unpack("H*")[0].downcase
#   end
#
# end
