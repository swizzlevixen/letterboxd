# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added

- This `CHANGELOG.markdown`
- Documentation written with reStructuredText and Sphinx, being built to [Read the Docs](https://letterboxd.readthedocs.io/)

## [0.1.0] - 2018-06-24
### Added

- First public version! Version 0.1.0a [tagged on GitHub](https://github.com/bobtiki/letterboxd/releases/tag/v0.1.0a), and [posted to PyPI](https://pypi.org/project/letterboxd/).
- letterboxd, api, user, auth, member, and film modules.
- coverage for Letterboxd API endpoints:
    - film
    - /film/{id}
    - /film/{id}/availability — this data is first-party only
    - /film/{id}/me
    - /me
    - /member/{id}/watchlist

## Changelog format

- Each version should:
    - List its release date in ISO 8601 format (YYYY-MM-DD).
    - Group changes to describe their impact on the project, as follows:
        - `Added` for new features.
        - `Changed` for changes in existing functionality.
        - `Deprecated` for once-stable features removed in upcoming releases.
        - `Removed` for deprecated features removed in this release.
        - `Fixed` for any bug fixes.
        - `Security` to invite users to upgrade in case of vulnerabilities.