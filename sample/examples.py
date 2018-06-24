import os
import pprint
import sys

# Add the relative directory containing the letterboxd module to the Python path
lbxd_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lbxd_path)

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
    prettyprinter = pprint.PrettyPrinter(indent=4)

    # Assuming use of environment variables:
    lbxd = Letterboxd()
    # If not using environment variables, instead instantiate Letterboxd() with your secrets:
    # lbxd = Letterboxd(api_key='YOUR_KEY_HERE', api_secret='YOUR_SECRET_HERE')

    # Login user
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    test_user = lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    # If not using environment variables, instead instantiate Letterboxd() with your credentials
    # test_user = lbxd.user(YOUR_USERNAME_HERE, YOUR_PASSWORD_HERE)

    # request /me endpoint
    me_dict = test_user.me
    # print it pretty
    print("\n-------------------------\n/me\n-------------------------\n")
    prettyprinter.pprint(me_dict)

    # request /film/{id} endpoint
    film = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    response = film.info()
    response_json = response.json()
    print("\n-------------------------\nfilm/{id}\n-------------------------\n")
    prettyprinter.pprint(response_json)

    # request /film/{id}/me endpoint,
    film_instance = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    response = film_instance.me()
    response_json = response.json()
    print("\n-------------------------\nfilm/{id}/me\n-------------------------\n")
    prettyprinter.pprint(response_json)
