"""
/file endpoints
"""
import logging

class Film(object):
    def __init__(self, film_id, api):
        self.__api = api
        self.__film_id = film_id

    # /film/{id}
    def info(self):
        return self.__api.api_call(path = 'film/{}'.format(self.__film_id))
