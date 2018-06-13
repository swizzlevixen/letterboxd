import os
import requests


LBX_API_KEY = os.environ.get('LBX_API_KEY', None)

class APIKeyMissingError(Exception):
    pass

if LBX_API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "https://letterboxd.com/api-coming-soon/ "
        "for more information"
    )

session = requests.Session()
session.params = {}
session.params['api_key'] = LBX_API_KEY

from letterboxd.services.film import Film
