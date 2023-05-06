# organization

## Overview

An Organization is the top level object in Humanitec. All other objects belong to an Organization.
<SchemaDefinition schemaRef="#/components/schemas/OrganizationRequest" />


### Available Operations

* [get_orgs](#get_orgs) - List active organizations the user has access to.
* [get_orgs_org_id_](#get_orgs_org_id_) - Get the specified Organization.

## get_orgs

List active organizations the user has access to.

### Example Usage

```python
import test_1


s = test_1.Test1()


res = s.organization.get_orgs()

if res.organization_responses is not None:
    # handle response
```

## get_orgs_org_id_

Get the specified Organization.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDRequest(
    org_id='cum',
)

res = s.organization.get_orgs_org_id_(req)

if res.organization_response is not None:
    # handle response
```
