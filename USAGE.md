<!-- Start SDK Example Usage -->
```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDResourcesAccountTypesRequest(
    org_id='corrupti',
)

res = s.account_type.get_orgs_org_id_resources_account_types(req)

if res.account_type_responses is not None:
    # handle response
```
<!-- End SDK Example Usage -->