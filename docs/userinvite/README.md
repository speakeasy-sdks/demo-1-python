# user_invite

### Available Operations

* [get_orgs_org_id_invitations](#get_orgs_org_id_invitations) - List the invites issued for the organization.

## get_orgs_org_id_invitations

List the invites issued for the organization.

### Example Usage

```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDInvitationsRequest(
    org_id='vel',
)

res = s.user_invite.get_orgs_org_id_invitations(req)

if res.user_invite_responses is not None:
    # handle response
```
