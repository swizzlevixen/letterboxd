import logging
from letterboxd.config import *
from letterboxd.letterboxd import Letterboxd

logging.getLogger(__name__).addHandler(logging.NullHandler())

name = "letterboxd"


def new(api_base=API_BASE_URL, api_key="", api_secret=""):
    lbxd = Letterboxd(api_base=api_base, api_key=api_key, api_secret=api_secret)
    return lbxd
