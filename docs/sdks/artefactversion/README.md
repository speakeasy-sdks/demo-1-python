# artefact_version

## Overview

An Artefact Version represents a particular version of an Artefact that can be added to an Application.
<SchemaDefinition schemaRef="#/components/schemas/ArtefactVersionRequest" />


### Available Operations

* [get_orgs_org_id_artefact_versions](#get_orgs_org_id_artefact_versions) - List all Artefacts Versions.
* [get_orgs_org_id_artefact_versions_artefact_version_id_](#get_orgs_org_id_artefact_versions_artefact_version_id_) - Get an Artefacts Versions.
* [get_orgs_org_id_artefacts_artefact_id_versions](#get_orgs_org_id_artefacts_artefact_id_versions) - List all Artefact Versions of an Artefact.
* [patch_orgs_org_id_artefacts_artefact_id_versions_version_id_](#patch_orgs_org_id_artefacts_artefact_id_versions_version_id_) - Update Version of an Artefact.
* [post_orgs_org_id_artefact_versions](#post_orgs_org_id_artefact_versions) - Register a new Artefact Version with your organization.

## get_orgs_org_id_artefact_versions

Returns the Artefact Versions registered with your organization. If no elements are found, an empty list is returned.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDArtefactVersionsRequest(
    archived='excepturi',
    name='Charlene Nicolas',
    org_id='architecto',
    reference='mollitia',
)

res = s.artefact_version.get_orgs_org_id_artefact_versions(req)

if res.artefact_version_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetOrgsOrgIDArtefactVersionsRequest](../../models/operations/getorgsorgidartefactversionsrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetOrgsOrgIDArtefactVersionsResponse](../../models/operations/getorgsorgidartefactversionsresponse.md)**


## get_orgs_org_id_artefact_versions_artefact_version_id_

Returns a specific Artefact Version.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDArtefactVersionsArtefactVersionIDRequest(
    artefact_version_id='dolorem',
    org_id='culpa',
)

res = s.artefact_version.get_orgs_org_id_artefact_versions_artefact_version_id_(req)

if res.artefact_version_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                          | [operations.GetOrgsOrgIDArtefactVersionsArtefactVersionIDRequest](../../models/operations/getorgsorgidartefactversionsartefactversionidrequest.md) | :heavy_check_mark:                                                                                                                                 | The request object to use for the request.                                                                                                         |


### Response

**[operations.GetOrgsOrgIDArtefactVersionsArtefactVersionIDResponse](../../models/operations/getorgsorgidartefactversionsartefactversionidresponse.md)**


## get_orgs_org_id_artefacts_artefact_id_versions

Returns the Artefact Versions of a specified Artefact registered with your organization. If no elements are found, an empty list is returned.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDArtefactsArtefactIDVersionsRequest(
    archived='consequuntur',
    artefact_id='repellat',
    limit='mollitia',
    org_id='occaecati',
    reference='numquam',
)

res = s.artefact_version.get_orgs_org_id_artefacts_artefact_id_versions(req)

if res.artefact_version_responses is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.GetOrgsOrgIDArtefactsArtefactIDVersionsRequest](../../models/operations/getorgsorgidartefactsartefactidversionsrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.GetOrgsOrgIDArtefactsArtefactIDVersionsResponse](../../models/operations/getorgsorgidartefactsartefactidversionsresponse.md)**


## patch_orgs_org_id_artefacts_artefact_id_versions_version_id_

Update the version of a specified Artefact registered with your organization".

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PatchOrgsOrgIDArtefactsArtefactIDVersionsVersionIDRequest(
    update_artefact_version_payload_request=shared.UpdateArtefactVersionPayloadRequest(
        archived=False,
    ),
    artefact_id='commodi',
    org_id='quam',
    version_id='molestiae',
)

res = s.artefact_version.patch_orgs_org_id_artefacts_artefact_id_versions_version_id_(req)

if res.artefact_version_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                    | [operations.PatchOrgsOrgIDArtefactsArtefactIDVersionsVersionIDRequest](../../models/operations/patchorgsorgidartefactsartefactidversionsversionidrequest.md) | :heavy_check_mark:                                                                                                                                           | The request object to use for the request.                                                                                                                   |


### Response

**[operations.PatchOrgsOrgIDArtefactsArtefactIDVersionsVersionIDResponse](../../models/operations/patchorgsorgidartefactsartefactidversionsversionidresponse.md)**


## post_orgs_org_id_artefact_versions

Register a new Artefact Version with your organization.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDArtefactVersionsRequest(
    add_artefact_version_payload_request=shared.AddArtefactVersionPayloadRequest(
        commit='velit',
        digest='error',
        name='Beatrice Brown',
        ref='enim',
        type='odit',
        version='quo',
    ),
    org_id='sequi',
    vcs='tenetur',
)

res = s.artefact_version.post_orgs_org_id_artefact_versions(req)

if res.artefact_version_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PostOrgsOrgIDArtefactVersionsRequest](../../models/operations/postorgsorgidartefactversionsrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PostOrgsOrgIDArtefactVersionsResponse](../../models/operations/postorgsorgidartefactversionsresponse.md)**

