import json
from .letterboxd.letterboxd import Letterboxd
import helpers


API_KEY = 'YOUR_KEY_HERE'
API_SECRET = 'YOUR_SECRET_HERE'

API_BASE = 'https://api.letterboxd.com/api/v0'

lbxd = Letterboxd.new API_BASE, API_KEY, API_SECRET

lbxd.login 'YOUR_USERNAME_HERE', 'YOUR_PASSWORD_HERE'
helpers.show_json(lbxd.get_me)