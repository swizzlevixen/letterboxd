from pytest import fixture
from letterboxd.letterboxd import Letterboxd
import logging
import requests

logging.getLogger(__name__)
# FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
# logging.basicConfig(format=FORMAT, level = logging.DEBUG)
logging.basicConfig(level = logging.DEBUG)

@fixture
def film_keys():
    # Responsible only for returning the test data
    # A film could also include 'originalName', but does not apply here
    return ['id', 'name', 'alternativeNames',
            'releaseYear', 'tagline', 'description', 'runTime',
            'poster', 'backdrop', 'backdropFocalPoint', 'trailer',
            'genres', 'contributions', 'filmCollectionId', 'links']


def test_film_info():
    """Tests API call to get a film's info"""

    # Assume use of environment variables for api key and secret
    lbxd = Letterboxd()

    film_instance = lbxd.film(film_id = "2bbs")  # Raiders of the Lost Ark
    response = film_instance.info()
    logging.debug("response: {}".format(response))
    assert isinstance(response, requests.Response)
    assert response.status_code == 200

    response_json = response.json()
    logging.debug("response_json: {}".format(response_json))
    assert isinstance(response_json, dict)
    assert response_json['id'] == "2bbs", "The ID should be in the response"
    assert set(film_keys()).issubset(response_json.keys()), "All keys should be in the response"
