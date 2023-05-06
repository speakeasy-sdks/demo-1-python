# workload_profile

## Overview

Workload Profiles provide the baseline configuration for Workloads in Applications in Humanitec. Developers can configure various features of a workload profile to suit their needs. Examples of features might be `schedules` used in Kubernetes CronJobs or `ingress` which might be used to expose Pods controlled by a Kubernetes Deployment.

Workloads in Humanitec are implemented as Helm Charts which must implement a specific schema.
<SchemaDefinition schemaRef="#/components/schemas/WorkloadProfileRequest" />


### Available Operations

* [delete_orgs_org_id_workload_profiles_profile_id_versions_version_](#delete_orgs_org_id_workload_profiles_profile_id_versions_version_) - Delete a Workload Profile Version
* [delete_orgs_org_id_workload_profiles_profile_qid_](#delete_orgs_org_id_workload_profiles_profile_qid_) - Delete a Workload Profile
* [get_orgs_org_id_workload_profiles](#get_orgs_org_id_workload_profiles) - List workload profiles available to the organization.
* [get_orgs_org_id_workload_profiles_profile_qid_](#get_orgs_org_id_workload_profiles_profile_qid_) - Get a Workload Profile
* [get_orgs_org_id_workload_profiles_profile_qid_versions](#get_orgs_org_id_workload_profiles_profile_qid_versions) - List versions of the given workload profile with optional constraint.
* [post_orgs_org_id_workload_profiles](#post_orgs_org_id_workload_profiles) - Create new Workload Profile
* [post_orgs_org_id_workload_profiles_profile_qid_versions](#post_orgs_org_id_workload_profiles_profile_qid_versions) - Add new Version of the Workload Profile

## delete_orgs_org_id_workload_profiles_profile_id_versions_version_

Delete a Workload Profile Version

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDWorkloadProfilesProfileIDVersionsVersionRequest(
    org_id='aut',
    profile_id='temporibus',
    version='tenetur',
)

res = s.workload_profile.delete_orgs_org_id_workload_profiles_profile_id_versions_version_(req)

if res.status_code == 200:
    # handle response
```

## delete_orgs_org_id_workload_profiles_profile_qid_

This will also delete all versions of a workload profile.

It is not possible to delete profiles of other organizations.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDWorkloadProfilesProfileQidRequest(
    org_id='incidunt',
    profile_qid='numquam',
)

res = s.workload_profile.delete_orgs_org_id_workload_profiles_profile_qid_(req)

if res.status_code == 200:
    # handle response
```

## get_orgs_org_id_workload_profiles

List workload profiles available to the organization.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDWorkloadProfilesRequest(
    org_id='corrupti',
)

res = s.workload_profile.get_orgs_org_id_workload_profiles(req)

if res.workload_profile_responses is not None:
    # handle response
```

## get_orgs_org_id_workload_profiles_profile_qid_

Get a Workload Profile

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDWorkloadProfilesProfileQidRequest(
    org_id='similique',
    profile_qid='dolore',
)

res = s.workload_profile.get_orgs_org_id_workload_profiles_profile_qid_(req)

if res.workload_profile_response is not None:
    # handle response
```

## get_orgs_org_id_workload_profiles_profile_qid_versions

List versions of the given workload profile with optional constraint.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDWorkloadProfilesProfileQidVersionsRequest(
    org_id='esse',
    profile_qid='reiciendis',
    version='iste',
)

res = s.workload_profile.get_orgs_org_id_workload_profiles_profile_qid_versions(req)

if res.workload_profile_version_responses is not None:
    # handle response
```

## post_orgs_org_id_workload_profiles

Create new Workload Profile

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDWorkloadProfilesRequest(
    workload_profile_request=shared.WorkloadProfileRequest(
        id='390c5888-0983-4dab-b9ef-3ffdd9f7f079',
    ),
    org_id='similique',
)

res = s.workload_profile.post_orgs_org_id_workload_profiles(req)

if res.workload_profile_response is not None:
    # handle response
```

## post_orgs_org_id_workload_profiles_profile_qid_versions

Creates a Workload Profile Version from the uploaded Helm chart. The version is retrieved from the chart's metadata (Charts.yaml file).

The request has content type `multipart/form-data` and the request body includes two parts:

1. `file` with `application/x-gzip` content type which is an archive containing a Helm chart.

2. `metadata` with `application/json` content type which defines the version's metadata.

Request body example:

	Content-Type: multipart/form-data; boundary=----boundary 	----boundary 	Content-Disposition: form-data; name="metadata" 	Content-Type: application/json; charset=UTF-8 	{ 	  "features": { 	     "humanitec/service": {}, 	     "humanitec/volumes": {}, 	     "custom": {"schema": {}} 	  }, 	  "notes": "Notes related to this version of the profile" 	} 	----boundary 	Content-Disposition: form-data; name="file"; filename="my-workload-1.0.1.tgz" 	Content-Type: application/x-gzip 	[TGZ_DATA] 	----boundary

**NOTE:**

A Workload Profile must be created before a version can be added to it.

### Example Usage

```python
import test_1
from test_1.models import operations, shared

s = test_1.Test1()

req = operations.PostOrgsOrgIDWorkloadProfilesProfileQidVersionsRequest(
    request_body=operations.PostOrgsOrgIDWorkloadProfilesProfileQidVersionsRequestBody(
        file=operations.PostOrgsOrgIDWorkloadProfilesProfileQidVersionsRequestBodyFile(
            content='asperiores'.encode(),
            file='modi',
        ),
        metadata=shared.WorkloadProfileVersionRequest(
            features={
                "neque": 'quis',
                "in": 'sed',
                "non": 'porro',
                "fugiat": 'soluta',
            },
            notes='ipsa',
        ),
    ),
    org_id='reiciendis',
    profile_qid='labore',
)

res = s.workload_profile.post_orgs_org_id_workload_profiles_profile_qid_versions(req)

if res.workload_profile_version_response is not None:
    # handle response
```
