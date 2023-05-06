# user_profile

## Overview

UserProfile holds the profile information of a user
<SchemaDefinition schemaRef="#/components/schemas/UserProfileRequest" />


### Available Operations

* [delete_tokens_token_id_](#delete_tokens_token_id_) - DEPRECATED
* [get_current_user](#get_current_user) - Gets the extended profile of the current user
* [get_tokens](#get_tokens) - DEPRECATED
* [get_users_me](#get_users_me) - DEPRECATED
* [patch_current_user](#patch_current_user) - Updates the extended profile of the current user.
* [post_orgs_org_id_users](#post_orgs_org_id_users) - Creates a new service user.

## delete_tokens_token_id_

DEPRECATED

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteTokensTokenIDRequest(
    token_id='eligendi',
)

res = s.user_profile.delete_tokens_token_id_(req)

if res.status_code == 200:
    # handle response
```

## get_current_user

Gets the extended profile of the current user

### Example Usage

```python
import test_1


s = test_1.Test1()


res = s.user_profile.get_current_user()

if res.user_profile_extended_response is not None:
    # handle response
```

## get_tokens

DEPRECATED

### Example Usage

```python
import test_1


s = test_1.Test1()


res = s.user_profile.get_tokens()

if res.get_tokens_200_application_json_object is not None:
    # handle response
```

## get_users_me

DEPRECATED

### Example Usage

```python
import test_1


s = test_1.Test1()


res = s.user_profile.get_users_me()

if res.get_users_me_200_application_json_object is not None:
    # handle response
```

## patch_current_user

Updates the extended profile of the current user.

### Example Usage

```python
import test_1
from test_1.models import shared

s = test_1.Test1()

req = shared.UserProfileExtendedRequest(
    created_at='2020-06-22T09:37:23.523Z',
    email='Gunnar98@hotmail.com',
    id='eeb1c7cb-db6e-4ec7-8378-ba25317747dc',
    name='Gregory Heidenreich',
    properties={
        "maxime": 'dolorum',
    },
    roles={
        "nostrum": 'illum',
        "quibusdam": 'commodi',
        "esse": 'explicabo',
        "consectetur": 'temporibus',
    },
    type='optio',
)

res = s.user_profile.patch_current_user(req)

if res.user_profile_extended_response is not None:
    # handle response
```

## post_orgs_org_id_users

Creates a new service user.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDUsersRequest(
    new_service_user_request=shared.NewServiceUserRequest(
        email='Wilford_Heller@gmail.com',
        name='Dixie Doyle',
        role='harum',
    ),
    org_id='ducimus',
)

res = s.user_profile.post_orgs_org_id_users(req)

if res.user_profile_extended_response is not None:
    # handle response
```
