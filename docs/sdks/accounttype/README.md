# account_type

## Overview

Resource Account Types define cloud providers or protocols to which a resource account can belong.
<SchemaDefinition schemaRef="#/components/schemas/AccountTypeRequest" />


### Available Operations

* [get_orgs_org_id_resources_account_types](#get_orgs_org_id_resources_account_types) - List Resource Account Types available to the organization.

## get_orgs_org_id_resources_account_types

List Resource Account Types available to the organization.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDResourcesAccountTypesRequest(
    org_id='provident',
)

res = s.account_type.get_orgs_org_id_resources_account_types(req)

if res.account_type_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.GetOrgsOrgIDResourcesAccountTypesRequest](../../models/operations/getorgsorgidresourcesaccounttypesrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.GetOrgsOrgIDResourcesAccountTypesResponse](../../models/operations/getorgsorgidresourcesaccounttypesresponse.md)**

