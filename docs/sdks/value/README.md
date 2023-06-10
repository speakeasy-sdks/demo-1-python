# value

## Overview

Shared Values can be used to manage variables and configuration that might vary between environments. They are also the way that secrets can be stored securely.

Shared Values are by default shared across all environments in an application. However, they can be overridden on an Environment by Environment basis.

For example: There might be 2 API keys that are used in an application. One development key used in the development and staging environments and another used for production. The development API key would be set at the Application level. The value would then be overridden at the Environment level for the production Environment.
<SchemaDefinition schemaRef="#/components/schemas/ValueRequest" />


### Available Operations

* [delete_orgs_org_id_apps_app_id_envs_env_id_values](#delete_orgs_org_id_apps_app_id_envs_env_id_values) - Delete all Shared Value for an Environment
* [delete_orgs_org_id_apps_app_id_envs_env_id_values_key_](#delete_orgs_org_id_apps_app_id_envs_env_id_values_key_) - Delete Shared Value for an Environment
* [delete_orgs_org_id_apps_app_id_values](#delete_orgs_org_id_apps_app_id_values) - Delete all Shared Value for an App
* [delete_orgs_org_id_apps_app_id_values_key_](#delete_orgs_org_id_apps_app_id_values_key_) - Delete Shared Value for an Application
* [get_orgs_org_id_apps_app_id_envs_env_id_values](#get_orgs_org_id_apps_app_id_envs_env_id_values) - List Shared Values in an Environment
* [get_orgs_org_id_apps_app_id_values](#get_orgs_org_id_apps_app_id_values) - List Shared Values in an Application
* [patch_orgs_org_id_apps_app_id_envs_env_id_values_key_](#patch_orgs_org_id_apps_app_id_envs_env_id_values_key_) - Update Shared Value for an Environment
* [patch_orgs_org_id_apps_app_id_values_key_](#patch_orgs_org_id_apps_app_id_values_key_) - Update Shared Value for an Application
* [post_orgs_org_id_apps_app_id_envs_env_id_values](#post_orgs_org_id_apps_app_id_envs_env_id_values) - Create a Shared Value for an Environment
* [post_orgs_org_id_apps_app_id_values](#post_orgs_org_id_apps_app_id_values) - Create a Shared Value for an Application
* [put_orgs_org_id_apps_app_id_envs_env_id_values_key_](#put_orgs_org_id_apps_app_id_envs_env_id_values_key_) - Update Shared Value for an Environment
* [put_orgs_org_id_apps_app_id_values_key_](#put_orgs_org_id_apps_app_id_values_key_) - Update Shared Value for an Application

## delete_orgs_org_id_apps_app_id_envs_env_id_values

All Shared Values will be deleted. If the Shared Values are marked as a secret, they will also be deleted.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDValuesRequest(
    app_id='quo',
    env_id='veniam',
    org_id='aliquam',
)

res = s.value.delete_orgs_org_id_apps_app_id_envs_env_id_values(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDValuesRequest](../../models/operations/deleteorgsorgidappsappidenvsenvidvaluesrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDValuesResponse](../../models/operations/deleteorgsorgidappsappidenvsenvidvaluesresponse.md)**


## delete_orgs_org_id_apps_app_id_envs_env_id_values_key_

The specified Shared Value will be permanently deleted. If the Shared Value is marked as a secret, it will also be permanently deleted.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyRequest(
    app_id='provident',
    env_id='vero',
    key='earum',
    org_id='doloremque',
)

res = s.value.delete_orgs_org_id_apps_app_id_envs_env_id_values_key_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyRequest](../../models/operations/deleteorgsorgidappsappidenvsenvidvalueskeyrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyResponse](../../models/operations/deleteorgsorgidappsappidenvsenvidvalueskeyresponse.md)**


## delete_orgs_org_id_apps_app_id_values

All Shared Values will be deleted. If the Shared Values are marked as a secret, they will also be deleted.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDAppsAppIDValuesRequest(
    app_id='ipsum',
    org_id='alias',
)

res = s.value.delete_orgs_org_id_apps_app_id_values(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.DeleteOrgsOrgIDAppsAppIDValuesRequest](../../models/operations/deleteorgsorgidappsappidvaluesrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.DeleteOrgsOrgIDAppsAppIDValuesResponse](../../models/operations/deleteorgsorgidappsappidvaluesresponse.md)**


## delete_orgs_org_id_apps_app_id_values_key_

The specified Shared Value will be permanently deleted. If the Shared Value is marked as a secret, it will also be permanently deleted.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDAppsAppIDValuesKeyRequest(
    app_id='doloremque',
    key='tempora',
    org_id='perspiciatis',
)

res = s.value.delete_orgs_org_id_apps_app_id_values_key_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.DeleteOrgsOrgIDAppsAppIDValuesKeyRequest](../../models/operations/deleteorgsorgidappsappidvalueskeyrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.DeleteOrgsOrgIDAppsAppIDValuesKeyResponse](../../models/operations/deleteorgsorgidappsappidvalueskeyresponse.md)**


## get_orgs_org_id_apps_app_id_envs_env_id_values

The returned values will be the base Application values with the Environment overrides where applicable. The `source` field will specify the level from which the value is from.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValuesRequest(
    app_id='quam',
    env_id='atque',
    org_id='officia',
)

res = s.value.get_orgs_org_id_apps_app_id_envs_env_id_values(req)

if res.value_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValuesRequest](../../models/operations/getorgsorgidappsappidenvsenvidvaluesrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValuesResponse](../../models/operations/getorgsorgidappsappidenvsenvidvaluesresponse.md)**


## get_orgs_org_id_apps_app_id_values

The returned values will be the "base" values for the Application. The overridden value for the Environment can be retrieved via the `/orgs/{orgId}/apps/{appId}/envs/{envId}/values` endpoint.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDValuesRequest(
    app_id='ex',
    org_id='architecto',
)

res = s.value.get_orgs_org_id_apps_app_id_values(req)

if res.value_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetOrgsOrgIDAppsAppIDValuesRequest](../../models/operations/getorgsorgidappsappidvaluesrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetOrgsOrgIDAppsAppIDValuesResponse](../../models/operations/getorgsorgidappsappidvaluesresponse.md)**


## patch_orgs_org_id_apps_app_id_envs_env_id_values_key_

Update the value or description of the Shared Value. Shared Values marked as secret can also be updated.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PatchOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyRequest(
    value_patch_payload_request=shared.ValuePatchPayloadRequest(
        description='a',
        value='laborum',
    ),
    app_id='veritatis',
    env_id='quod',
    key='a',
    org_id='qui',
)

res = s.value.patch_orgs_org_id_apps_app_id_envs_env_id_values_key_(req)

if res.value_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.PatchOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyRequest](../../models/operations/patchorgsorgidappsappidenvsenvidvalueskeyrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.PatchOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyResponse](../../models/operations/patchorgsorgidappsappidenvsenvidvalueskeyresponse.md)**


## patch_orgs_org_id_apps_app_id_values_key_

Update the value or description of the Shared Value. Shared Values marked as secret can also be updated.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PatchOrgsOrgIDAppsAppIDValuesKeyRequest(
    value_patch_payload_request=shared.ValuePatchPayloadRequest(
        description='accusantium',
        value='commodi',
    ),
    app_id='atque',
    key='totam',
    org_id='tenetur',
)

res = s.value.patch_orgs_org_id_apps_app_id_values_key_(req)

if res.value_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PatchOrgsOrgIDAppsAppIDValuesKeyRequest](../../models/operations/patchorgsorgidappsappidvalueskeyrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.PatchOrgsOrgIDAppsAppIDValuesKeyResponse](../../models/operations/patchorgsorgidappsappidvalueskeyresponse.md)**


## post_orgs_org_id_apps_app_id_envs_env_id_values

The Shared Value created will only be available to the specific Environment.

If a Value is marked as a secret, it will be securely stored. It will not be possible to retrieve the value again through the API. The value of the secret can however be updated.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValuesRequest(
    value_create_payload_request=shared.ValueCreatePayloadRequest(
        description='voluptate',
        is_secret=False,
        key='quam',
        value='quod',
    ),
    app_id='vitae',
    env_id='sapiente',
    org_id='reiciendis',
)

res = s.value.post_orgs_org_id_apps_app_id_envs_env_id_values(req)

if res.value_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValuesRequest](../../models/operations/postorgsorgidappsappidenvsenvidvaluesrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValuesResponse](../../models/operations/postorgsorgidappsappidenvsenvidvaluesresponse.md)**


## post_orgs_org_id_apps_app_id_values

The Shared Value created will be available to all Environments in that Application.

If a Value is marked as a secret, it will be securely stored. It will not be possible to retrieve the value again through the API. The value of the secret can however be updated.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDValuesRequest(
    value_create_payload_request=shared.ValueCreatePayloadRequest(
        description='quod',
        is_secret=False,
        key='voluptate',
        value='inventore',
    ),
    app_id='facere',
    org_id='maxime',
)

res = s.value.post_orgs_org_id_apps_app_id_values(req)

if res.value_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PostOrgsOrgIDAppsAppIDValuesRequest](../../models/operations/postorgsorgidappsappidvaluesrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PostOrgsOrgIDAppsAppIDValuesResponse](../../models/operations/postorgsorgidappsappidvaluesresponse.md)**


## put_orgs_org_id_apps_app_id_envs_env_id_values_key_

Update the value or description of the Shared Value. Shared Values marked as secret can also be updated.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyRequest(
    value_edit_payload_request=shared.ValueEditPayloadRequest(
        description='fuga',
        is_secret=False,
        key='ab',
        value='ex',
    ),
    app_id='consectetur',
    env_id='maiores',
    key='sed',
    org_id='animi',
)

res = s.value.put_orgs_org_id_apps_app_id_envs_env_id_values_key_(req)

if res.value_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyRequest](../../models/operations/putorgsorgidappsappidenvsenvidvalueskeyrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyResponse](../../models/operations/putorgsorgidappsappidenvsenvidvalueskeyresponse.md)**


## put_orgs_org_id_apps_app_id_values_key_

Update the value or description of the Shared Value. Shared Values marked as secret can also be updated.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PutOrgsOrgIDAppsAppIDValuesKeyRequest(
    value_edit_payload_request=shared.ValueEditPayloadRequest(
        description='sequi',
        is_secret=False,
        key='eligendi',
        value='voluptatum',
    ),
    app_id='perferendis',
    key='laborum',
    org_id='omnis',
)

res = s.value.put_orgs_org_id_apps_app_id_values_key_(req)

if res.value_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PutOrgsOrgIDAppsAppIDValuesKeyRequest](../../models/operations/putorgsorgidappsappidvalueskeyrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PutOrgsOrgIDAppsAppIDValuesKeyResponse](../../models/operations/putorgsorgidappsappidvalueskeyresponse.md)**

