"""
/file endpoints
"""

from letterboxd.api import API

class Film(object):
    def __init__(self, id):
        self.id = id

    # /film/{id}
    def info(self):
        API.api(self, path='film/{}'.format(self.id))
