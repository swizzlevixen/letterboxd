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

**THIS PROJECT IS CURRENTLY IN ALPHA:**

- **IT MAY BE BROKEN**
- **WHAT IS WORKING NOW MAY BREAK IN THE FUTURE**
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

Usage
-----

Instantiate the ``Letterboxd`` class, and provide it with the ``api_base`` URL for the API, your ``api_key``, and your ``api_secret``. You can pass it as a variable to the class initializer, or add it to your environment variables as:

.. code-block:: bash
   :linenos:

    export LBXD_API_KEY="YOUR_KEY_HERE"
    export LBXD_API_SECRET="YOUR_SECRET_HERE"

If you do not provide an `api_base`, it currently defaults to `https://api.letterboxd.com/api/v0`.

For testing, you can also add environment variables for an account user name and password, and the location of your [Charles proxy SSL certificate](https://www.charlesproxy.com/documentation/using-charles/ssl-certificates/).

```
export LBXD_USERNAME="YOUR_USERNAME"
export LBXD_PASSWORD="YOUR_PASSWORD"
export CHARLES_CERTIFICATE="/path/to/charles-ssl-proxying-certificate.pem"
```

Set the `CHARLES` environment variable to `True` to turn the proxy settings on. For example, if you want to use it on a case-by-case basis for testing, run the tests like this:

```
$ CHARLES="True" py.test
```

Please see [Read the Docs](https://letterboxd.readthedocs.io) for more details on usage of the library classes.
