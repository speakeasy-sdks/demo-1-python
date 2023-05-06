"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import humanitecerrorresponse as shared_humanitecerrorresponse
from ..shared import rolerequest as shared_rolerequest
from ..shared import userroleresponse as shared_userroleresponse
from typing import Optional


@dataclasses.dataclass
class PatchOrgsOrgIDEnvTypesEnvTypeUsersUserIDRequest:
    
    env_type: str = dataclasses.field(metadata={'path_param': { 'field_name': 'envType', 'style': 'simple', 'explode': False }})
    r"""The Environment Type."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    role_request: shared_rolerequest.RoleRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""The new user role"""
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    r"""The User ID"""
    

@dataclasses.dataclass
class PatchOrgsOrgIDEnvTypesEnvTypeUsersUserIDResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    humanitec_error_response: Optional[shared_humanitecerrorresponse.HumanitecErrorResponse] = dataclasses.field(default=None)
    r"""The request was invalid or the payload malformed."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    user_role_response: Optional[shared_userroleresponse.UserRoleResponse] = dataclasses.field(default=None)
    r"""The information on the user."""
    