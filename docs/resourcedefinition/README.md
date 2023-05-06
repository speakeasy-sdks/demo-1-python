# resource_definition

## Overview

A Resource Definitions describes how and when a resource should be provisioned. It links a driver (the how) along with a Matching Criteria (the when) to a Resource Type. This allows Humanitec to invoke a particular driver for the required Resource Type in the context of a particular Application and Environment.

The schema for the `driver_inputs` is defined by the `input_schema` property on the DriverDefinition identified by the `driver_type` property.
<SchemaDefinition schemaRef="#/components/schemas/ResourceDefinitionRequest" />


### Available Operations

* [delete_orgs_org_id_resources_defs_def_id_](#delete_orgs_org_id_resources_defs_def_id_) - Delete a Resource Definition.
* [delete_orgs_org_id_resources_defs_def_id_criteria_criteria_id_](#delete_orgs_org_id_resources_defs_def_id_criteria_criteria_id_) - Delete a Matching Criteria from a Resource Definition.
* [get_orgs_org_id_resources_defs](#get_orgs_org_id_resources_defs) - List Resource Definitions.
* [get_orgs_org_id_resources_defs_def_id_](#get_orgs_org_id_resources_defs_def_id_) - Get a specific Resource Definition.
* [get_orgs_org_id_resources_defs_def_id_resources](#get_orgs_org_id_resources_defs_def_id_resources) - List Active Resources provisioned via a specific Resource Definition.
* [patch_orgs_org_id_resources_defs_def_id_](#patch_orgs_org_id_resources_defs_def_id_) - Update a Resource Definition.
* [post_orgs_org_id_resources_defs](#post_orgs_org_id_resources_defs) - Create a new Resource Definition.
* [post_orgs_org_id_resources_defs_def_id_criteria](#post_orgs_org_id_resources_defs_def_id_criteria) - Add a new Matching Criteria to a Resource Definition.
* [put_orgs_org_id_resources_defs_def_id_](#put_orgs_org_id_resources_defs_def_id_) - Update a Resource Definition.

## delete_orgs_org_id_resources_defs_def_id_

If there **are no** Active Resources provisioned via the current definition, the Resource Definition is deleted immediately.

If there **are** Active Resources provisioned via the current definition, the request fails. The response will describe the changes to the affected Active Resources if operation is forced.

The request can take an optional `force` query parameter. If set to `true`, the current Resource Definition is **marked as** pending deletion and will be deleted (purged) as soon as no existing Active Resources reference it. With the next deployment matching criteria for Resources will be re-evaluated, and current Active Resources for the target environment would be either linked to another matching Resource Definition or decommissioned and created using the new or default Resource Definition (when available).

The Resource Definition that has been marked for deletion cannot be used to provision new resources.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDResourcesDefsDefIDRequest(
    def_id='asperiores',
    force=False,
    org_id='veniam',
)

res = s.resource_definition.delete_orgs_org_id_resources_defs_def_id_(req)

if res.status_code == 200:
    # handle response
```

## delete_orgs_org_id_resources_defs_def_id_criteria_criteria_id_

If there **are no** Active Resources that would match to a different Resource Definition when the current Matching Criteria is deleted, the Matching Criteria is deleted immediately.

If there **are** Active Resources that would match to a different Resource Definition, the request fails with HTTP status code 409 (Conflict). The response content will list all of affected Active Resources and their new matches.

The request can take an optional `force` query parameter. If set to `true`, the Matching Criteria is deleted immediately. Referenced Active Resources would match to a different Resource Definition during the next deployment in the target environment.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDResourcesDefsDefIDCriteriaCriteriaIDRequest(
    criteria_id='consequuntur',
    def_id='facere',
    force=False,
    org_id='laudantium',
)

res = s.resource_definition.delete_orgs_org_id_resources_defs_def_id_criteria_criteria_id_(req)

if res.status_code == 200:
    # handle response
```

## get_orgs_org_id_resources_defs

Filter criteria can be applied to obtain all the resource definitions that could match the filters, grouped by type and sorted by matching rank.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDResourcesDefsRequest(
    app='odit',
    env='pariatur',
    env_type='amet',
    org_id='exercitationem',
    res='ab',
    res_type='velit',
)

res = s.resource_definition.get_orgs_org_id_resources_defs(req)

if res.resource_definition_responses is not None:
    # handle response
```

## get_orgs_org_id_resources_defs_def_id_

Get a specific Resource Definition.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDResourcesDefsDefIDRequest(
    def_id='facilis',
    org_id='tempore',
)

res = s.resource_definition.get_orgs_org_id_resources_defs_def_id_(req)

if res.resource_definition_response is not None:
    # handle response
```

## get_orgs_org_id_resources_defs_def_id_resources

List Active Resources provisioned via a specific Resource Definition.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDResourcesDefsDefIDResourcesRequest(
    def_id='nisi',
    org_id='voluptatibus',
)

res = s.resource_definition.get_orgs_org_id_resources_defs_def_id_resources(req)

if res.active_resource_responses is not None:
    # handle response
```

## patch_orgs_org_id_resources_defs_def_id_

Update a Resource Definition.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PatchOrgsOrgIDResourcesDefsDefIDRequest(
    patch_resource_definition_request_request=shared.PatchResourceDefinitionRequestRequest(
        driver_account='quaerat',
        driver_inputs=shared.ValuesSecretsRequest(
            secrets={
                "distinctio": 'nisi',
                "quis": 'nisi',
                "libero": 'minus',
            },
            values={
                "facilis": 'ipsum',
                "ad": 'voluptatibus',
                "voluptatibus": 'consequuntur',
                "debitis": 'labore',
            },
        ),
        name='Craig Kiehn',
    ),
    def_id='iusto',
    org_id='est',
)

res = s.resource_definition.patch_orgs_org_id_resources_defs_def_id_(req)

if res.resource_definition_response is not None:
    # handle response
```

## post_orgs_org_id_resources_defs

Create a new Resource Definition.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDResourcesDefsRequest(
    create_resource_definition_request_request=shared.CreateResourceDefinitionRequestRequest(
        criteria=[
            shared.MatchingCriteriaRequest(
                app_id='eligendi',
                env_id='fugiat',
                env_type='unde',
                id='e7319c17-7d52-45f7-bb11-4eeb52ff785f',
                res_id='quisquam',
            ),
            shared.MatchingCriteriaRequest(
                app_id='sequi',
                env_id='nihil',
                env_type='deleniti',
                id='14d4c98e-0c2b-4b89-ab75-dad636c60050',
                res_id='amet',
            ),
            shared.MatchingCriteriaRequest(
                app_id='illum',
                env_id='praesentium',
                env_type='quidem',
                id='b31180f7-39ae-49e0-97eb-809e2810331f',
                res_id='dolor',
            ),
        ],
        driver_account='occaecati',
        driver_inputs=shared.ValuesSecretsRequest(
            secrets={
                "beatae": 'at',
                "labore": 'minus',
                "esse": 'voluptatem',
            },
            values={
                "rerum": 'ea',
            },
        ),
        driver_type='aperiam',
        id='7f3c93c7-3b9d-4a3f-aced-a7e23f225741',
        name='May Nolan',
        type='distinctio',
    ),
    org_id='in',
)

res = s.resource_definition.post_orgs_org_id_resources_defs(req)

if res.resource_definition_response is not None:
    # handle response
```

## post_orgs_org_id_resources_defs_def_id_criteria

Matching Criteria are combined with Resource Type to select a specific definition. Matching Criteria can be set for any combination of Application ID, Environment ID, Environment Type, and Resource ID. In the event of multiple matches, the most specific match is chosen.

For example, given 3 sets of matching criteria for the same type:

```
 1. {"env_type":"test"}
 2. {"env_type":"development"}
 3. {"env_type":"test", "app_id":"my-app"}
```

If, a resource of that time was needed in an Application `my-app`, Environment `qa-team` with Type `test` and Resource ID `modules.my-module-externals.my-resource`, there would be two resources definitions matching the criteria: #1 & #3. Definition #3 will be chosen because it's matching criteria is the most specific.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDResourcesDefsDefIDCriteriaRequest(
    matching_criteria_rule_request=shared.MatchingCriteriaRuleRequest(
        app_id='exercitationem',
        env_id='labore',
        env_type='numquam',
        res_id='repudiandae',
    ),
    def_id='modi',
    org_id='in',
)

res = s.resource_definition.post_orgs_org_id_resources_defs_def_id_criteria(req)

if res.matching_criteria_response is not None:
    # handle response
```

## put_orgs_org_id_resources_defs_def_id_

Update a Resource Definition.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PutOrgsOrgIDResourcesDefsDefIDRequest(
    update_resource_definition_request_request=shared.UpdateResourceDefinitionRequestRequest(
        driver_account='explicabo',
        driver_inputs=shared.ValuesSecretsRequest(
            secrets={
                "rem": 'aperiam',
                "odit": 'deleniti',
                "enim": 'voluptate',
                "similique": 'minima',
            },
            values={
                "magnam": 'sit',
                "modi": 'eum',
                "nesciunt": 'mollitia',
            },
        ),
        name='Hope Hegmann',
    ),
    def_id='reiciendis',
    org_id='ab',
)

res = s.resource_definition.put_orgs_org_id_resources_defs_def_id_(req)

if res.resource_definition_response is not None:
    # handle response
```
