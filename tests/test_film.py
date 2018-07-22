#! /usr/bin/env python3
import logging

import letterboxd
from letterboxd.letterboxd import Letterboxd
from letterboxd.services.film import Film
from tests.letterboxd_definitions import *
from tests.test_letterboxd import load_user_pass

logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


# -------------------------
# Film
# -------------------------


def test_film_details():
    """Tests API call to get a film's details"""

    # Assume use of environment variables for api key and secret
    lbxd = Letterboxd()
    film_instance = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    assert isinstance(film_instance, Film)
    film = film_instance.details()
    logging.debug(f"film: {film}")
    assert isinstance(film, dict)
    assert film["id"] == "2bbs", "The ID should be in the response"
    assert set(film_keys()).issubset(film.keys()), "All keys should be in Film"


def test_film_availability():
    # This data is first-party only, so it doesn't return any data for normal users
    lbxd = Letterboxd()
    film_instance = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    film_availability_response = film_instance.availability()
    logging.debug(f"film_availability_response: {film_availability_response}")
    assert isinstance(film_availability_response, dict)
    # If we were to get a response, this would be the test:
    # assert set(film_availability_response_keys()).issubset(
    #     film_availability_response.keys()
    # ), "All keys should be in FilmAvailabilityResponse"
    # film_availability = film_availability_response[0]
    # assert set(film_availability_response()).issubset(
    #     film_availability.keys()
    # ), "All keys should be in FilmAvailability"


def test_film_me():
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    # login
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    film_instance = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    film_relationship = film_instance.me()
    logging.debug(f"film_relationship 1: {film_relationship}")
    assert isinstance(film_relationship, dict)
    assert set(film_relationship_keys()).issubset(
        film_relationship.keys()
    ), "All keys should be in FilmRelationship, against film with relationship"

    # test against film with no relationships
    film_instance = lbxd.film(film_id="Xwa")  # Shark Attack 2
    film_relationship = film_instance.me()
    logging.debug(f"film_relationship 2: {film_relationship}")
    assert set(film_relationship_keys()).issubset(
        film_relationship.keys()
    ), "All keys should be in FilmRelationship, against film with no relationship"


def test_film_patch_me():
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    # login
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    # Test the film with a movie this user hasn't seen, and isn't likely to ever see.
    film_instance = lbxd.film(film_id="1HIc")  # Shark Attack 3: Megalodon
    # Add it to my watchlist
    film_relationship_update_request = {"inWatchlist": True}
    film_relationship_update_response = film_instance.me_update(
        film_relationship_update_request=film_relationship_update_request
    )
    logging.debug(
        f"film_relationship_update_response: {film_relationship_update_response}"
    )
    assert isinstance(film_relationship_update_response, dict)
    assert set(film_relationship_update_response_keys()).issubset(
        film_relationship_update_response.keys()
    ), "All keys should be in FilmRelationshipUpdateResponse"
    assert isinstance(film_relationship_update_response["data"], dict)
    film_relationship = film_relationship_update_response["data"]
    assert set(film_relationship_keys()).issubset(
        film_relationship.keys()
    ), "All keys should be in FilmRelationship"
    assert isinstance(film_relationship_update_response["messages"], list)

    # Mark it watched, liked, and rate it
    film_relationship_update_request = {"watched": True, "liked": True, "rating": 2.5}
    film_relationship_update_response = film_instance.me_update(
        film_relationship_update_request=film_relationship_update_request
    )
    logging.debug(
        f"film_relationship_update_response: {film_relationship_update_response}"
    )
    assert isinstance(film_relationship_update_response, dict)

    # Remove activity and reset rating
    film_relationship_update_request = {
        "watched": False,
        "liked": False,
        "inWatchlist": False,
        "rating": "null",  # I had this as Null, but my params cleaner was stripping it out.
    }
    film_relationship_update_response = film_instance.me_update(
        film_relationship_update_request=film_relationship_update_request
    )
    logging.debug(
        f"film_relationship_update_response: {film_relationship_update_response}"
    )
    assert isinstance(film_relationship_update_response, dict)


def test_film_members():
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    # login
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    film_instance = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    member_film_relationships_request = {
        "perPage": 100,
        "sort": "Name",
        "member": "11Ht",
        "memberRelationship": "IsFollowedBy",
        "filmRelationship": "Liked",
    }
    member_film_relationships_response = film_instance.members(
        member_film_relationships_request=member_film_relationships_request
    )
    logging.debug(
        f"member_film_relationships_response: {member_film_relationships_response}"
    )
    logging.debug(
        f"member_film_relationships_response.keys(): {member_film_relationships_response.keys()}"
    )
    assert isinstance(member_film_relationships_response, dict)
    assert set(member_film_relationships_response_keys()).issubset(
        member_film_relationships_response.keys()
    ), "All keys should be in MemberFilmRelationshipsResponse"
    assert isinstance(member_film_relationships_response["items"], list)
    member_film_relationship = member_film_relationships_response["items"][0]
    logging.debug(f"member_film_relationship: {member_film_relationship}")
    assert isinstance(member_film_relationship["member"], dict)
    member_summary = member_film_relationship["member"]
    logging.debug(f"member_summary: {member_summary}")
    assert set(member_summary_keys()).issubset(
        member_summary.keys()
    ), "All keys should be in MemberSummary"
    assert isinstance(member_film_relationship["relationship"], dict)
    film_relationship = member_film_relationship["relationship"]
    logging.debug(f"film_relationship: {film_relationship}")
    assert set(film_relationship_keys()).issubset(
        film_relationship.keys()
    ), "All keys should be in FilmRelationship"


