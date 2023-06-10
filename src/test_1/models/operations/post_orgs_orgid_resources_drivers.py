"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createdriverrequestrequest as shared_createdriverrequestrequest
from ..shared import driverdefinitionresponse as shared_driverdefinitionresponse
from ..shared import humanitecerrorresponse as shared_humanitecerrorresponse
from typing import Optional



@dataclasses.dataclass
class PostOrgsOrgIDResourcesDriversRequest:
    create_driver_request_request: shared_createdriverrequestrequest.CreateDriverRequestRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""Resources Driver details."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    




@dataclasses.dataclass
class PostOrgsOrgIDResourcesDriversResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    driver_definition_response: Optional[shared_driverdefinitionresponse.DriverDefinitionResponse] = dataclasses.field(default=None)
    r"""The newly registered Resources Driver details."""
    humanitec_error_response: Optional[shared_humanitecerrorresponse.HumanitecErrorResponse] = dataclasses.field(default=None)
    r"""One or more request parameters is missing or invalid."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

