import hashlib
import hmac
import json
import logging
import os
import time
import uuid

import requests

logging.getLogger(__name__)

CHARLES_PROXY = "http://localhost:8888/"
CHARLES_CERTIFICATE = os.environ.get("CHARLES_CERTIFICATE", None)
CHARLES = os.environ.get("CHARLES", None)


class API:
    """
    Communication methods for the Letterboxd API
    """

    def __init__(self, api_base, api_key, api_secret):
        """
        This method will start the shared requests session for the Letterboxd
        API. If the API key and secret are not passed, the initializer will
        attempt to get them from the environment variables.

        :param api_base: str - the base URL of the API endpoints, including version number
        :param api_key: str - API key provided by Letterboxd
        :param api_secret: str - API shared secret provided by Letterboxd
        """
        self.api_base = api_base
        self.api_key = api_key
        self.api_secret = api_secret
        self.user = None

        if self.api_key == "":
            # If the API key wasn't passed in
            class APIKeyMissingError(Exception):
                pass

            raise APIKeyMissingError(
                "All methods require an API key. See "
                "https://letterboxd.com/api-coming-soon/ "
                "for more information"
            )

        if self.api_secret == "":
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

    def api_call(self, path, params={}, form=None, headers={}, method="get"):
        """
        The workhorse method of calls to the Letterboxd API

        :param path: str - URL endpoint path for the desired service
        :param params: dict - request parameters
        :param form: str - form information, likely from the auth.py call
        :param headers: dict - request parameters
        :param method: str - HTML methods, [get, post, put, patch]
        :return: requests.Response object
        """

        # If we have an oAuth token
        if self.user:
            headers["Authorization"] = f"Bearer {self.user.token}"

        url = f"{self.api_base}/{path}"

        logging.debug(
            f"\n"
            f"url: {url}\n"
            f"params: {params}\n"
            f"form: {form}\n"
            f"headers: {headers}\n"
            f"method: {method}\n"
            f"-------------------------"
        )

        if form:
            # `form` seems to only be used in an oAuth call?
            # should some of this code be in there instead?
            logging.debug("API.api_call() if form")
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            # Prepare the request
            prepared_dict = self.__prepare_request(
                url, body=form, headers=headers, method=method
            )
            prepared_request = prepared_dict["prepared_request"]
            signature = prepared_dict["signature"]
            # Add the signature to the headers
            prepared_request.headers["Authorization"] = f"Signature {signature}"
        elif method.lower() in ["post", "put", "patch"]:
            logging.debug(
                'API.api_call() elif method.lower() in ["post", "put", "patch"]:'
            )
            params = self.__remove_empty_from_dict(params)
            # JSON-encode the body
            body = json.dumps(params)
            headers["Content-Type"] = "application/json"
            # prepare the request
            prepared_dict = self.__prepare_request(
                url, body=body, headers=headers, method=method
            )
            prepared_request = prepared_dict["prepared_request"]
            signature = prepared_dict["signature"]
            # Attach the signature
            prepared_request.prepare_url(prepared_request.url, {"signature": signature})
        else:
            logging.debug("API.api_call() else:")
            # It's a GET
            # Prepare the request
            prepared_dict = self.__prepare_request(
                url, params=params, headers=headers, method=method
            )
            prepared_request = prepared_dict["prepared_request"]
            signature = prepared_dict["signature"]
            logging.debug(prepared_request.url)
            # Add the signature to the end of the params in the url
            prepared_request.prepare_url(prepared_request.url, {"signature": signature})

        logging.debug(
            f"API.api_call() prepared_request\n"
            f"method: {prepared_request.method}\n"
            f"url: {prepared_request.url}\n"
            f"headers: {prepared_request.headers}\n"
            f"body: {prepared_request.body}"
        )

        try:
            # If we've set the environment variable, run with Charles proxy
            if CHARLES == "True":
                # First, make sure we have the correct settings
                if (
                    logging.getLogger().isEnabledFor(logging.DEBUG)
                    and CHARLES_CERTIFICATE
                ):
                    logging.debug("Send prepared_request through Charles")
                    proxies = {"http": CHARLES_PROXY, "https": CHARLES_PROXY}
                    self.session.verify = CHARLES_CERTIFICATE
                    # send the request through the proxy
                    response = self.session.send(prepared_request, proxies=proxies)
            else:
                # send the request normally
                logging.debug("Send prepared_request")
                response = self.session.send(prepared_request)
        except ConnectionError as error:
            logging.error(error)
            raise

        # Return the response
        logging.debug(f"api_call() response.status_code: {response.status_code}")
        if response.status_code is requests.codes.ok:
            return response
        else:
            response.raise_for_status()
            return response

    # -------------------------
    # Private methods

    def __prepare_request(
        self, url, params={}, body=[], headers={}, method="get", form=False
    ):
        """
        Prepare the request and sign it

        :param url: string
        :param params: dict
        :param form: bool
        :param headers: dict
        :param method: string - get, post, put, patch
        :return: dict - {'prepared_request', 'signature'}
        """
        # Add the request params required for uniquely identifying the request
        params = self.__add_unique_params(params)

        # Prepare the request and add it to the current requests session
        request = requests.Request(
            method.upper(), url, params=params, data=body, headers=headers
        )
        prepared_request = self.session.prepare_request(request)

        logging.debug(f"prepared url: {prepared_request.url}")
        # Hash the request signature
        signature = self.__sign(
            method=prepared_request.method,
            url=prepared_request.url,
            body=prepared_request.body,
        )
        return {"prepared_request": prepared_request, "signature": signature}

    def __remove_empty_from_dict(self, dirty_dict):
        """
        Takes a dictionary recursively removes all None and "" values

        :param dirty_dict: dict
        :return: dict
        """
        logging.debug(f"params: {dirty_dict}")
        cleaned_dict = {}
        for key, value in dirty_dict.items():
            logging.debug(f"key: {key}, value: {value}")

            if (value is None) or (value is ""):
                logging.debug("Toss the value!")
            elif isinstance(value, dict):
                this_dict = self.__remove_empty_from_dict(value)
                cleaned_dict[key] = this_dict
            elif isinstance(value, tuple) or isinstance(value, list):
                cleaned_dict[key] = self.__remove_empty_from_list(value)
            else:
                cleaned_dict[key] = value
            logging.debug("-------------------------")
        logging.debug(f"result: {cleaned_dict}")
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
                logging.debug(f"item {__item} is None")
                pass
            elif isinstance(__item, dict):
                logging.debug(f"item {__item} is dict")
                cleaned_list.append(self.__remove_empty_from_dict(__item))
            elif isinstance(__item, tuple) or isinstance(__item, list):
                logging.debug(f"item {__item} is tuple or list")
                cleaned_list.append(self.__remove_empty_from_list(__item))
            else:
                logging.debug(f"item {__item} is else")
                cleaned_list.append(__item)
        return cleaned_list

    def __add_unique_params(self, params):
        """
        Adds the metabody params required for signing the request

        :param params: dict
        :return: dict
        """
        params["apikey"] = self.api_key
        # nonce: UUID string, must be unique for each API request
        params["nonce"] = uuid.uuid4()
        # timestamp: number of seconds since epoch, Jan 1, 1970 (UTC)
        params["timestamp"] = int(time.time())
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
        if body == None:
            body = ""
        signing_bytestring = b"\x00".join(
            [str.encode(method), str.encode(url), str.encode(body)]
        )
        logging.debug(f"signing_bytestring: {signing_bytestring}")
        # applying an HMAC/SHA-256 transformation, using our API Secret
        signature = hmac.new(
            str.encode(self.api_secret), signing_bytestring, digestmod=hashlib.sha256
        )
        # get the string representation of the hash
        signature_string = signature.hexdigest()
        return signature_string
