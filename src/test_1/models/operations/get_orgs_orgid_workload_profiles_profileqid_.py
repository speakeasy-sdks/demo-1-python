"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import humanitecerrorresponse as shared_humanitecerrorresponse
from ..shared import workloadprofileresponse as shared_workloadprofileresponse
from typing import Optional



@dataclasses.dataclass
class GetOrgsOrgIDWorkloadProfilesProfileQidRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    profile_qid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'profileQid', 'style': 'simple', 'explode': False }})
    r"""The fully qualified Workload ID. (If not a profile from the current org, must be prefixed with `{orgId}.` e.g. `humanitec.default-cronjob`)"""
    




@dataclasses.dataclass
class GetOrgsOrgIDWorkloadProfilesProfileQidResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    humanitec_error_response: Optional[shared_humanitecerrorresponse.HumanitecErrorResponse] = dataclasses.field(default=None)
    r"""The requested WorkloadProfile is not found."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    workload_profile_response: Optional[shared_workloadprofileresponse.WorkloadProfileResponse] = dataclasses.field(default=None)
    r"""The requested WorkloadProfile."""
    

