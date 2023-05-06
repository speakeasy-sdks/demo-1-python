"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import accounttyperesponse as shared_accounttyperesponse
from ..shared import humanitecerrorresponse as shared_humanitecerrorresponse
from typing import Optional


@dataclasses.dataclass
class GetOrgsOrgIDResourcesAccountTypesRequest:
    
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    

@dataclasses.dataclass
class GetOrgsOrgIDResourcesAccountTypesResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    account_type_responses: Optional[list[shared_accounttyperesponse.AccountTypeResponse]] = dataclasses.field(default=None)
    r"""A possibly empty list of Resources Accounts Types."""
    humanitec_error_response: Optional[shared_humanitecerrorresponse.HumanitecErrorResponse] = dataclasses.field(default=None)
    r"""Internal application error."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    