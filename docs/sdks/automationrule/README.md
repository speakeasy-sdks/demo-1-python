# automation_rule

## Overview

An Automation Rule defining how and when artefacts in an environment should be updated.
<SchemaDefinition schemaRef="#/components/schemas/AutomationRuleRequest" />


### Available Operations

* [delete_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_](#delete_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_) - Delete Automation Rule from an Environment.
* [get_orgs_org_id_apps_app_id_envs_env_id_rules](#get_orgs_org_id_apps_app_id_envs_env_id_rules) - List all Automation Rules in an Environment.
* [get_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_](#get_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_) - Get a specific Automation Rule for an Environment.
* [post_orgs_org_id_apps_app_id_envs_env_id_rules](#post_orgs_org_id_apps_app_id_envs_env_id_rules) - Create a new Automation Rule for an Environment.
* [put_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_](#put_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_) - Update an existing Automation Rule for an Environment.

## delete_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_

Delete Automation Rule from an Environment.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDRequest(
    app_id='ipsam',
    env_id='id',
    org_id='possimus',
    rule_id='aut',
)

res = s.automation_rule.delete_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDRequest](../../models/operations/deleteorgsorgidappsappidenvsenvidrulesruleidrequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDResponse](../../models/operations/deleteorgsorgidappsappidenvsenvidrulesruleidresponse.md)**


## get_orgs_org_id_apps_app_id_envs_env_id_rules

List all Automation Rules in an Environment.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRulesRequest(
    app_id='quasi',
    env_id='error',
    org_id='temporibus',
)

res = s.automation_rule.get_orgs_org_id_apps_app_id_envs_env_id_rules(req)

if res.automation_rule_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRulesRequest](../../models/operations/getorgsorgidappsappidenvsenvidrulesrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRulesResponse](../../models/operations/getorgsorgidappsappidenvsenvidrulesresponse.md)**


## get_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_

Get a specific Automation Rule for an Environment.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDRequest(
    app_id='laborum',
    env_id='quasi',
    org_id='reiciendis',
    rule_id='voluptatibus',
)

res = s.automation_rule.get_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_(req)

if res.automation_rule_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDRequest](../../models/operations/getorgsorgidappsappidenvsenvidrulesruleidrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDResponse](../../models/operations/getorgsorgidappsappidenvsenvidrulesruleidresponse.md)**


## post_orgs_org_id_apps_app_id_envs_env_id_rules

Items marked as deprecated are still supported (however not recommended) for use and are incompatible with properties of the latest api version. In particular an error is raised if  `images_filter` (deprecated) and `artefacts_filter` are used in the same payload. The same is true for `exclude_images_filter` (deprecated) and `exclude_artefacts_filter`. `match` and `update_to` are still supported but will trigger an error if combined with `match_ref`.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDRulesRequest(
    automation_rule_request=shared.AutomationRuleRequest(
        active=False,
        artefacts_filter=[
            'nihil',
            'praesentium',
            'voluptatibus',
            'ipsa',
        ],
        exclude_artefacts_filter=False,
        exclude_images_filter=False,
        images_filter=[
            'voluptate',
            'cum',
            'perferendis',
        ],
        match='doloremque',
        match_ref='reprehenderit',
        type='ut',
        update_to='maiores',
    ),
    app_id='dicta',
    env_id='corporis',
    org_id='dolore',
)

res = s.automation_rule.post_orgs_org_id_apps_app_id_envs_env_id_rules(req)

if res.automation_rule_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDRulesRequest](../../models/operations/postorgsorgidappsappidenvsenvidrulesrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDRulesResponse](../../models/operations/postorgsorgidappsappidenvsenvidrulesresponse.md)**


## put_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_

Items marked as deprecated are still supported (however not recommended) for use and are incompatible with properties of the latest api version. In particular an error is raised if  `images_filter` (deprecated) and `artefacts_filter` are used in the same payload. The same is true for `exclude_images_filter` (deprecated) and `exclude_artefacts_filter`. `match` and `update_to` are still supported but will trigger an error if combined with `match_ref`.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDRequest(
    automation_rule_request=shared.AutomationRuleRequest(
        active=False,
        artefacts_filter=[
            'dicta',
            'harum',
        ],
        exclude_artefacts_filter=False,
        exclude_images_filter=False,
        images_filter=[
            'accusamus',
            'commodi',
        ],
        match='repudiandae',
        match_ref='quae',
        type='ipsum',
        update_to='quidem',
    ),
    app_id='molestias',
    env_id='excepturi',
    org_id='pariatur',
    rule_id='modi',
)

res = s.automation_rule.put_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_(req)

if res.automation_rule_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDRequest](../../models/operations/putorgsorgidappsappidenvsenvidrulesruleidrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDResponse](../../models/operations/putorgsorgidappsappidenvsenvidrulesruleidresponse.md)**

