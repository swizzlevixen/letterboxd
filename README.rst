.. Semaphore Build Status
.. image:: https://semaphoreci.com/api/v1/bobtiki/letterboxd/branches/master/badge.svg
   :target: https://semaphoreci.com/bobtiki/letterboxd

.. Travis CI build status
.. image:: https://travis-ci.org/bobtiki/letterboxd.svg?branch=master
   :target: https://travis-ci.org/bobtiki/letterboxd

.. ReadTheDocs document status
.. image:: https://readthedocs.org/projects/letterboxd/badge/?version=latest
   :target: https://letterboxd.readthedocs.io/en/latest/?badge=latest

Letterboxd
==========

Python 3 implementation of the `Letterboxd API v0 <http://api-docs.letterboxd.com/>`_.

* PyPI package: https://pypi.org/project/letterboxd/
* GitHub repo: https://github.com/bobtiki/letterboxd
* Documentation: https://letterboxd.readthedocs.io
* Free software: MIT license

Python ≥3.6 is required.

.. warning::

    **THIS PROJECT IS CURRENTLY IN ALPHA:**

    - It may be broken.
    - What is working now may break between now and v1.0
    - Initial focus is on implementing endpoints related to retrieving watchlists and other lists for users.

Letterboxd API Access
---------------------

Letterboxd has posted an `example Ruby client <https://github.com/grantyb/letterboxd-api-example-ruby-client>`_, but as they say in the readme there:

    Although the Letterboxd API isn’t public yet (as at 2017-06-12), we have seeded some developers with API keys.

If you need more information about API access, please see `<https://letterboxd.com/api-coming-soon/>`_.

Acknowledgements
----------------

Thanks to Kevin Ndung'u Gathuku of Semaphore for `this article on writing and testing an API wrapper <https://semaphoreci.com/community/tutorials/building-and-testing-an-api-wrapper-in-python>`_ from which I learned many of the techniques I used to build this wrapper.

And of course, many thanks to Matthew Buchanan and Grant Berridge at `Letterboxd <https://letterboxd.com>`_ for allowing me beta access to the Letterboxd API, and providing helpful assistance when I stumbled.