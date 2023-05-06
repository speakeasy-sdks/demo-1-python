# matching_criteria

## Overview

Matching Criteria are a set of rules used to choose which Resource Definition to use to provision a particular Resource Type.

Matching criteria are made up in order of specificity with least specific first:

- Environment Type (`env_type`)

- Application (`app_id`)

- Environment (`env_id`)

- Resource (`res_id`)

When selecting matching criteria, the most specific one is selected. In general, this means of all the Matching Criteria fully matching the context, the Matching Criteria Rule with the most specific element filled is chosen. If there is a tie, the next most specific elements are compared and so on until one is chosen.

**NOTE:**

Humanitec will reject the registration of matching criteria rules that duplicate rules already present for a Resource Type.
<SchemaDefinition schemaRef="#/components/schemas/MatchingCriteriaRequest" />


### Available Operations

* [delete_orgs_org_id_resources_defs_def_id_criteria_criteria_id_](#delete_orgs_org_id_resources_defs_def_id_criteria_criteria_id_) - Delete a Matching Criteria from a Resource Definition.
* [post_orgs_org_id_resources_defs_def_id_criteria](#post_orgs_org_id_resources_defs_def_id_criteria) - Add a new Matching Criteria to a Resource Definition.

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
    criteria_id='sint',
    def_id='ea',
    force=False,
    org_id='autem',
)

res = s.matching_criteria.delete_orgs_org_id_resources_defs_def_id_criteria_criteria_id_(req)

if res.status_code == 200:
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
        app_id='ipsam',
        env_id='rerum',
        env_type='laudantium',
        res_id='corporis',
    ),
    def_id='officiis',
    org_id='voluptatibus',
)

res = s.matching_criteria.post_orgs_org_id_resources_defs_def_id_criteria(req)

if res.matching_criteria_response is not None:
    # handle response
```
