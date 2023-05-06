"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import humanitecerrorresponse as shared_humanitecerrorresponse
from ..shared import valuesetversionresponse as shared_valuesetversionresponse
from typing import Optional


@dataclasses.dataclass
class GetOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDRequest:
    
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'appId', 'style': 'simple', 'explode': False }})
    r"""The Application ID."""
    env_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'envId', 'style': 'simple', 'explode': False }})
    r"""The Environment ID."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    value_set_version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'valueSetVersionId', 'style': 'simple', 'explode': False }})
    r"""The ValueSetVersion ID."""
    

@dataclasses.dataclass
class GetOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    humanitec_error_response: Optional[shared_humanitecerrorresponse.HumanitecErrorResponse] = dataclasses.field(default=None)
    r"""ValueSetVersion with `valueSetVersionId` in Environment."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    value_set_version_response: Optional[shared_valuesetversionresponse.ValueSetVersionResponse] = dataclasses.field(default=None)
    r"""The requested ValueSetVersion"""
    