# driver_definition

## Overview

DriverDefinition describes the resource driver.

Resource Drivers are code that fulfils the Humanitec Resource Driver Interface. This interface allows for certain actions to be performed on resources such as creation and destruction. Humanitec provides numerous Resource Drivers “out of the box”. It is also possible to use 3rd party Resource Drivers or write your own.
<SchemaDefinition schemaRef="#/components/schemas/DriverDefinitionRequest" />


### Available Operations

* [delete_orgs_org_id_resources_drivers_driver_id_](#delete_orgs_org_id_resources_drivers_driver_id_) - Delete a Resources Driver.
* [get_orgs_org_id_resources_drivers](#get_orgs_org_id_resources_drivers) - List Resource Drivers.
* [get_orgs_org_id_resources_drivers_driver_id_](#get_orgs_org_id_resources_drivers_driver_id_) - Get a Resource Driver.
* [post_orgs_org_id_resources_drivers](#post_orgs_org_id_resources_drivers) - Register a new Resource Driver.
* [put_orgs_org_id_resources_drivers_driver_id_](#put_orgs_org_id_resources_drivers_driver_id_) - Update a Resource Driver.

## delete_orgs_org_id_resources_drivers_driver_id_

Delete a Resources Driver.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDResourcesDriversDriverIDRequest(
    driver_id='architecto',
    org_id='sit',
)

res = s.driver_definition.delete_orgs_org_id_resources_drivers_driver_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.DeleteOrgsOrgIDResourcesDriversDriverIDRequest](../../models/operations/deleteorgsorgidresourcesdriversdriveridrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.DeleteOrgsOrgIDResourcesDriversDriverIDResponse](../../models/operations/deleteorgsorgidresourcesdriversdriveridresponse.md)**


## get_orgs_org_id_resources_drivers

List Resource Drivers.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDResourcesDriversRequest(
    org_id='modi',
)

res = s.driver_definition.get_orgs_org_id_resources_drivers(req)

if res.driver_definition_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetOrgsOrgIDResourcesDriversRequest](../../models/operations/getorgsorgidresourcesdriversrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetOrgsOrgIDResourcesDriversResponse](../../models/operations/getorgsorgidresourcesdriversresponse.md)**


## get_orgs_org_id_resources_drivers_driver_id_

# Only drivers that belongs to the given organization or registered as `public` are accessible through this endpoint

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDResourcesDriversDriverIDRequest(
    driver_id='fugit',
    org_id='ab',
)

res = s.driver_definition.get_orgs_org_id_resources_drivers_driver_id_(req)

if res.driver_definition_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.GetOrgsOrgIDResourcesDriversDriverIDRequest](../../models/operations/getorgsorgidresourcesdriversdriveridrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.GetOrgsOrgIDResourcesDriversDriverIDResponse](../../models/operations/getorgsorgidresourcesdriversdriveridresponse.md)**


## post_orgs_org_id_resources_drivers

Register a new Resource Driver.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDResourcesDriversRequest(
    create_driver_request_request=shared.CreateDriverRequestRequest(
        account_types=[
            'quae',
            'dolor',
            'fugiat',
        ],
        id='5208ece7-e253-4b66-8451-c6c6e205e16d',
        inputs_schema={
            "est": 'harum',
            "sequi": 'doloribus',
            "repudiandae": 'optio',
            "occaecati": 'nemo',
        },
        is_public=False,
        target='voluptate',
        template='blanditiis',
        type='officia',
    ),
    org_id='voluptas',
)

res = s.driver_definition.post_orgs_org_id_resources_drivers(req)

if res.driver_definition_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PostOrgsOrgIDResourcesDriversRequest](../../models/operations/postorgsorgidresourcesdriversrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PostOrgsOrgIDResourcesDriversResponse](../../models/operations/postorgsorgidresourcesdriversresponse.md)**


## put_orgs_org_id_resources_drivers_driver_id_

Update a Resource Driver.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PutOrgsOrgIDResourcesDriversDriverIDRequest(
    update_driver_request_request=shared.UpdateDriverRequestRequest(
        account_types=[
            'nemo',
            'quos',
        ],
        inputs_schema={
            "aspernatur": 'ducimus',
            "nesciunt": 'fuga',
        },
        is_public=False,
        target='laudantium',
        template='incidunt',
        type='quasi',
    ),
    driver_id='rem',
    org_id='fugiat',
)

res = s.driver_definition.put_orgs_org_id_resources_drivers_driver_id_(req)

if res.driver_definition_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.PutOrgsOrgIDResourcesDriversDriverIDRequest](../../models/operations/putorgsorgidresourcesdriversdriveridrequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.PutOrgsOrgIDResourcesDriversDriverIDResponse](../../models/operations/putorgsorgidresourcesdriversdriveridresponse.md)**

