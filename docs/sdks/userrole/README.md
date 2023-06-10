# user_role

## Overview

UserRole holds the mapping of role to user for a particular object.
<SchemaDefinition schemaRef="#/components/schemas/UserRoleRequest" />


### Available Operations

* [delete_orgs_org_id_apps_app_id_users_user_id_](#delete_orgs_org_id_apps_app_id_users_user_id_) - Remove the role of a User on an Application
* [delete_orgs_org_id_env_types_env_type_users_user_id_](#delete_orgs_org_id_env_types_env_type_users_user_id_) - Remove the role of a User on an Environment Type
* [delete_orgs_org_id_users_user_id_](#delete_orgs_org_id_users_user_id_) - Remove the role of a User on an Organization
* [get_orgs_org_id_apps_app_id_users](#get_orgs_org_id_apps_app_id_users) - List Users with roles in an App
* [get_orgs_org_id_apps_app_id_users_user_id_](#get_orgs_org_id_apps_app_id_users_user_id_) - Get the role of a User on an Application
* [get_orgs_org_id_env_types_env_type_users_user_id_](#get_orgs_org_id_env_types_env_type_users_user_id_) - Get the role of a User on an Environment Type
* [get_orgs_org_id_users](#get_orgs_org_id_users) - List Users with roles in an Organization
* [get_orgs_org_id_users_user_id_](#get_orgs_org_id_users_user_id_) - Get the role of a User on an Organization
* [patch_orgs_org_id_apps_app_id_users_user_id_](#patch_orgs_org_id_apps_app_id_users_user_id_) - Update the role of a User on an Application
* [patch_orgs_org_id_env_types_env_type_users_user_id_](#patch_orgs_org_id_env_types_env_type_users_user_id_) - Update the role of a User on an Environment Type
* [patch_orgs_org_id_users_user_id_](#patch_orgs_org_id_users_user_id_) - Update the role of a User on an Organization
* [post_orgs_org_id_apps_app_id_users](#post_orgs_org_id_apps_app_id_users) - Adds a User to an Application with a Role
* [post_orgs_org_id_env_types_env_type_users](#post_orgs_org_id_env_types_env_type_users) - Adds a User to an Environment Type with a Role
* [post_orgs_org_id_invitations](#post_orgs_org_id_invitations) - Invites a user to an Organization with a specified role.

## delete_orgs_org_id_apps_app_id_users_user_id_

Remove the role of a User on an Application

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDAppsAppIDUsersUserIDRequest(
    app_id='doloremque',
    org_id='perferendis',
    user_id='laudantium',
)

res = s.user_role.delete_orgs_org_id_apps_app_id_users_user_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.DeleteOrgsOrgIDAppsAppIDUsersUserIDRequest](../../models/operations/deleteorgsorgidappsappidusersuseridrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.DeleteOrgsOrgIDAppsAppIDUsersUserIDResponse](../../models/operations/deleteorgsorgidappsappidusersuseridresponse.md)**


## delete_orgs_org_id_env_types_env_type_users_user_id_

Remove the role of a User on an Environment Type

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDEnvTypesEnvTypeUsersUserIDRequest(
    env_type='iusto',
    org_id='corrupti',
    user_id='molestiae',
)

res = s.user_role.delete_orgs_org_id_env_types_env_type_users_user_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.DeleteOrgsOrgIDEnvTypesEnvTypeUsersUserIDRequest](../../models/operations/deleteorgsorgidenvtypesenvtypeusersuseridrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.DeleteOrgsOrgIDEnvTypesEnvTypeUsersUserIDResponse](../../models/operations/deleteorgsorgidenvtypesenvtypeusersuseridresponse.md)**


## delete_orgs_org_id_users_user_id_

Remove the role of a User on an Organization

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDUsersUserIDRequest(
    org_id='quis',
    user_id='iure',
)

res = s.user_role.delete_orgs_org_id_users_user_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.DeleteOrgsOrgIDUsersUserIDRequest](../../models/operations/deleteorgsorgidusersuseridrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.DeleteOrgsOrgIDUsersUserIDResponse](../../models/operations/deleteorgsorgidusersuseridresponse.md)**


## get_orgs_org_id_apps_app_id_users

List Users with roles in an App

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDUsersRequest(
    app_id='ab',
    org_id='quaerat',
)

res = s.user_role.get_orgs_org_id_apps_app_id_users(req)

if res.user_role_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetOrgsOrgIDAppsAppIDUsersRequest](../../models/operations/getorgsorgidappsappidusersrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetOrgsOrgIDAppsAppIDUsersResponse](../../models/operations/getorgsorgidappsappidusersresponse.md)**


## get_orgs_org_id_apps_app_id_users_user_id_

Get the role of a User on an Application

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDUsersUserIDRequest(
    app_id='amet',
    org_id='sapiente',
    user_id='corporis',
)

res = s.user_role.get_orgs_org_id_apps_app_id_users_user_id_(req)

if res.user_role_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetOrgsOrgIDAppsAppIDUsersUserIDRequest](../../models/operations/getorgsorgidappsappidusersuseridrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GetOrgsOrgIDAppsAppIDUsersUserIDResponse](../../models/operations/getorgsorgidappsappidusersuseridresponse.md)**


## get_orgs_org_id_env_types_env_type_users_user_id_

Get the role of a User on an Environment Type

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDEnvTypesEnvTypeUsersUserIDRequest(
    env_type='est',
    org_id='iure',
    user_id='quisquam',
)

res = s.user_role.get_orgs_org_id_env_types_env_type_users_user_id_(req)

if res.user_role_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.GetOrgsOrgIDEnvTypesEnvTypeUsersUserIDRequest](../../models/operations/getorgsorgidenvtypesenvtypeusersuseridrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.GetOrgsOrgIDEnvTypesEnvTypeUsersUserIDResponse](../../models/operations/getorgsorgidenvtypesenvtypeusersuseridresponse.md)**


## get_orgs_org_id_users

List Users with roles in an Organization

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDUsersRequest(
    org_id='provident',
)

res = s.user_role.get_orgs_org_id_users(req)

if res.user_role_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetOrgsOrgIDUsersRequest](../../models/operations/getorgsorgidusersrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetOrgsOrgIDUsersResponse](../../models/operations/getorgsorgidusersresponse.md)**


## get_orgs_org_id_users_user_id_

Get the role of a User on an Organization

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDUsersUserIDRequest(
    org_id='laudantium',
    user_id='nam',
)

res = s.user_role.get_orgs_org_id_users_user_id_(req)

if res.user_role_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetOrgsOrgIDUsersUserIDRequest](../../models/operations/getorgsorgidusersuseridrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetOrgsOrgIDUsersUserIDResponse](../../models/operations/getorgsorgidusersuseridresponse.md)**


## patch_orgs_org_id_apps_app_id_users_user_id_

Update the role of a User on an Application

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PatchOrgsOrgIDAppsAppIDUsersUserIDRequest(
    role_request=shared.RoleRequest(
        role='nemo',
    ),
    app_id='enim',
    org_id='ipsam',
    user_id='minima',
)

res = s.user_role.patch_orgs_org_id_apps_app_id_users_user_id_(req)

if res.user_role_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.PatchOrgsOrgIDAppsAppIDUsersUserIDRequest](../../models/operations/patchorgsorgidappsappidusersuseridrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.PatchOrgsOrgIDAppsAppIDUsersUserIDResponse](../../models/operations/patchorgsorgidappsappidusersuseridresponse.md)**


## patch_orgs_org_id_env_types_env_type_users_user_id_

Update the role of a User on an Environment Type

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PatchOrgsOrgIDEnvTypesEnvTypeUsersUserIDRequest(
    role_request=shared.RoleRequest(
        role='tempora',
    ),
    env_type='perferendis',
    org_id='corrupti',
    user_id='doloremque',
)

res = s.user_role.patch_orgs_org_id_env_types_env_type_users_user_id_(req)

if res.user_role_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.PatchOrgsOrgIDEnvTypesEnvTypeUsersUserIDRequest](../../models/operations/patchorgsorgidenvtypesenvtypeusersuseridrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.PatchOrgsOrgIDEnvTypesEnvTypeUsersUserIDResponse](../../models/operations/patchorgsorgidenvtypesenvtypeusersuseridresponse.md)**


## patch_orgs_org_id_users_user_id_

Update the role of a User on an Organization

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PatchOrgsOrgIDUsersUserIDRequest(
    role_request=shared.RoleRequest(
        role='fugiat',
    ),
    org_id='numquam',
    user_id='doloremque',
)

res = s.user_role.patch_orgs_org_id_users_user_id_(req)

if res.user_role_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.PatchOrgsOrgIDUsersUserIDRequest](../../models/operations/patchorgsorgidusersuseridrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.PatchOrgsOrgIDUsersUserIDResponse](../../models/operations/patchorgsorgidusersuseridresponse.md)**


## post_orgs_org_id_apps_app_id_users

Adds a User to an Application with a Role

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDUsersRequest(
    user_role_request=shared.UserRoleRequest(
        created_at='2020-06-22T09:37:23.523Z',
        email='Neva_Murphy39@hotmail.com',
        id='cbd6b5f3-ec90-4930-8f92-6bad2553819b',
        invite='tempora',
        name='Dr. Monica Ratke',
        role='fugit',
        type='voluptatem',
        user='repudiandae',
    ),
    app_id='corporis',
    org_id='ea',
)

res = s.user_role.post_orgs_org_id_apps_app_id_users(req)

if res.user_role_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PostOrgsOrgIDAppsAppIDUsersRequest](../../models/operations/postorgsorgidappsappidusersrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PostOrgsOrgIDAppsAppIDUsersResponse](../../models/operations/postorgsorgidappsappidusersresponse.md)**


## post_orgs_org_id_env_types_env_type_users

Adds a User to an Environment Type with a Role

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDEnvTypesEnvTypeUsersRequest(
    user_role_request=shared.UserRoleRequest(
        created_at='2020-06-22T09:37:23.523Z',
        email='Elmer_Kuvalis99@gmail.com',
        id='639a910a-bdca-4b62-a766-96e1ec00221b',
        invite='sequi',
        name='Yvonne Stamm',
        role='similique',
        type='eligendi',
        user='tempore',
    ),
    env_type='amet',
    org_id='debitis',
)

res = s.user_role.post_orgs_org_id_env_types_env_type_users(req)

if res.user_role_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.PostOrgsOrgIDEnvTypesEnvTypeUsersRequest](../../models/operations/postorgsorgidenvtypesenvtypeusersrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.PostOrgsOrgIDEnvTypesEnvTypeUsersResponse](../../models/operations/postorgsorgidenvtypesenvtypeusersresponse.md)**


## post_orgs_org_id_invitations

Invites a user to an Organization with a specified role.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDInvitationsRequest(
    user_invite_request_request=shared.UserInviteRequestRequest(
        email='Yasmine_Smith@hotmail.com',
        role='quibusdam',
    ),
    org_id='sit',
)

res = s.user_role.post_orgs_org_id_invitations(req)

if res.user_role_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PostOrgsOrgIDInvitationsRequest](../../models/operations/postorgsorgidinvitationsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.PostOrgsOrgIDInvitationsResponse](../../models/operations/postorgsorgidinvitationsresponse.md)**

