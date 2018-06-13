import os
import requests

# Load in the basic API information and make sure it's there.

API_KEY = os.environ.get('LBX_API_KEY', None)

class APIKeyMissingError(Exception):
    pass

if API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "https://letterboxd.com/api-coming-soon/ "
        "for more information"
    )

API_SECRET = os.environ.get('LBX_API_SECRET', None)

class APISecretMissingError(Exception):
    pass

if API_SECRET is None:
    raise APISecretMissingError(
        "All methods require an API secret. See "
        "https://letterboxd.com/api-coming-soon/ "
        "for more information"
    )

API_BASE = 'https://api.letterboxd.com/api/v0'

# Start the shared requests session
session = requests.Session()
session.params = {}
session.params['api_key'] = API_KEY
