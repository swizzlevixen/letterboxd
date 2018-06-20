"""
Film(s) services for the Letterboxd API

/films endpoints documentation
http://api-docs.letterboxd.com/#path--films

/film endpoints documentation
http://api-docs.letterboxd.com/#path--film--id-
"""
import logging


class Film(object):
    def __init__(self, film_id, api):
        self.__api = api
        self.__film_id = film_id

    # /film/{id}
    def info(self):
        return self.__api.api_call(path="film/{}".format(self.__film_id))
