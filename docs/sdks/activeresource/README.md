# active_resource

## Overview

Active Resources represent the concrete resources provisioned for an Environment. They are provisioned on the first deployment after a dependency on a particular resource type is introduced into an Environment. In general, Active Resources are only deleted when their introductory Environment is deleted.

Active Resources are provisioned based on a Resource Definition. The Resource Definition describes how to provision a concrete resource based on a Resource Type and metadata about the Environment (for example the Environment Type or the Application ID). The criteria for how to choose a Resource Definition is known as a Matching Criteria. If the Matching Criteria changes or the Resource Definition is deleted, the concrete resource represented by an Active Resource might be deleted and reprovisioned when a deployment occurs in the Environment.
<SchemaDefinition schemaRef="#/components/schemas/ActiveResourceRequest" />


### Available Operations

* [delete_orgs_org_id_apps_app_id_envs_env_id_resources_type_res_id_](#delete_orgs_org_id_apps_app_id_envs_env_id_resources_type_res_id_) - Delete Active Resources.
* [get_orgs_org_id_apps_app_id_envs_env_id_resources](#get_orgs_org_id_apps_app_id_envs_env_id_resources) - List Active Resources provisioned in an environment.
* [get_orgs_org_id_resources_defs_def_id_resources](#get_orgs_org_id_resources_defs_def_id_resources) - List Active Resources provisioned via a specific Resource Definition.

## delete_orgs_org_id_apps_app_id_envs_env_id_resources_type_res_id_

Delete Active Resources.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDResourcesTypeResIDRequest(
    app_id='distinctio',
    env_id='quibusdam',
    org_id='unde',
    res_id='nulla',
    type='corrupti',
)

res = s.active_resource.delete_orgs_org_id_apps_app_id_envs_env_id_resources_type_res_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDResourcesTypeResIDRequest](../../models/operations/deleteorgsorgidappsappidenvsenvidresourcestyperesidrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDResourcesTypeResIDResponse](../../models/operations/deleteorgsorgidappsappidenvsenvidresourcestyperesidresponse.md)**


## get_orgs_org_id_apps_app_id_envs_env_id_resources

List Active Resources provisioned in an environment.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDResourcesRequest(
    app_id='illum',
    env_id='vel',
    org_id='error',
)

res = s.active_resource.get_orgs_org_id_apps_app_id_envs_env_id_resources(req)

if res.active_resource_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDResourcesRequest](../../models/operations/getorgsorgidappsappidenvsenvidresourcesrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDResourcesResponse](../../models/operations/getorgsorgidappsappidenvsenvidresourcesresponse.md)**


## get_orgs_org_id_resources_defs_def_id_resources

List Active Resources provisioned via a specific Resource Definition.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDResourcesDefsDefIDResourcesRequest(
    def_id='deserunt',
    org_id='suscipit',
)

res = s.active_resource.get_orgs_org_id_resources_defs_def_id_resources(req)

if res.active_resource_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.GetOrgsOrgIDResourcesDefsDefIDResourcesRequest](../../models/operations/getorgsorgidresourcesdefsdefidresourcesrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.GetOrgsOrgIDResourcesDefsDefIDResourcesResponse](../../models/operations/getorgsorgidresourcesdefsdefidresourcesresponse.md)**

