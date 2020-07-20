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

- pytests for the new endpoints

## Changed



