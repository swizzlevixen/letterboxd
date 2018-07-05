Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[Unreleased]
------------

Added
.....

- This ``CHANGELOG.markdown``
- Documentation written with reStructuredText and Sphinx, being built to `Read the Docs <https://letterboxd.readthedocs.io/>`_
- Added a number of files/tests provided as defaults in `cookiecutter-pypackage <https://github.com/audreyr/cookiecutter-pypackage>`_
- Added an easy initializer with ``import letterboxd`` and then ``letterboxd.new()``
- ``User.refresh_token()`` to refresh the user authentication oAuth token
- Coverage for Letterboxd API endpoints:
    - /film/{id}/members
    - /film/{id}/report
    - /film/{id}/statistics
    - /films
    - /films/film-services
    - /films/genres
    - /film-collection/{id}
    - /search

Changed
.......

- All api-calling methods now return the dictionary from the response JSON, instead of the entire ``requests.Response``.

[0.1.0] - 2018-06-24
--------------------
Added
.....

- First public version! Version 0.1.0a `tagged on GitHub <https://github.com/bobtiki/letterboxd/releases/tag/v0.1.0a>`_, and `posted to PyPI <https://pypi.org/project/letterboxd/>`_.
- letterboxd, api, user, auth, member, and film modules.
- coverage for Letterboxd API endpoints:
    - film
    - /film/{id}
    - /film/{id}/availability — this data is first-party only
    - /film/{id}/me
    - /me
    - /member/{id}/watchlist

Changelog format
----------------

- Each version should:
    - List its release date in ISO 8601 format (YYYY-MM-DD).
    - Group changes to describe their impact on the project, as follows:
        - ``Added`` for new features.
        - ``Changed`` for changes in existing functionality.
        - ``Deprecated`` for once-stable features removed in upcoming releases.
        - ``Removed`` for deprecated features removed in this release.
        - ``Fixed`` for any bug fixes.
        - ``Security`` to invite users to upgrade in case of vulnerabilities.
    - Take a look at `this checklist for packaging a new version <http://www.sherifsoliman.com/2016/09/30/Python-package-with-GitHub-PyPI/>`_, and `this one <https://cookiecutter-pypackage.readthedocs.io/en/latest/pypi_release_checklist.html>`_