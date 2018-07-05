=====
Usage
=====

To use Letterboxd in a project:

.. code-block:: python

    import letterboxd
    lbxd = letterboxd.new()

You can pass the ``api_base`` URL for the API, your ``api_key``, and your ``api_secret`` as arguments in ``.new()``, or add it to your environment variables as:

.. code-block:: bash

    export LBXD_API_KEY="YOUR_KEY_HERE"
    export LBXD_API_SECRET="YOUR_SECRET_HERE"

If you do not provide an ``api_base``, it currently defaults to ``https://api.letterboxd.com/api/v0``.

For testing, you can also add environment variables for an account user name and password, and the location of your `Charles proxy SSL certificate <https://www.charlesproxy.com/documentation/using-charles/ssl-certificates/>`_.

.. code-block:: bash

    export LBXD_USERNAME="YOUR_USERNAME"
    export LBXD_PASSWORD="YOUR_PASSWORD"
    export CHARLES_CERTIFICATE="/path/to/charles-ssl-proxying-certificate.pem"

Set the ``CHARLES`` environment variable to ``True`` to turn the proxy settings on. For example, if you want to use it on a case-by-case basis for testing, run the tests like this:

.. code-block:: bash

    $ CHARLES="True" pytest

Please see `Modules <modules.html>`_ for more details on usage of the classes.
