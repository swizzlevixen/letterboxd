from letterboxd.letterboxd import Letterboxd

# Assuming use of environment variables:
lbxd = Letterboxd()

# If not using environment variables, instead instantiate Letterboxd() with your secrets:
# API_KEY = 'YOUR_KEY_HERE'
# API_SECRET = 'YOUR_SECRET_HERE'
# lbxd = Letterboxd(api_key=API_KEY, api_secret=API_SECRET)


# try to get the username from environment variable
LBXD_USERNAME = os.environ.get("LBXD_USERNAME", None)


class UsernameMissingError(Exception):
    pass


if LBXD_USERNAME is None:
    raise UsernameMissingError("Auth methods require a Letterboxd username.")

# try to get the user password from environment variable
LBXD_PASSWORD = os.environ.get("LBXD_PASSWORD", None)


class PasswordMissingError(Exception):
    pass


if LBXD_PASSWORD is None:
    raise PasswordMissingError("Auth methods require a Letterboxd password.")

lbxd = Letterboxd()
# make login
test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
test_token = test_user.token()
test_user.get_me


# FIXME: ruby implementation
# lbxd.login 'YOUR_USERNAME_HERE', 'YOUR_PASSWORD_HERE'
# helpers.show_json(lbxd.get_me)
