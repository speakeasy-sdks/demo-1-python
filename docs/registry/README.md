# registry

## Overview

Humanitec can be used to manage registry credentials. The Registry object represents how to match credentials to a particular registry.

Humanitec supports all Docker compatible registries as well as the custom authentication formats used by AWS Elastic Container Registry and Google Container Registry. It also supports the injection of a specific secret to be copied from an existing namespace in the cluster.
<SchemaDefinition schemaRef="#/components/schemas/RegistryRequest" />


### Available Operations

* [delete_orgs_org_id_registries_reg_id_](#delete_orgs_org_id_registries_reg_id_) - Deletes an existing registry record and all associated credentials and secrets.
* [get_orgs_org_id_registries](#get_orgs_org_id_registries) - Lists available registries for the organization.
* [get_orgs_org_id_registries_reg_id_](#get_orgs_org_id_registries_reg_id_) - Loads a registry record details.
* [get_orgs_org_id_registries_reg_id_creds](#get_orgs_org_id_registries_reg_id_creds) - Returns current account credentials or secret details for the registry.
* [patch_orgs_org_id_registries_reg_id_](#patch_orgs_org_id_registries_reg_id_) - Updates (patches) an existing registry record.
* [post_orgs_org_id_registries](#post_orgs_org_id_registries) - Creates a new registry record.

## delete_orgs_org_id_registries_reg_id_

_Deletions are currently irreversible._

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDRegistriesRegIDRequest(
    org_id='at',
    reg_id='alias',
)

res = s.registry.delete_orgs_org_id_registries_reg_id_(req)

if res.status_code == 200:
    # handle response
```

## get_orgs_org_id_registries

Lists available registries for the organization.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDRegistriesRequest(
    org_id='quia',
)

res = s.registry.get_orgs_org_id_registries(req)

if res.registry_responses is not None:
    # handle response
```

## get_orgs_org_id_registries_reg_id_

Loads a registry record details.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDRegistriesRegIDRequest(
    org_id='quidem',
    reg_id='fuga',
)

res = s.registry.get_orgs_org_id_registries_reg_id_(req)

if res.registry_response is not None:
    # handle response
```

## get_orgs_org_id_registries_reg_id_creds

Returns current account credentials or secret details for the registry.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDRegistriesRegIDCredsRequest(
    org_id='repudiandae',
    reg_id='accusantium',
)

res = s.registry.get_orgs_org_id_registries_reg_id_creds(req)

if res.registry_creds_response is not None:
    # handle response
```

## patch_orgs_org_id_registries_reg_id_

Updates (patches) an existing registry record.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PatchOrgsOrgIDRegistriesRegIDRequest(
    registry_request=shared.RegistryRequest(
        creds=shared.AccountCredsRequest(
            expires='2020-06-22T09:37:23.523Z',
            password='expedita',
            username='Shea.Dare51',
        ),
        enable_ci=False,
        id='2259e3ea-4b51-497f-9244-3da7ce52b895',
        registry='placeat',
        secrets={
            "neque": shared.ClusterSecretRequest(
                namespace='in',
                secret='minus',
            ),
            "eum": shared.ClusterSecretRequest(
                namespace='modi',
                secret='corporis',
            ),
        },
        type='magnam',
    ),
    org_id='voluptates',
    reg_id='maiores',
)

res = s.registry.patch_orgs_org_id_registries_reg_id_(req)

if res.registry_response is not None:
    # handle response
```

## post_orgs_org_id_registries

Creates a new registry record.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDRegistriesRequest(
    registry_request=shared.RegistryRequest(
        creds=shared.AccountCredsRequest(
            expires='2020-06-22T09:37:23.523Z',
            password='tempore',
            username='Alvis28',
        ),
        enable_ci=False,
        id='896c3ca5-acfb-4e2f-9570-7577929177de',
        registry='similique',
        secrets={
            "ex": shared.ClusterSecretRequest(
                namespace='quaerat',
                secret='commodi',
            ),
            "officiis": shared.ClusterSecretRequest(
                namespace='placeat',
                secret='quidem',
            ),
            "exercitationem": shared.ClusterSecretRequest(
                namespace='quam',
                secret='dolorem',
            ),
            "modi": shared.ClusterSecretRequest(
                namespace='ipsa',
                secret='sint',
            ),
        },
        type='vero',
    ),
    org_id='sequi',
)

res = s.registry.post_orgs_org_id_registries(req)

if res.registry_response is not None:
    # handle response
```
