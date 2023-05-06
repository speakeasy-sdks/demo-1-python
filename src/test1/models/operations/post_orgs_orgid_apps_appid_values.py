"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import humanitecerrorresponse as shared_humanitecerrorresponse
from ..shared import valuecreatepayloadrequest as shared_valuecreatepayloadrequest
from ..shared import valueresponse as shared_valueresponse
from typing import Optional


@dataclasses.dataclass
class PostOrgsOrgIDAppsAppIDValuesRequest:
    
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'appId', 'style': 'simple', 'explode': False }})
    r"""The Application ID."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    value_create_payload_request: shared_valuecreatepayloadrequest.ValueCreatePayloadRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""Definition of the new Shared Value."""
    

@dataclasses.dataclass
class PostOrgsOrgIDAppsAppIDValuesResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    humanitec_error_response: Optional[shared_humanitecerrorresponse.HumanitecErrorResponse] = dataclasses.field(default=None)
    r"""Input not valid."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    value_response: Optional[shared_valueresponse.ValueResponse] = dataclasses.field(default=None)
    r"""Shared Value successfully created."""
    