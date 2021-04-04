#! /usr/bin/env python3
"""
Letterboxd API definitions for testing
"""

from _pytest.fixtures import fixture

# -------------------------
# Film-collection
# -------------------------


@fixture
def film_collection_keys():
    # FilmCollection definition
    return ["id", "name", "films", "links"]


# -------------------------
# Film
# -------------------------


@fixture
def film_keys():
    """
    Film definition

    Optional keys: "originalName", "alternativeNames"
    """
    return [
        "id",
        "name",
        "releaseYear",
        "tagline",
        "description",
        "runTime",
        "poster",
        "backdrop",
        "backdropFocalPoint",
        "trailer",
        "genres",
        "contributions",
        "filmCollectionId",
        "links",
    ]


@fixture
def film_availability_response_keys():
    """FilmAvailabilityResponse definition"""
    return ["FilmAvailability"]


@fixture
def film_availability_keys():
    """
    FilmAvailability definition

    Optional keys: "id"
    """
    return ["service", "displayName", "country", "url"]


@fixture
def film_relationship_keys():
    """
    FilmRelationship definition

    Optional keys: "whenWatched", "whenLiked", "whenAddedToWatchlist",
        "whenCompletedInWatchlist", "rating"
    """
    return ["watched", "liked", "favorited", "inWatchlist", "reviews", "diaryEntries"]


@fixture
def film_relationship_update_response_keys():
    """FilmRelationshipUpdateResponse definition"""
    return ["data", "messages"]


@fixture
def member_film_relationships_response_keys():
    """
    MemberFilmRelationshipsResponse definition

    Optional keys: "next"
    """
    return ["items"]


@fixture
def member_film_relationship_keys():
    """MemberFilmRelationship definition"""
    return ["member", "relationship"]


@fixture
def member_summary_keys():
    """
    MemberSummary definition

    Optional keys:  "givenName", "familyName"
    """
    return [
        "id",
        "username",
        "displayName",
        "shortName",
        "pronoun",
        "avatar",
        "memberStatus",
    ]


@fixture
def film_statistics_keys():
    """
    FilmStatistics definition

    Optional keys: "rating" (I suspect "ratingsHistogram" might be?)
    """
    return ["film", "counts", "ratingsHistogram"]


@fixture
def film_summary_keys():
    """
    FilmSummary definition

    Optional keys: "originalName", "alternativeNames", "filmCollectionId",
        "releaseYear", "poster",
    """
    return ["id", "name", "directors", "links", "relationships"]


# -------------------------
# Films
# -------------------------


@fixture
def films_response_keys():
    """
    FilmsResponse definition

    Optional key: "next"
    """
    return ["items"]


@fixture
def film_services_response_keys():
    """FilmServicesResponse definition"""
    return ["items"]


@fixture
def service_keys():
    """Service definition"""
    return ["id", "name"]


@fixture
def genres_response_keys():
    """GenresResponse definition"""
    return ["items"]


@fixture
def genre_keys():
    """Genre definition"""
    return ["id", "name"]


@fixture
def link_keys():
    """Link definition"""
    return ["type", "id", "url"]


# -------------------------
# User (/me)
# -------------------------


@fixture
def member_settings_update_response_keys():
    """
    MemberSettingsUpdateResponse definition
    """
    return ["data", "messages"]


@fixture
def search_response_keys():
    return ["next", "items"]


@fixture
def abstract_search_item_keys():
    return ["type", "score"]


# -------------------------
# List
# -------------------------


@fixture
def list_keys():
    """
    Keys definition

    Optional keys: "canShareOn", "sharedOn", "descriptionLbml", "description",
    """
    return [
        "id",
        "name",
        "filmCount",
        "published",
        "ranked",
        "hasEntriesWithNotes",
        "tags2",
        "whenCreated",
        "whenPublished",
        "owner",
        "previewEntries",
        "links",
    ]


@fixture
def list_update_response_keys():
    """
    ListUpdateResponse definition
    """
    return ["data", "messages"]


@fixture
def list_comments_response_keys():
    """
    ListCommentsResponse definition

    Optional key: "next"
    """
    return ["items"]


@fixture
def list_comment_keys():
    """
    ListComment definition

    Optional keys:
    """
    return [
        "id",
        "member",
        "whenCreated",
        "whenUpdated",
        "commentLbml",
        "removedByAdmin",
        "deleted",
        "blocked",
        "blockedByOwner",
        "list",
        "comment",
    ]


@fixture
def list_entries_response_keys():
    """
    ListEntriesResponse definition

    Optional keys: "next"
    """
    return ["items", "metadata", "relationships"]


@fixture
def list_relationship_keys():
    """
    ListRelationship definition
    """
    return ["liked", "subscribed", "subscriptionState", "commentThreadState"]


@fixture
def list_relationship_update_response_keys():
    """
    ListRelationshipUpdateResponse definition
    """
    return ["data", "messages"]


@fixture
def list_statistics_keys():
    """ListStatistics definition"""
    return ["list", "counts"]


# -------------------------
# Lists
# -------------------------


@fixture
def lists_response_keys():
    return ["next", "items"]


@fixture
def list_summary_keys():
    """
    ListSummary definition

    Optional keys: "descriptionLbml", "descriptionTruncated", "clonedFrom",
        "description",
    """
    return ["id", "name", "filmCount", "published", "ranked", "owner", "previewEntries"]

@fixture
def list_create_response_keys():
    """Returns list of keys in ListCreateResponse"""
    return ["data", "messages"]

# -------------------------
# Log-Entries / Log-entry
# -------------------------

@fixture
def log_entries_response_keys():
    """Returns list of keys in LogEntriesResponse
    Optional keys: "next" - cursor
    """
    return ["items"]

@fixture
def log_entry_keys():
    """Returns list of keys in LogEntry"""
    return ["id", "name", "owner", "film", "diaryDetails", "review", "tags", "tags2", "whenCreated", "whenUpdated", "like", "commentable", "links"]

@fixture
def review_update_response_keys():
    """Returns list of keys in ReviewUpdateResponse"""
    return ["data", "messages"]

@fixture
def review_comments_response_keys():
    """Returns list of keys in ReviewCommentsResponse
    Optional keys: "next" - cursor
    """
    return ["items"]

@fixture
def review_comment_keys():
    """Returns list of keys in ReviewComment"""
    return ["id", "member", "whenCreated", "whenUpdated", "commentLbml", "removedByAdmin", "removedByContentOwner", "deleted", "blocked", "blockedByOwner", "editableWindowExpiresIn", "review", "comment"]

@fixture
def review_relationship_keys():
    """Returns list of keys in ReviewRelationship"""
    return ["liked", "subscribed", "subscriptionState", "commentThreadState"]

@fixture
def review_relationship_update_response_keys():
    """Returns list of keys in ReviewRelationshipUpdateResponse"""
    return ["data", "messages"]

@fixture
def review_statistics_keys():
    """Returns list of keys in ReviewStatistics"""
    return ["logEntry", "counts"]

# -------------------------
# Comment
# -------------------------

@fixture
def comment_update_response_keys():
    """Returns list of keys in CommentUpdateResponse"""
    return ["data", "messages"]



