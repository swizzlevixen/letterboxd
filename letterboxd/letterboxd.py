"""
Python 3 wrapper for
Version 0 of the Letterboxd API
"""

# import api
# import service/auth
# import service/comments
# import service/contributors
from .services.film import Film
# import service/lists
# import service/log_entries
# import service/me
# import service/members
# import service/search


LBX_API_SECRET = os.environ.get('LBX_API_SECRET', None)
API_BASE_URL = "https://api.letterboxd.com/api/v0"

class Letterboxd(object):
    def __init__(self, api_base, api_key, api_secret):
        self.api_base = api_base
        self.api_key = api_key
        self.api_secret = api_secret
