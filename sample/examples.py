import os
import pprint
import sys

# Add the directory containing the letterboxd module to the Python path
lbxd_path = "../"
sys.path.append(os.path.abspath(lbxd_path))

from letterboxd.letterboxd import Letterboxd


def load_user_pass():
    """
    Loads the username and password from the environment
    :return: tuple - [username, password]
    """
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
    return (LBXD_USERNAME, LBXD_PASSWORD)


if __name__ == "__main__":
    # Assuming use of environment variables:
    lbxd = Letterboxd()

    # If not using environment variables, instead instantiate Letterboxd() with your secrets:
    # API_KEY = 'YOUR_KEY_HERE'
    # API_SECRET = 'YOUR_SECRET_HERE'
    # lbxd = Letterboxd(api_key=API_KEY, api_secret=API_SECRET)

    # make login
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    # request from the API endpoint /me
    me_dict = test_user.me()
    # print it pretty
    prettyprinter = pprint.PrettyPrinter(indent=4)
    prettyprinter.pprint(me_dict)
