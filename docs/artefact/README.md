# artefact

## Overview

Artefacts can be registered with Humanitec. Continuous Integration (CI) pipelines notify Humanitec when a new version of an Artefact becomes available. Humanitec tracks the Artefact along with metadata about how it was built.
<SchemaDefinition schemaRef="#/components/schemas/ArtefactRequest" />


### Available Operations

* [delete_orgs_org_id_artefacts_artefact_id_](#delete_orgs_org_id_artefacts_artefact_id_) - Delete Artefact and all related Artefact Versions
* [get_orgs_org_id_artefacts](#get_orgs_org_id_artefacts) - List all Artefacts.

## delete_orgs_org_id_artefacts_artefact_id_

The specified Artefact and its Artefact Versions will be permanently deleted. Only Administrators can delete an Artefact.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.DeleteOrgsOrgIDArtefactsArtefactIDRequest(
    artefact_id='dolores',
    org_id='dolorem',
)

res = s.artefact.delete_orgs_org_id_artefacts_artefact_id_(req)

if res.status_code == 200:
    # handle response
```

## get_orgs_org_id_artefacts

Returns the Artefacts registered with your organization. If no elements are found, an empty list is returned.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDArtefactsRequest(
    name='Rose Rolfson',
    org_id='nemo',
    type='minima',
)

res = s.artefact.get_orgs_org_id_artefacts(req)

if res.artefact_responses is not None:
    # handle response
```
