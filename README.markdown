# Letterboxd

`v0.2.0a0`

A Python 3 implementation of the [Letterboxd API v0](http://api-docs.letterboxd.com/).

Python 3.6+ is required, because this library uses formatted strings, among other modern niceties.

**THE CODE IS CURRENTLY IN AN ALPHA STATE, AND MAY BE VERY BROKEN, AND/OR WHAT IS WORKING NOW MAY BREAK IN THE FUTURE.**
 
Currently a ***WORK-IN-PROGRESS,*** focusing first on retrieving watchlists and other lists for users.

## Letterboxd API Access

Letterboxd has posted an [example ruby client](https://github.com/grantyb/letterboxd-api-example-ruby-client), but as they say in the readme there:

> Although the Letterboxd API isn’t public yet (as at 2017-06-12), we have seeded some developers with API keys.

If you need more information about API access, please see [https://letterboxd.com/api-coming-soon/]().

## Documentation

Documentation is written in the `/docs` folder, and being generated for [human-readable documentation on Read the Docs](https://letterboxd.readthedocs.io).

At the moment, most of the docs are generated automatically from the code’s docstrings. More human documentation will come as we approach v1.0.

## Usage

Instantiate the `Letterboxd` class, and provide it with the `api_base` URL for the API, your `api_key`, and your `api_secret`. You can pass it as a variable to the class initializer, or add it to your environment variables as:

```
export LBXD_API_KEY="YOUR_KEY_HERE"
export LBXD_API_SECRET="YOUR_SECRET_HERE"
```

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