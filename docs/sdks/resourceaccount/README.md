# resource_account

## Overview

ResourceAccount represents the account being used to access a resource.

Resource Accounts hold credentials that are required to provision and manage resources.
<SchemaDefinition schemaRef="#/components/schemas/ResourceAccountRequest" />


### Available Operations

* [get_orgs_org_id_resources_accounts](#get_orgs_org_id_resources_accounts) - List Resource Accounts in the organization.
* [get_orgs_org_id_resources_accounts_acc_id_](#get_orgs_org_id_resources_accounts_acc_id_) - Get a Resource Account.
* [patch_orgs_org_id_resources_accounts_acc_id_](#patch_orgs_org_id_resources_accounts_acc_id_) - Update a Resource Account.
* [post_orgs_org_id_resources_accounts](#post_orgs_org_id_resources_accounts) - Create a new Resource Account in the organization.

## get_orgs_org_id_resources_accounts

List Resource Accounts in the organization.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDResourcesAccountsRequest(
    org_id='repudiandae',
)

res = s.resource_account.get_orgs_org_id_resources_accounts(req)

if res.resource_account_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetOrgsOrgIDResourcesAccountsRequest](../../models/operations/getorgsorgidresourcesaccountsrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetOrgsOrgIDResourcesAccountsResponse](../../models/operations/getorgsorgidresourcesaccountsresponse.md)**


## get_orgs_org_id_resources_accounts_acc_id_

Get a Resource Account.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDResourcesAccountsAccIDRequest(
    acc_id='cum',
    org_id='dicta',
)

res = s.resource_account.get_orgs_org_id_resources_accounts_acc_id_(req)

if res.resource_account_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetOrgsOrgIDResourcesAccountsAccIDRequest](../../models/operations/getorgsorgidresourcesaccountsaccidrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetOrgsOrgIDResourcesAccountsAccIDResponse](../../models/operations/getorgsorgidresourcesaccountsaccidresponse.md)**


## patch_orgs_org_id_resources_accounts_acc_id_

Update a Resource Account.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PatchOrgsOrgIDResourcesAccountsAccIDRequest(
    update_resource_account_request_request=shared.UpdateResourceAccountRequestRequest(
        credentials={
            "veniam": 'animi',
            "dolores": 'nam',
            "dicta": 'consequuntur',
            "necessitatibus": 'nobis',
        },
        name='Mr. Dora Wuckert',
    ),
    acc_id='pariatur',
    org_id='libero',
)

res = s.resource_account.patch_orgs_org_id_resources_accounts_acc_id_(req)

if res.resource_account_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.PatchOrgsOrgIDResourcesAccountsAccIDRequest](../../models/operations/patchorgsorgidresourcesaccountsaccidrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.PatchOrgsOrgIDResourcesAccountsAccIDResponse](../../models/operations/patchorgsorgidresourcesaccountsaccidresponse.md)**


## post_orgs_org_id_resources_accounts

Create a new Resource Account in the organization.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDResourcesAccountsRequest(
    create_resource_account_request_request=shared.CreateResourceAccountRequestRequest(
        credentials={
            "occaecati": 'nemo',
            "aliquam": 'nostrum',
            "doloribus": 'eligendi',
        },
        id='95fa8897-0e18-49db-b30f-cb33ea055b19',
        name='Sheri Schuppe',
        type='itaque',
    ),
    org_id='sed',
)

res = s.resource_account.post_orgs_org_id_resources_accounts(req)

if res.resource_account_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PostOrgsOrgIDResourcesAccountsRequest](../../models/operations/postorgsorgidresourcesaccountsrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PostOrgsOrgIDResourcesAccountsResponse](../../models/operations/postorgsorgidresourcesaccountsresponse.md)**

