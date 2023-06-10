"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import humanitecerrorresponse as shared_humanitecerrorresponse
from ..shared import workloadprofileversionresponse as shared_workloadprofileversionresponse
from typing import Optional



@dataclasses.dataclass
class GetOrgsOrgIDWorkloadProfilesProfileQidVersionsRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    profile_qid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'profileQid', 'style': 'simple', 'explode': False }})
    r"""The Workload profile qualified ID."""
    version: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'version', 'style': 'form', 'explode': True }})
    r"""Optional query parameter, defines version constraint pattern (https://github.com/Masterminds/semver#checking-version-constraints)."""
    




@dataclasses.dataclass
class GetOrgsOrgIDWorkloadProfilesProfileQidVersionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    humanitec_error_response: Optional[shared_humanitecerrorresponse.HumanitecErrorResponse] = dataclasses.field(default=None)
    r"""Workload Profile Versions not found or not accessible by the organization."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    workload_profile_version_responses: Optional[list[shared_workloadprofileversionresponse.WorkloadProfileVersionResponse]] = dataclasses.field(default=None)
    r"""A possibly empty list of Workload Profile Versions."""
    

