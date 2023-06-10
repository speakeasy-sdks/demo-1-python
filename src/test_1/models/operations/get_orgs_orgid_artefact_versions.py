"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import artefactversionresponse as shared_artefactversionresponse
from ..shared import humanitecerrorresponse as shared_humanitecerrorresponse
from typing import Optional



@dataclasses.dataclass
class GetOrgsOrgIDArtefactVersionsRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The organization ID."""
    archived: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'archived', 'style': 'form', 'explode': True }})
    r"""(Optional) Filter for non-archived Artefact Versions. If no filter is defined only non-archived Artefact Versions are returned, if the filter is true both archived and non-archived Versions are returned."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""(Optional) Filter Artefact Versions by name."""
    reference: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'reference', 'style': 'form', 'explode': True }})
    r"""(Optional) Filter Artefact Versions by the reference to a Version of the same Artefact. This cannot be used together with `name`."""
    




@dataclasses.dataclass
class GetOrgsOrgIDArtefactVersionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    artefact_version_responses: Optional[list[shared_artefactversionresponse.ArtefactVersionResponse]] = dataclasses.field(default=None)
    r"""A list of Artefact Versions registered with your organization."""
    humanitec_error_response: Optional[shared_humanitecerrorresponse.HumanitecErrorResponse] = dataclasses.field(default=None)
    r"""Bad request."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

