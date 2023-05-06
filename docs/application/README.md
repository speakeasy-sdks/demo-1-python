# application

## Overview

An Application is a collection of Workloads that work together. When deployed, all Workloads in an Application are deployed to the same namespace.

Apps are the root of the configuration tree holding Environments, Deployments, Shared Values, and Secrets.
<SchemaDefinition schemaRef="#/components/schemas/ApplicationRequest" />


### Available Operations

* [delete_orgs_org_id_apps_app_id_](#delete_orgs_org_id_apps_app_id_) - Delete an Application
* [get_orgs_org_id_apps](#get_orgs_org_id_apps) - List all Applications in an Organization.
* [get_orgs_org_id_apps_app_id_](#get_orgs_org_id_apps_app_id_) - Get an existing Application
* [post_orgs_org_id_apps](#post_orgs_org_id_apps) - Add a new Application to an Organization

## delete_orgs_org_id_apps_app_id_

Deleting an Application will also delete everything associated with it. This includes Environments, Deployment history on those Environments, and any shared values and secrets associated.

_Deletions are currently irreversible._

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDAppsAppIDRequest(
    app_id='iure',
    org_id='magnam',
)

res = s.application.delete_orgs_org_id_apps_app_id_(req)

if res.status_code == 200:
    # handle response
```

## get_orgs_org_id_apps

Listing or lists of all Applications that exist within a specific Organization.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsRequest(
    org_id='debitis',
)

res = s.application.get_orgs_org_id_apps(req)

if res.application_responses is not None:
    # handle response
```

## get_orgs_org_id_apps_app_id_

Gets a specific Application in the specified Organization by ID.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDRequest(
    app_id='ipsa',
    org_id='delectus',
)

res = s.application.get_orgs_org_id_apps_app_id_(req)

if res.application_response is not None:
    # handle response
```

## post_orgs_org_id_apps

Creates a new Application, then adds it to the specified Organization.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsRequest(
    application_creation_request=shared.ApplicationCreationRequest(
        env=shared.EnvironmentBaseRequest(
            id='467cc879-6ed1-451a-85df-c2ddf7cc78ca',
            name='Antoinette Nikolaus',
            type='deleniti',
        ),
        id='fc816742-cb73-4920-9929-396fea7596eb',
        name='Brenda Wisozk',
    ),
    org_id='laborum',
)

res = s.application.post_orgs_org_id_apps(req)

if res.application_response is not None:
    # handle response
```
