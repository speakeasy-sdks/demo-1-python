"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createresourcedefinitionrequestrequest as shared_createresourcedefinitionrequestrequest
from ..shared import humanitecerrorresponse as shared_humanitecerrorresponse
from ..shared import resourcedefinitionresponse as shared_resourcedefinitionresponse
from typing import Optional


@dataclasses.dataclass
class PostOrgsOrgIDResourcesDefsRequest:
    
    create_resource_definition_request_request: shared_createresourcedefinitionrequestrequest.CreateResourceDefinitionRequestRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""The Resource Definition details."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    

@dataclasses.dataclass
class PostOrgsOrgIDResourcesDefsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    humanitec_error_response: Optional[shared_humanitecerrorresponse.HumanitecErrorResponse] = dataclasses.field(default=None)
    r"""One or more request parameters is missing or invalid."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    resource_definition_response: Optional[shared_resourcedefinitionresponse.ResourceDefinitionResponse] = dataclasses.field(default=None)
    r"""The newly created Resources Definition details."""
    