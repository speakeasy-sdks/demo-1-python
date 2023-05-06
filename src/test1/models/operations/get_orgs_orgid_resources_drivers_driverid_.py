"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import driverdefinitionresponse as shared_driverdefinitionresponse
from ..shared import humanitecerrorresponse as shared_humanitecerrorresponse
from typing import Optional


@dataclasses.dataclass
class GetOrgsOrgIDResourcesDriversDriverIDRequest:
    
    driver_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'driverId', 'style': 'simple', 'explode': False }})
    r"""The Resource Driver ID."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    

@dataclasses.dataclass
class GetOrgsOrgIDResourcesDriversDriverIDResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    driver_definition_response: Optional[shared_driverdefinitionresponse.DriverDefinitionResponse] = dataclasses.field(default=None)
    r"""The requested Resources Driver details."""
    humanitec_error_response: Optional[shared_humanitecerrorresponse.HumanitecErrorResponse] = dataclasses.field(default=None)
    r"""A Resource Driver with the 'driverId' ID is not found or is not accessible by the organization."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    