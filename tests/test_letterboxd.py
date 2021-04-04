import logging
import os

from pytest import fixture

from letterboxd.letterboxd import Letterboxd
from tests.letterboxd_definitions import *

logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def test_letterboxd():
    lbxd = Letterboxd()
    assert isinstance(lbxd, Letterboxd)


# -------------------------
# Letterboxd API Definitions
# -------------------------

@fixture
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
