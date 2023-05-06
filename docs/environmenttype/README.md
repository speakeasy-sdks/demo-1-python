# environment_type

## Overview

Environment Types are a way of grouping and managing Environments. Every Environment has exactly 1 Environment Type.

Environment Types can be used with External Resources to manage where resources such as databases are provisioned or even which cluster to deploy to.
<SchemaDefinition schemaRef="#/components/schemas/EnvironmentTypeRequest" />


### Available Operations

* [delete_orgs_org_id_env_types_env_type_id_](#delete_orgs_org_id_env_types_env_type_id_) - Deletes an Environment Type
* [get_orgs_org_id_env_types](#get_orgs_org_id_env_types) - List all Environment Types
* [get_orgs_org_id_env_types_env_type_id_](#get_orgs_org_id_env_types_env_type_id_) - Get an Environment Type
* [post_orgs_org_id_env_types](#post_orgs_org_id_env_types) - Add a new Environment Type

## delete_orgs_org_id_env_types_env_type_id_

Deletes a specific Environment Type from an Organization. If there are Environments with this Type in the Organization, the operation will fail.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDEnvTypesEnvTypeIDRequest(
    env_type_id='accusamus',
    org_id='impedit',
)

res = s.environment_type.delete_orgs_org_id_env_types_env_type_id_(req)

if res.environment_type_response is not None:
    # handle response
```

## get_orgs_org_id_env_types

Lists all Environment Types in an Organization.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDEnvTypesRequest(
    org_id='hic',
)

res = s.environment_type.get_orgs_org_id_env_types(req)

if res.environment_type_responses is not None:
    # handle response
```

## get_orgs_org_id_env_types_env_type_id_

Gets a specific Environment Type within an Organization.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDEnvTypesEnvTypeIDRequest(
    env_type_id='necessitatibus',
    org_id='asperiores',
)

res = s.environment_type.get_orgs_org_id_env_types_env_type_id_(req)

if res.environment_type_response is not None:
    # handle response
```

## post_orgs_org_id_env_types

Adds a new Environment Type to an Organization.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDEnvTypesRequest(
    environment_type_request=shared.EnvironmentTypeRequest(
        description='ex',
        id='6ef1caa3-383c-42be-b477-373c8d72f64d',
    ),
    org_id='inventore',
)

res = s.environment_type.post_orgs_org_id_env_types(req)

if res.environment_type_response is not None:
    # handle response
```
