"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import driverdefinitionresponse as shared_driverdefinitionresponse
from ..shared import humanitecerrorresponse as shared_humanitecerrorresponse
from ..shared import updatedriverrequestrequest as shared_updatedriverrequestrequest
from typing import Optional



@dataclasses.dataclass
class PutOrgsOrgIDResourcesDriversDriverIDRequest:
    driver_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'driverId', 'style': 'simple', 'explode': False }})
    r"""The Resource Driver ID."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    update_driver_request_request: shared_updatedriverrequestrequest.UpdateDriverRequestRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class PutOrgsOrgIDResourcesDriversDriverIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    driver_definition_response: Optional[shared_driverdefinitionresponse.DriverDefinitionResponse] = dataclasses.field(default=None)
    r"""The updated Resources Driver details."""
    humanitec_error_response: Optional[shared_humanitecerrorresponse.HumanitecErrorResponse] = dataclasses.field(default=None)
    r"""One or more request parameters is missing or invalid."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

