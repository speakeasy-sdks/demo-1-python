"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import plaindeltaresponse as shared_plaindeltaresponse
from typing import Optional



@dataclasses.dataclass
class GetOrgsOrgIDAppsAppIDSetsSetIDDiffSourceSetIDRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'appId', 'style': 'simple', 'explode': False }})
    r"""The Application ID."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    set_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'setId', 'style': 'simple', 'explode': False }})
    r"""ID of the Deployment Set."""
    source_set_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'sourceSetId', 'style': 'simple', 'explode': False }})
    r"""ID of the Deployment Set to diff against."""
    




@dataclasses.dataclass
class GetOrgsOrgIDAppsAppIDSetsSetIDDiffSourceSetIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_orgs_org_id_apps_app_id_sets_set_id_diff_source_set_id_404_application_json_string: Optional[str] = dataclasses.field(default=None)
    r"""No Deployment Set with ID `setId` or `sourceSetId` found in Application."""
    plain_delta_response: Optional[shared_plaindeltaresponse.PlainDeltaResponse] = dataclasses.field(default=None)
    r"""A Deployment Delta which if applied to the Set with ID `sourceSetId` gives the Set with ID `setId`."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

