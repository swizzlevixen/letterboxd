from pytest import fixture
from letterboxd.services.film import Film
import vcr

@fixture
def film_keys():
    # Responsible only for returning the test data
    return ['id', 'name', 'originalName', 'alternativeNames',
            'releaseYear', 'tagline', 'description', 'runTime',
            'poster', 'backdrop', 'backdropFocalPoint', 'trailer',
            'genres', 'contributions', 'filmCollectionId', 'links']

@vcr.use_cassette('tests/vcr_cassettes/film_info.yml')
def test_film_info(film_keys):
    """Tests API call to get a film's info"""

    film_instance = Film("raiders-of-the-lost-ark")
    response = film_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == "raiders-of-the-lost-ark", "The ID should be in the response"
    assert set(film_keys).issubset(response.keys()), "All keys should be in the response"
