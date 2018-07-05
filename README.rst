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

Documentation
-------------

Documentation is written in the ``/docs`` folder, and being generated for `human-readable documentation on Read the Docs <https://letterboxd.readthedocs.io>`_.

At the moment, most of the docs are generated automatically from the code’s docstrings. More human documentation will come as we approach v1.0.
