## Description

- Added the /log-entry and /log-entries endpoints which allows the user to add entries(diaries/reviews) to their log.
- Added the /comment endpoint which allows the user to edit and delete comments made from other endpoints.

## Changelog
### Added

- /log-entries (http://api-docs.letterboxd.com/#path--log-entries)
    - /log-entries
    - /log-entry/{id}
    - /log-entry/{id}/comments
    - /log-entry/{id}/me
    - /log-entry/{id}/report
    - /log-entry/{id}/statistics

- /comments (http://api-docs.letterboxd.com/#path--comment--id-)
    - /comment/{id}
    - /comment/{id}/report

- Tests for the new endpoints

## Fixes
Updated old tests because they directly called fixtures. That feature was deprecated in pytest v4.0 and caused the tests to fail on pytest 5.2. 
They are now passed as parameters to the tests they are relevant to and the tests pass.
Relevant link (https://docs.pytest.org/en/latest/deprecations.html#calling-fixtures-directly)



