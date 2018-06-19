"""
Communication methods for the Letterboxd API

API Documentation:
http://api-docs.letterboxd.com/
"""
import hashlib
import hmac
import logging
import requests
import time
import uuid

logging.getLogger(__name__)

CHARLES_PROXY = "http://localhost:8888/"

class API():
    """
    Letterboxd API helpers
    """
    def __init__(self, api_base, api_key, api_secret):
        self.api_base = api_base
        self.api_key = api_key
        self.api_secret = api_secret

        if (self.api_key == ""):
            # If the API key wasn't passed in
            class APIKeyMissingError(Exception):
                pass

            raise APIKeyMissingError(
                    "All methods require an API key. See "
                    "https://letterboxd.com/api-coming-soon/ "
                    "for more information"
            )

        if (self.api_secret == ""):
            # If the API shared secret wasn't passed in
            class APISecretMissingError(Exception):
                pass

            raise APISecretMissingError(
                    "All methods require an API secret. See "
                    "https://letterboxd.com/api-coming-soon/ "
                    "for more information"
            )

        # Start the shared requests session
        self.session = requests.Session()
        self.session.params = {}

        # TODO: Put the auth.py call here, if we have a user/pass
        self.token = ''


    def api_call(self, path, params = {}, form = None, headers = {}, method = "get"):
        """
        :param path: string - The endpoint for the service
        :param params: dictionary - of parameters
        :param form: string - the form information from the auth.py call
        :param headers: dictionary - dictionary of parameters
        :param method: string - HTML methods get, post, put, patch
        :return: ??? response
        """

        # If we have an oAuth token
        if self.token:
            headers["Authorization"] = 'Bearer {}'.format(self.token)

        url = "{}/{}".format(self.api_base, path)

        logging.debug(
            "\nurl: {}\nparams: {}\nform: {}\nheaders: {}\nmethod: {}\n-------------------------".format(url, params,
                                                                                                         form, headers,
                                                                                                         method))

        # Is there any other need to use `form` than for an oAuth call?
        # should some of this code be in there instead?
        if form:
            params['form'] = form
            headers["Content-Type"] = "application/x-www-form-urlencoded"



        # TODO: Ruby representation that needs re-writing

        # if form:
        #     params['form'] = form
        #     headers["Content-Type"] = "application/x-www-form-urlencoded"
        #     signature = self.__sign(method.upper(), url, body)
        #     headers["Authorization"] = "Signature {}".format(signature)
        # elif method.lower() in ['post', 'put', 'patch']:
        #     params = self.__remove_empty_from_dict(params)
        #     body = json_data = json.dumps(params)
        #     signature = self.__sign(method.upper(), url, body)
        #     url = self.__add_params(url, signature)
        # else:
        #     body = ""
        #     url = self.__add_params(url, params)
        #     signature = self.__sign(method.upper(), url)
        #     url = self.__add_params(url, signature)

        prepared_request = self.__prepare_request(url, params = params, headers = headers, method = method)
        logging.debug(prepared_request.url)
        response = self.session.send(prepared_request)
        logging.debug(response.status_code)
        logging.debug(type(response))
        # TODO: if status code 200 or 204(?), return the response JSON decoded, else handle the error
        return response


    # -------------------------
    # Private methods


    def __prepare_request(self, url, params = {}, data = [], headers = {}, method = "get", form = False):
        """
        Prepare the request and sign it
        :param url: string
        :param params: dict
        :param form: bool
        :param headers: dict
        :param method: string - get, post, put, patch
        :return: ??? prepared_request
        """
        # TODO: Probably need to do an if: for Form == True differences
        # Add the request metadata required for uniquely identifying the request
        params = self.__add_metadata(params)

        # Prepare the request and add it to the current requests session
        request = requests.Request(method.upper(), url, params = params, data = data, headers = headers)
        prepared_request = self.session.prepare_request(request)

        logging.debug("prepared url: {}".format(prepared_request.url))
        # Sign the request
        signature = self.__sign(method = method.upper(), url = prepared_request.url)
        # Add the signature to the end of the params in the url
        prepared_request.prepare_url(prepared_request.url, {'signature': signature})
        logging.debug(type(prepared_request))
        return prepared_request


    def __remove_empty_from_dict(self, dirty_dict):
        """
        Takes a dictionary recursively removes all None and "" values
        :param dirty_dict: dict
        :return: dict
        """
        logging.debug("params: {}".format(dirty_dict))
        cleaned_dict = {}
        for key, value in dirty_dict.items():
            logging.debug("key: {}, value: {}".format(key, value))

            if (value is None) or (value is ""):
                logging.debug("Toss the value!")
            elif isinstance(value,dict):
                this_dict = self.__remove_empty_from_dict(value)
                cleaned_dict[key] = this_dict
            elif isinstance(value,tuple) or isinstance(value, list):
                cleaned_dict[key] = self.__remove_empty_from_list(value)
            else:
                cleaned_dict[key] = value
            logging.debug("-------------------------")
        logging.debug("result: {}".format(cleaned_dict))
        return cleaned_dict


    def __remove_empty_from_list(self, dirty_list):
        """
        Takes a tuple or list and recursively removes all None and "" values
        :param dirty_list: tuple or list
        :return: list
        """
        cleaned_list = []
        for __item in dirty_list:
            logging.debug(__item)
            if __item is "" or __item is None:
                logging.debug("item {} is {}".format(__item, "None"))
                pass
            elif isinstance(__item, dict):
                logging.debug("item {} is {}".format(__item, "dict"))
                cleaned_list.append(self.__remove_empty_from_dict(__item))
            elif isinstance(__item,tuple) or isinstance(__item, list):
                logging.debug("item {} is {}".format(__item, "tuple or list"))
                cleaned_list.append(self.__remove_empty_from_list(__item))
            else:
                logging.debug("item {} is {}".format(__item, "else"))
                cleaned_list.append(__item)
        return cleaned_list


    def __rest_call(self, method, url, body, headers):
        """
        Do the rest call
        :param method: str - get, post, put, patch
        :param url: str
        :param body: str - JSON encoded
        :param headers: dict
        :return: ???
        """
        # TODO: This isn't actually hooked up to anything yet.
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


    def __add_metadata(self, params):
        """
        Adds the metadata params required for signing the request
        :param params: dict
        :return: dict
        """
        params['apikey'] = self.api_key
        # nonce: UUID string, must be unique for each API request
        params['nonce'] = uuid.uuid4()
        # timestamp: number of seconds since epoch, Jan 1, 1970 (UTC)
        params['timestamp'] = int(time.time())
        return params


    def __sign(self, method, url, body=""):
        """
        Create a salted string as bytes, of the form [METHOD]\x00[URL]\x00[BODY],
        where [METHOD] is GET, POST, etc., [URL] is the fully-qualified request
        URL including the apikey, nonce, timestamp and any other method parameters,
        and [BODY] is a JSON-encoded string (for POST, PATCH and DELETE requests)
        or empty (for GET requests). Next, create a [SIGNATURE] from the salted
        string by applying a lower-case HMAC/SHA-256 transformation, using your
        API Secret, and append it to your API request URL as the final query
        parameter: …&signature=[SIGNATURE]

        Notes: you must specify a Content-Type: application/json request header
        if [BODY] is JSON-encoded. The apikey parameter is your supplied API Key.
        The nonce parameter should be a UUID string and must be unique for each
        API request. The timestamp parameter is the number of seconds since
        Jan 1, 1970 (UTC), also know as "UNIX Epoch time."

        :param method: str - get, post, put, patch
        :param url: str
        :param body: str - JSON-encoded
        :return: str
        """
        # Create the salted bytestring
        signing_bytestring = b"\x00".join([str.encode(method), str.encode(url), str.encode(body)])
        logging.debug('signing_bytestring: type: {}, value: {}'.format(type(signing_bytestring), signing_bytestring))
        # applying an HMAC/SHA-256 transformation, using our API Secret
        signature = hmac.new(str.encode(self.api_secret), signing_bytestring, digestmod=hashlib.sha256)
        # get the string representation of the hash
        signature_string = signature.hexdigest()
        return signature_string
