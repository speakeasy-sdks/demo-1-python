"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import activeresourceresponse as shared_activeresourceresponse
from ..shared import humanitecerrorresponse as shared_humanitecerrorresponse
from typing import Optional


@dataclasses.dataclass
class GetOrgsOrgIDAppsAppIDEnvsEnvIDResourcesRequest:
    
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'appId', 'style': 'simple', 'explode': False }})
    r"""The Application ID."""
    env_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'envId', 'style': 'simple', 'explode': False }})
    r"""The Environment ID."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    

@dataclasses.dataclass
class GetOrgsOrgIDAppsAppIDEnvsEnvIDResourcesResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    active_resource_responses: Optional[list[shared_activeresourceresponse.ActiveResourceResponse]] = dataclasses.field(default=None)
    r"""A possibly empty list of Active Resources."""
    humanitec_error_response: Optional[shared_humanitecerrorresponse.HumanitecErrorResponse] = dataclasses.field(default=None)
    r"""Internal application error."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    