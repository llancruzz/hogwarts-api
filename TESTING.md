# API Testing

## Table of Contents

- [Automated Testing](#automated-testing)
- [Manual Testing](#manual-testing)
  - [Endpoint Testing](#endpoint-testing)
  - [CRUD Functionality Testing](#crud-functionality-testing)
    - [Comments App](#comments-app)
    - [Contacts App](#contacts-app)
    - [Followers App](#followers-app)
    - [Likes App](#likes-app)
    - [Posts App](#posts-app)
    - [Profiles App](#profiles-app)


## Automated Testing

Automated tests were created for the Comments, Contacts, Followers, Likes and Posts applications.


### Links to tests create can be found below:

- [Comments - View Tests](https://github.com/llancruzz/hogwarts-api/blob/main/comments/tests.py)
- [Contacts - View Tests](https://github.com/llancruzz/hogwarts-api/blob/main/contacts/tests.py)
- [Followers - View Tests](https://github.com/llancruzz/hogwarts-api/blob/main/followers/tests.py)
- [Likes - View Tests](https://github.com/llancruzz/hogwarts-api/blob/main/likes/tests.py)
- [Posts - View Tests](https://github.com/llancruzz/hogwarts-api/blob/main/posts/tests.py)

Please find the full coverage report [COVERAGE.md](https://github.com/llancruzz/hogwarts-api/blob/main/COVERAGE.md).

## Manual Testing

Manual testing took place throughout development of the API to ensure features functioned. These included visiting each URL to ensure accurate results were returned depending on authorization state, the creation, update and deletion of items:

### Endpoint Testing

| URL | Passed |
|---|---|
| root | :white_check_mark: |
| /comments/ | :white_check_mark: |
| /comments/\<id>/ | :white_check_mark: |
| /contacts/ | :white_check_mark: |
| /contacts/\<id>/ | :white_check_mark: |
| /followers/ | :white_check_mark: |
| /followers/\<id>/ | :white_check_mark: |
| /likes/ | :white_check_mark: |
| /likes/\<id>/ | :white_check_mark: |
| /posts/ | :white_check_mark: |
| /posts/\<id>/ | :white_check_mark: |
| /profiles/ | :white_check_mark: |
| /profiles/\<id>/ | :white_check_mark: |

### CRUD Functionality Testing

#### Comments App

| App | Action | Authenticated | Unauthenticated | Passed |
|---|---|---|---|---|
| Comments | Create | 201 Response | 403 Response | :white_check_mark: |
| Comments | Read (List) | 200 Response | 200 Response | :white_check_mark: |
| Comments | Update | 200 Response |403 Response | :white_check_mark: |
| Comments | Delete | 200 Response | 403 Response | :white_check_mark: |


#### Contacts App

| App | Action | Authenticated | Unauthenticated | Passed |
|---|---|---|---|---|
| Contacts | Create | 201 Response | N/A | :white_check_mark: |
| Contacts | Read (List) | N/A | N/A | N/A |
| Contacts | Update | N/A| N/A | N/A |
| Contacts | N/A | N/A | N/A  | N/A |

#### Followers App

| App | Action | Authenticated | Unauthenticated | Passed |
|---|---|---|---|---|
| Followers | Create | 201 Response | N/A | :white_check_mark: |
| Followers | Read (List) | 200 Response | 200 Response | :white_check_mark: |
| Followers| Update | 200 Response| 403 Response | :white_check_mark: |
| Followers | Delete | 200 Response | 403 Response  | :white_check_mark: |

#### Likes App

| App | Action | Authenticated | Unauthenticated | Passed |
|---|---|---|---|---|
| Likes | Create | 201 Response | 403 Response | :white_check_mark: |
| Likes | Read (List) | 200 Response | 200 Response | :white_check_mark: |
| Likes | Update | 200 Response| 403 Response | :white_check_mark: |
| Likes | Delete | 200 Response | 403cResponse  | :white_check_mark: |

#### Posts App

| App | Action | Authenticated | Unauthenticated | Passed |
|---|---|---|---|---|
| Posts | Create | 201 Response | 403 Response | :white_check_mark: |
| Posts | Read (List) | 200 Response | 403 Response | :white_check_mark: |
| Posts | Update | 200 Response| 403 Response | :white_check_mark: |
| Posts | Delete | 200 Response | 403 Response  | :white_check_mark: |

#### Profiles App

| App | Action | Authenticated | Unauthenticated | Passed |
|---|---|---|---|---|
| Profiles| Create | 201 Response | 201 Response | :white_check_mark: |
| Profiles | Read (List) | 200 Response | 200 Response | :white_check_mark: |
| Profiles | Update | 200 Response| 403 Response | N/A |
| Profiles | Delete | N/A | N/A  | N/A |
