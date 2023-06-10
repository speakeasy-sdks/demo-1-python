"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import humanitecerrorresponse as shared_humanitecerrorresponse
from typing import Optional



@dataclasses.dataclass
class DeleteOrgsOrgIDResourcesDriversDriverIDRequest:
    driver_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'driverId', 'style': 'simple', 'explode': False }})
    r"""The Resources Driver ID to delete."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    




@dataclasses.dataclass
class DeleteOrgsOrgIDResourcesDriversDriverIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    humanitec_error_response: Optional[shared_humanitecerrorresponse.HumanitecErrorResponse] = dataclasses.field(default=None)
    r"""Internal application error."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

