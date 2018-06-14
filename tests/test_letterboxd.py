from pytest import fixture
from letterboxd.letterboxd import Letterboxd
import vcr

@fixture
def film_keys():
    # Responsible only for returning the test data
    return ['id', 'name', 'originalName', 'alternativeNames',
            'releaseYear', 'tagline', 'description', 'runTime',
            'poster', 'backdrop', 'backdropFocalPoint', 'trailer',
            'genres', 'contributions', 'filmCollectionId', 'links']

# @vcr.use_cassette('tests/vcr_cassettes/film_info.yml')
# def test_film_info(film_keys):
#     """Tests API call to get a film's info"""
#
#     lbxd = Letterboxd()
#
#     film_instance = Film("raiders-of-the-lost-ark")
#     response = film_instance.info()
#
#     assert isinstance(response, dict)
#     assert response['id'] == "raiders-of-the-lost-ark", "The ID should be in the response"
#     assert set(film_keys).issubset(response.keys()), "All keys should be in the response"

@vcr.use_cassette('tests/vcr_cassettes/movie-info.yml', filter_query_parameters=['api_key'])
def test_film_info():
    """Tests API call to get a film's info"""

    lbxd = Letterboxd(API_BASE, API_KEY, API_SECRET)

    film_instance = Film("raiders-of-the-lost-ark")
    response = film_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == "raiders-of-the-lost-ark", "The ID should be in the response"
    assert set(film_keys).issubset(response.keys()), "All keys should be in the response"
