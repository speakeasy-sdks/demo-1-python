# resource_type

## Overview

Resources Types define the technology that Applications can have dependencies on.

Each Resource Type also defines a set of input parameters (`inputs_schema`), and a set of output data (`outputs_schema`). When provisioning a resource, these are treated as inputs and outputs respectively.
<SchemaDefinition schemaRef="#/components/schemas/ResourceTypeRequest" />


### Available Operations

* [get_orgs_org_id_resources_types](#get_orgs_org_id_resources_types) - List Resource Types.

## get_orgs_org_id_resources_types

List Resource Types.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDResourcesTypesRequest(
    org_id='modi',
)

res = s.resource_type.get_orgs_org_id_resources_types(req)

if res.resource_type_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetOrgsOrgIDResourcesTypesRequest](../../models/operations/getorgsorgidresourcestypesrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetOrgsOrgIDResourcesTypesResponse](../../models/operations/getorgsorgidresourcestypesresponse.md)**

