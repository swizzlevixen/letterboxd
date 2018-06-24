# Letterboxd

`v0.1.0a`

**THE CODE IS CURRENTLY IN AN ALPHA STATE, AND MAY BE VERY BROKEN, AND/OR WHAT IS WORKING NOW MAY BREAK IN THE FUTURE.**

A Python 3 implementation of the [Letterboxd API v0](http://api-docs.letterboxd.com/). Python 3.6+ is required, because this uses formatted strings.
 
Currently a ***WORK-IN-PROGRESS,*** focusing first on retrieving watchlists and other lists.

Letterboxd has posted an [example ruby client](https://github.com/grantyb/letterboxd-api-example-ruby-client), but as they say in the readme there:

> Although the Letterboxd API isn’t public yet (as at 2017-06-12), we have seeded some developers with API keys.

If you need more information about API access, please see https://letterboxd.com/api-coming-soon/

## API Coverage

The library currently covers these Letterboxd API endpoints:

#### Film

- /film/{id}
- /film/{id}/availability — this does not seem to return any data at this time
- /film/{id}/me

#### Me

- /me

#### Member

- /member/{id}/watchlist

## Contributions

Code files should be passed through the [Black](https://github.com/ambv/black) Python code formatter before check-in.

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
