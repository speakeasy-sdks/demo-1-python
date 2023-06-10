# runtime_info

## Overview

RuntimeInfo object returned by the runtime endpoint. Represents a list post statuses grouped by modules and controllers (deployments and stateful sets).
<SchemaDefinition schemaRef="#/components/schemas/RuntimeInfoRequest" />


### Available Operations

* [get_orgs_org_id_apps_app_id_envs_env_id_runtime](#get_orgs_org_id_apps_app_id_envs_env_id_runtime) - Get Runtime information about the environment.
* [get_orgs_org_id_apps_app_id_runtime](#get_orgs_org_id_apps_app_id_runtime) - Get Runtime information about specific environments.
* [patch_orgs_org_id_apps_app_id_envs_env_id_runtime_replicas](#patch_orgs_org_id_apps_app_id_envs_env_id_runtime_replicas) - Set number of replicas for an environment's modules.
* [put_orgs_org_id_apps_app_id_envs_env_id_runtime_paused](#put_orgs_org_id_apps_app_id_envs_env_id_runtime_paused) - Pause / Resume an environment.

## get_orgs_org_id_apps_app_id_envs_env_id_runtime

Get Runtime information about the environment.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRuntimeRequest(
    app_id='aut',
    env_id='aut',
    org_id='eveniet',
)

res = s.runtime_info.get_orgs_org_id_apps_app_id_envs_env_id_runtime(req)

if res.runtime_info_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRuntimeRequest](../../models/operations/getorgsorgidappsappidenvsenvidruntimerequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRuntimeResponse](../../models/operations/getorgsorgidappsappidenvsenvidruntimeresponse.md)**


## get_orgs_org_id_apps_app_id_runtime

Get Runtime information about specific environments.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDRuntimeRequest(
    app_id='odio',
    id='64ad7334-ec1b-4781-b36a-08088d100efa',
    org_id='nulla',
)

res = s.runtime_info.get_orgs_org_id_apps_app_id_runtime(req)

if res.environment_runtime_info_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetOrgsOrgIDAppsAppIDRuntimeRequest](../../models/operations/getorgsorgidappsappidruntimerequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetOrgsOrgIDAppsAppIDRuntimeResponse](../../models/operations/getorgsorgidappsappidruntimeresponse.md)**


## patch_orgs_org_id_apps_app_id_envs_env_id_runtime_replicas

Set number of replicas for an environment's modules.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.PatchOrgsOrgIDAppsAppIDEnvsEnvIDRuntimeReplicasRequest(
    request_body={
        "sed": 30208,
        "alias": 910073,
        "hic": 27982,
    },
    app_id='incidunt',
    env_id='qui',
    org_id='qui',
)

res = s.runtime_info.patch_orgs_org_id_apps_app_id_envs_env_id_runtime_replicas(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                              | [operations.PatchOrgsOrgIDAppsAppIDEnvsEnvIDRuntimeReplicasRequest](../../models/operations/patchorgsorgidappsappidenvsenvidruntimereplicasrequest.md) | :heavy_check_mark:                                                                                                                                     | The request object to use for the request.                                                                                                             |


### Response

**[operations.PatchOrgsOrgIDAppsAppIDEnvsEnvIDRuntimeReplicasResponse](../../models/operations/patchorgsorgidappsappidenvsenvidruntimereplicasresponse.md)**


## put_orgs_org_id_apps_app_id_envs_env_id_runtime_paused

On pause requests, all the Kubernetes Deployment resources are scaled down to 0 replicas.

On resume requests, all the Kubernetes Deployment resources are scaled up to the number of replicas running before the environment was paused.

When an environment is paused, it is not possible to:

```
  - Deploy the environment within Humanitec.
  - Scale the number of replicas running of any workload.
```

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDRuntimePausedRequest(
    request_body=False,
    app_id='necessitatibus',
    env_id='harum',
    org_id='explicabo',
)

res = s.runtime_info.put_orgs_org_id_apps_app_id_envs_env_id_runtime_paused(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                      | [operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDRuntimePausedRequest](../../models/operations/putorgsorgidappsappidenvsenvidruntimepausedrequest.md) | :heavy_check_mark:                                                                                                                             | The request object to use for the request.                                                                                                     |


### Response

**[operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDRuntimePausedResponse](../../models/operations/putorgsorgidappsappidenvsenvidruntimepausedresponse.md)**

