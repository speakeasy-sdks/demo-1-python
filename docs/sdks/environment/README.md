# environment

## Overview

Environments are independent spaces where Applications can run. An Application is always deployed into an Environment.
<SchemaDefinition schemaRef="#/components/schemas/EnvironmentRequest" />


### Available Operations

* [delete_orgs_org_id_apps_app_id_envs_env_id_](#delete_orgs_org_id_apps_app_id_envs_env_id_) - Delete a specific Environment.
* [get_orgs_org_id_apps_app_id_envs](#get_orgs_org_id_apps_app_id_envs) - List all Environments.
* [get_orgs_org_id_apps_app_id_envs_env_id_](#get_orgs_org_id_apps_app_id_envs_env_id_) - Get a specific Environment.
* [post_orgs_org_id_apps_app_id_envs](#post_orgs_org_id_apps_app_id_envs) - Add a new Environment to an Application.
* [put_orgs_org_id_apps_app_id_envs_env_id_from_deploy_id](#put_orgs_org_id_apps_app_id_envs_env_id_from_deploy_id) - Rebase to a different Deployment.

## delete_orgs_org_id_apps_app_id_envs_env_id_

Deletes a specific Environment in an Application.

Deleting an Environment will also delete the Deployment history of the Environment.

_Deletions are currently irreversible._

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDRequest(
    app_id='dicta',
    env_id='nisi',
    org_id='consequuntur',
)

res = s.environment.delete_orgs_org_id_apps_app_id_envs_env_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDRequest](../../models/operations/deleteorgsorgidappsappidenvsenvidrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDResponse](../../models/operations/deleteorgsorgidappsappidenvsenvidresponse.md)**


## get_orgs_org_id_apps_app_id_envs

Lists all of the Environments in the Application.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDEnvsRequest(
    app_id='consectetur',
    org_id='aperiam',
)

res = s.environment.get_orgs_org_id_apps_app_id_envs(req)

if res.environment_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetOrgsOrgIDAppsAppIDEnvsRequest](../../models/operations/getorgsorgidappsappidenvsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetOrgsOrgIDAppsAppIDEnvsResponse](../../models/operations/getorgsorgidappsappidenvsresponse.md)**


## get_orgs_org_id_apps_app_id_envs_env_id_

Gets a specific Environment in an Application.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRequest(
    app_id='cupiditate',
    env_id='reiciendis',
    org_id='soluta',
)

res = s.environment.get_orgs_org_id_apps_app_id_envs_env_id_(req)

if res.environment_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRequest](../../models/operations/getorgsorgidappsappidenvsenvidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDResponse](../../models/operations/getorgsorgidappsappidenvsenvidresponse.md)**


## post_orgs_org_id_apps_app_id_envs

Creates a new Environment of the specified Type and associates it with the Application specified by `appId`.

The Environment is also initialized to the **current or past state of Deployment in another Environment**. This ensures that every Environment is derived from a previously known state. This means it is not possible to create a new Environment for an Application until at least one Deployment has occurred. (The Deployment does not have to be successful.)

The Type of the Environment must be already defined in the Organization.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDEnvsRequest(
    environment_definition_request=shared.EnvironmentDefinitionRequest(
        from_deploy_id='alias',
        id='929921ae-fb9f-458c-8d86-e68e4be05601',
        name='Shawna Hamill',
        type='deserunt',
    ),
    app_id='esse',
    org_id='nemo',
)

res = s.environment.post_orgs_org_id_apps_app_id_envs(req)

if res.environment_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PostOrgsOrgIDAppsAppIDEnvsRequest](../../models/operations/postorgsorgidappsappidenvsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PostOrgsOrgIDAppsAppIDEnvsResponse](../../models/operations/postorgsorgidappsappidenvsresponse.md)**


## put_orgs_org_id_apps_app_id_envs_env_id_from_deploy_id

Rebasing an Environment means that the next Deployment to the Environment will be based on the Deployment specified in the rebase rather than the last one in the Environment. The Deployment to rebase to can either be current or a previous Deployment. The Deployment can be from any Environment of the same Application.

_Running code will only be affected on the next Deployment to the Environment._

Common use cases for rebasing an Environment:

* _Rollback_: Rebasing to a previous Deployment in the current Environment and then Deploying without additional changes will execute a rollback to the previous Deployment state.

* _Clone_: Rebasing to the current Deployment in a different Environment and then deploying without additional changes will clone all of the configuration of the other Environment into the current one. (NOTE: External Resources will not be cloned in the process - the current External Resources of the Environment will remain unchanged and will be used by the deployed Application in the Environment.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDFromDeployIDRequest(
    request_body='reprehenderit',
    app_id='est',
    env_id='quis',
    org_id='sint',
)

res = s.environment.put_orgs_org_id_apps_app_id_envs_env_id_from_deploy_id(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDFromDeployIDRequest](../../models/operations/putorgsorgidappsappidenvsenvidfromdeployidrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDFromDeployIDResponse](../../models/operations/putorgsorgidappsappidenvsenvidfromdeployidresponse.md)**