def test_film_report():
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd = Letterboxd()
    # login, even though we don't use this value
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    film_instance = lbxd.film(film_id="9mMS")  # Kirk Cameron’s Saving Christmas
    report_film_request = {"reason": "Other", "message": "TEST — IGNORE"}
    success = film_instance.report(
        film_id="9mMS", report_film_request=report_film_request
    )
    logging.debug(f"success: {success}")
    assert success is True


def test_film_statistics():
    """Tests API call to get a film's statistics"""

    # Assume use of environment variables for api key and secret
    lbxd = Letterboxd()
    film_instance = lbxd.film(film_id="2bbs")  # Raiders of the Lost Ark
    assert isinstance(film_instance, Film)
    film_statistics = film_instance.statistics()
    logging.debug(f"film_statistics: {film_statistics}")
    assert isinstance(film_statistics, dict)
    assert set(film_statistics_keys()).issubset(
        film_statistics.keys()
    ), "All keys should be in FilmStatistics"
    assert film_statistics["film"]["id"] == "2bbs", "The ID should be in the response"


def test_films():
    """
    Test API call to /films
    """
    lbxd = Letterboxd()
    films_request = {
        "perPage": 25,
        "sort": "ReleaseDateEarliestFirst",
        # "filmId": ["2bbs", "imdb:tt0087469", "tmdb:89"],
        # "genre": "9a",  # Science Fiction
        # "decade": 1980,
        # "year": 1989,
        # "service": "amazon",  # Amazon
        # "where": ["NotReleased", "InWatchlist"],
        "member": "3P",
        "memberRelationship": "Favorited",
        "includeFriends": "All",
        # "tagCode": "stubs",
        # "tagger": "11Ht",
        # "includeTaggerFriends": "Only",
    }
    films = lbxd.films()
    films_response = films.films(films_request=films_request)
    logging.debug(f"films_response: {films_response}")
    assert isinstance(films_response, dict)
    assert set(films_response_keys()).issubset(
        films_response.keys()
    ), "All keys should be in FilmsResponse"
    # Debug print a simple list of the movies
    film_num = 1
    for film in films_response["items"]:
        logging.debug(f"{film_num}. {film['name']}")
        film_num += 1


def test_films_services():
    """
    Test API call to /films/film-services
    """
    lbxd = Letterboxd()
    # login, so that we can see all of the services available to this member
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    films = lbxd.films()
    film_services_response = films.services()
    logging.debug(f"film_services_response: {film_services_response}")
    assert isinstance(film_services_response, dict)
    assert set(film_services_response_keys()).issubset(
        film_services_response.keys()
    ), "All keys should be in FilmServicesResponse"
    assert isinstance(film_services_response["items"], list)
    service = film_services_response["items"][0]
    assert set(service_keys()).issubset(service.keys()), "All keys should be in Service"


def test_films_genres():
    """
    Test API call to /films/genres
    """
    lbxd = Letterboxd()
    films = lbxd.films()
    genres_response = films.genres()
    logging.debug(f"genres_response: {genres_response}")
    assert isinstance(genres_response, dict)
    assert set(genres_response_keys()).issubset(
        genres_response.keys()
    ), "All keys should be in GenresResponse"
    genre = genres_response["items"][0]
    logging.debug(f"genre: {genre}")
    assert set(genre_keys()).issubset(genre.keys()), "All keys should be in the Genre"


def test_film_collection():
    """
    Test API call to /film-collection/{id}
    """
    lbxd = letterboxd.new()
    # Log in as a user
    LBXD_USERNAME, LBXD_PASSWORD = load_user_pass()
    lbxd.user(LBXD_USERNAME, LBXD_PASSWORD)
    film_collection_id = "Nb"  # Indiana Jones
    film_collection_request = {
        "sort": "ReleaseDateEarliestFirst",
        "genre": "9k",
        "decade": 1980,
        "year": 1989,
        "service": "amazon",
        "where": ["Released"],
        "member": "3P",
        "memberRelationship": "Watched",
        "includeFriends": "Only",
        "tagCode": "stubs",
        "tagger": "11Ht",
        "includeTaggerFriends": "All",
    }
    film_collection = lbxd.film_collection(
        film_collection_id=film_collection_id,
        film_collection_request=film_collection_request,
    )
    film_summary = film_collection["films"][0]
    logging.debug(f"film_summary: {film_summary}")
    assert isinstance(film_summary, dict)
    assert set(film_summary_keys()).issubset(
        film_summary.keys()
    ), "All keys should be in FilmSummary"
    link = film_collection["links"][0]
    logging.debug(f"link: {link}")
    assert isinstance(link, dict)
    assert set(link_keys()).issubset(link.keys()), "All keys should be in Link"
