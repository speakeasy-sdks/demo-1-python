"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import userinviteresponse as shared_userinviteresponse
from typing import Optional



@dataclasses.dataclass
class GetOrgsOrgIDInvitationsRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    




@dataclasses.dataclass
class GetOrgsOrgIDInvitationsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    user_invite_responses: Optional[list[shared_userinviteresponse.UserInviteResponse]] = dataclasses.field(default=None)
    r"""The list of the invites issued for the organization."""
    

