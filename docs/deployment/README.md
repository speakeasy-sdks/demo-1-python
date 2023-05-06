# deployment

## Overview

Deployments represent updates to the running state of an Environment.

Deployments are made by applying _Deltas_ to a state defined by an existing Deployment. The Environment’s from_deploy property defines the Deployment. This Deployment is usually but not always in the current Environment. If the Deployment is from another Environment, the state of that Environment will be "cloned" into the current Environment with the option to apply a Delta.
<SchemaDefinition schemaRef="#/components/schemas/DeploymentRequest" />


### Available Operations

* [get_orgs_org_id_apps_app_id_envs_env_id_deploys](#get_orgs_org_id_apps_app_id_envs_env_id_deploys) - List Deployments in an Environment.
* [get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_](#get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_) - Get a specific Deployment.
* [get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_errors](#get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_errors) - List errors that occurred in a Deployment.
* [post_orgs_org_id_apps_app_id_envs_env_id_deploys](#post_orgs_org_id_apps_app_id_envs_env_id_deploys) - Start a new Deployment.

## get_orgs_org_id_apps_app_id_envs_env_id_deploys

List all of the Deployments that have been carried out in the current Environment. Deployments are returned with the newest first.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDDeploysRequest(
    app_id='ullam',
    env_id='perferendis',
    org_id='illum',
)

res = s.deployment.get_orgs_org_id_apps_app_id_envs_env_id_deploys(req)

if res.deployment_responses is not None:
    # handle response
```

## get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_

Gets a specific Deployment in an Application and an Environment.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDDeploysDeployIDRequest(
    app_id='totam',
    deploy_id='impedit',
    env_id='quibusdam',
    org_id='nam',
)

res = s.deployment.get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_(req)

if res.deployment_response is not None:
    # handle response
```

## get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_errors

List errors that occurred in a Deployment.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDDeploysDeployIDErrorsRequest(
    app_id='ipsam',
    deploy_id='culpa',
    env_id='dolor',
    org_id='aliquam',
)

res = s.deployment.get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_errors(req)

if res.deployment_error_responses is not None:
    # handle response
```

## post_orgs_org_id_apps_app_id_envs_env_id_deploys

At Humanitec, Deployments are defined as changes to the state of the Environment. The state can be changed by defining a set of desired changes to the current state via a Deployment Delta or by resetting the current state after a previous Deployment. (See Environment Rebase.) Both types of changes can be combined into a single Deployment during which the Delta is applied to the Rebased state.

When specifying a Delta, a Delta ID must be used. That Delta must have been committed to the Delta store prior to the Deployment.

A Set ID can also be defined in the deployment to force the state of the environment to a particular state. This will be ignored if the Delta is specified.

**NOTE:**

Directly setting a `set_id` in a deployment is not recommended as it will not record history of where the set came from. If the intention is to replicate an existing environment, use the environment rebasing approach described above.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDDeploysRequest(
    deployment_request=shared.DeploymentRequest(
        comment='inventore',
        delta_id='deleniti',
        value_set_version_id='veritatis',
    ),
    app_id='tempora',
    env_id='dolor',
    org_id='consequatur',
)

res = s.deployment.post_orgs_org_id_apps_app_id_envs_env_id_deploys(req)

if res.deployment_response is not None:
    # handle response
```
