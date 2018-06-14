import json
from .letterboxd.letterboxd import Letterboxd
import helpers

# Assuming use of environment variables:
lbxd = Letterboxd()

# If not using environment variables, instead instantiate Letterboxd() with your secrets:
# API_KEY = 'YOUR_KEY_HERE'
# API_SECRET = 'YOUR_SECRET_HERE'
# lbxd = Letterboxd(api_key=API_KEY, api_secret=API_SECRET)

# FIXME: ruby implementation
# lbxd.login 'YOUR_USERNAME_HERE', 'YOUR_PASSWORD_HERE'
# helpers.show_json(lbxd.get_me)