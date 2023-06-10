"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorinforesponse as shared_errorinforesponse
from ..shared import registryrequest as shared_registryrequest
from ..shared import registryresponse as shared_registryresponse
from typing import Optional



@dataclasses.dataclass
class PostOrgsOrgIDRegistriesRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""Unique (alpha-numerical) organization identifier."""
    registry_request: shared_registryrequest.RegistryRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""A new record details."""
    




@dataclasses.dataclass
class PostOrgsOrgIDRegistriesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_info_response: Optional[shared_errorinforesponse.ErrorInfoResponse] = dataclasses.field(default=None)
    r"""Request parameters or payload are incomplete or invalid."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    registry_response: Optional[shared_registryresponse.RegistryResponse] = dataclasses.field(default=None)
    r"""A newly created record details."""
    

