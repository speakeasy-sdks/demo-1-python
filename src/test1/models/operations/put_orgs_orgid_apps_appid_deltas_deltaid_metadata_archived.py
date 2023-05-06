"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import humanitecerrorresponse as shared_humanitecerrorresponse
from typing import Optional


@dataclasses.dataclass
class PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataArchivedRequest:
    
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'appId', 'style': 'simple', 'explode': False }})
    r"""The Application ID."""
    delta_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'deltaId', 'style': 'simple', 'explode': False }})
    r"""ID of the Deployment Delta."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    request_body: bool = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""Either `true` or `false`."""
    

@dataclasses.dataclass
class PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataArchivedResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    humanitec_error_response: Optional[shared_humanitecerrorresponse.HumanitecErrorResponse] = dataclasses.field(default=None)
    r"""The request was invalid."""
    put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_archived_404_application_json_string: Optional[str] = dataclasses.field(default=None)
    r"""No Deployment Delta with ID `deltaId` found in Application."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    