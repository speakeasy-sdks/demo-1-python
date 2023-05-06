# value_set_version

## Overview

A Value Set Version can be used as a track record of Shared Values changes, to restore a previous version of a Shared Value or Value Set, or to purge a Shared Value if it shouldn't be accessible anymore.
<SchemaDefinition schemaRef="#/components/schemas/ValueSetVersionResponse" />


### Available Operations

* [get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions](#get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions) - List Value Set Versions in an Environment of an App
* [get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_](#get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_) - Get a single Value Set Version in an Environment of an App
* [get_orgs_org_id_apps_app_id_value_set_versions](#get_orgs_org_id_apps_app_id_value_set_versions) - List Value Set Versions in the App
* [get_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_](#get_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_) - Get a single Value Set Version from the App
* [post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_purge_key_](#post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_purge_key_) - Purge the value of a specific Shared Value from the App Environment Version history.
* [post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore](#post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore) - Restore a Value Set Version in an Environment of an App
* [post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore_key_](#post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore_key_) - Restore a specific key from the Value Set Version in an Environment of an App
* [post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_purge_key_](#post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_purge_key_) - Purge the value of a specific Shared Value from the App Version history.
* [post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore](#post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore) - Restore a Value Set Version in an App
* [post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore_key_](#post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore_key_) - Restore a specific key from the Value Set Version in an App

## get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions

A new Value Set Version is created on every modification of a Value inside the an Environment of an App. In case this environment has no overrides the response is the same as the App level endpoint.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsRequest(
    app_id='nihil',
    env_id='tenetur',
    key_changed='sapiente',
    org_id='velit',
)

res = s.value_set_version.get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions(req)

if res.value_set_version_responses is not None:
    # handle response
```

## get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_

Get a single Value Set Version in an Environment of an App

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDRequest(
    app_id='adipisci',
    env_id='non',
    org_id='optio',
    value_set_version_id='ddf857a9-e618-476c-aab2-1d29dfc94d6f',
)

res = s.value_set_version.get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_(req)

if res.value_set_version_response is not None:
    # handle response
```

## get_orgs_org_id_apps_app_id_value_set_versions

A new Value Set Version is created on every modification of a Value inside the app.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDValueSetVersionsRequest(
    app_id='recusandae',
    key_changed='quisquam',
    org_id='facere',
)

res = s.value_set_version.get_orgs_org_id_apps_app_id_value_set_versions(req)

if res.value_set_version_responses is not None:
    # handle response
```

## get_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_

Get a single Value Set Version from the App

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDRequest(
    app_id='dignissimos',
    org_id='iste',
    value_set_version_id='9390066a-6d2d-4000-b553-38cec086fa21',
)

res = s.value_set_version.get_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_(req)

if res.value_set_version_response is not None:
    # handle response
```

## post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_purge_key_

Purging permanently removes the value of a specific Shared Value in an application. A purged value is no longer accessible, can't be restored and can't be used
by deployments referencing a Value Set Version where the value was present.

Learn more about purging in our [docs](https://docs.humanitec.com/reference/concepts/app-config/shared-app-values#purge).


### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDPurgeKeyRequest(
    value_set_action_payload_request=shared.ValueSetActionPayloadRequest(
        comment='necessitatibus',
    ),
    app_id='iste',
    env_id='dicta',
    key='ipsam',
    org_id='consequuntur',
    value_set_version_id='cb311916-7b8e-43c8-9b03-408d6d364ffd',
)

res = s.value_set_version.post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_purge_key_(req)

if res.status_code == 200:
    # handle response
```

## post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore

Restore the values of all Shared Values in an environment from a specific version. Keys not existing in the selected version are deleted.

Learn more about reverting in our [docs](https://docs.humanitec.com/reference/concepts/app-config/shared-app-values#revert).


### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDRestoreRequest(
    value_set_action_payload_request=shared.ValueSetActionPayloadRequest(
        comment='dolore',
    ),
    app_id='enim',
    env_id='ullam',
    org_id='perspiciatis',
    value_set_version_id='06d1263d-48e9-435c-ac9e-81f30be3e432',
)

res = s.value_set_version.post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore(req)

if res.value_set_version_response is not None:
    # handle response
```

## post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore_key_

Restore the values of a single Shared Value in an Environment from a specific version.

Learn more about reverting in our [docs](https://docs.humanitec.com/reference/concepts/app-config/shared-app-values#revert).


### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDRestoreKeyRequest(
    value_set_action_payload_request=shared.ValueSetActionPayloadRequest(
        comment='aperiam',
    ),
    app_id='dolores',
    env_id='illum',
    key='iusto',
    org_id='magni',
    value_set_version_id='16576506-6418-470d-9d21-f9ad030c4ecc',
)

res = s.value_set_version.post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore_key_(req)

if res.value_set_version_response is not None:
    # handle response
```

## post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_purge_key_

Purging permanently removes the value of a specific Shared Value in an Application. A purged value is no longer accessible, can't be restored and can't be used
by deployments referencing a Value Set Version where the value was present.

Learn more about purging in our [docs](https://docs.humanitec.com/reference/concepts/app-config/shared-app-values#purge).


### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDPurgeKeyRequest(
    value_set_action_payload_request=shared.ValueSetActionPayloadRequest(
        comment='et',
    ),
    app_id='beatae',
    key='id',
    org_id='consequatur',
    value_set_version_id='83642906-8b85-402a-95e7-f73bc845e320',
)

res = s.value_set_version.post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_purge_key_(req)

if res.status_code == 200:
    # handle response
```

## post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore

Restore the values of all Shared Values in an application from a specific version. Keys not existing in the selected version are deleted.

Learn more about reverting in our [docs](https://docs.humanitec.com/reference/concepts/app-config/shared-app-values#revert).


### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDRestoreRequest(
    value_set_action_payload_request=shared.ValueSetActionPayloadRequest(
        comment='est',
    ),
    app_id='amet',
    org_id='veritatis',
    value_set_version_id='9f4badf9-47c9-4a86-bbc4-2426665816dd',
)

res = s.value_set_version.post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore(req)

if res.value_set_version_response is not None:
    # handle response
```

## post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore_key_

Restore the values of a single Shared Value in an application from a specific version.

Learn more about reverting in our [docs](https://docs.humanitec.com/reference/concepts/app-config/shared-app-values#revert).


### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDRestoreKeyRequest(
    value_set_action_payload_request=shared.ValueSetActionPayloadRequest(
        comment='impedit',
    ),
    app_id='culpa',
    key='atque',
    org_id='voluptates',
    value_set_version_id='f51fcb4c-593e-4c12-8daa-d0ec7afedbd8',
)

res = s.value_set_version.post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore_key_(req)

if res.value_set_version_response is not None:
    # handle response
```
