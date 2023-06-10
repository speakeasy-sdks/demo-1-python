"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deploymentrequest as shared_deploymentrequest
from ..shared import deploymentresponse as shared_deploymentresponse
from ..shared import humanitecerrorresponse as shared_humanitecerrorresponse
from typing import Optional



@dataclasses.dataclass
class PostOrgsOrgIDAppsAppIDEnvsEnvIDDeploysRequest:
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'appId', 'style': 'simple', 'explode': False }})
    r"""The Application ID."""
    deployment_request: shared_deploymentrequest.DeploymentRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""The Delta describing the change to the Environment and a comment."""
    env_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'envId', 'style': 'simple', 'explode': False }})
    r"""The Environment ID."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    




@dataclasses.dataclass
class PostOrgsOrgIDAppsAppIDEnvsEnvIDDeploysResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    deployment_response: Optional[shared_deploymentresponse.DeploymentResponse] = dataclasses.field(default=None)
    r"""A description of the Deployment."""
    humanitec_error_response: Optional[shared_humanitecerrorresponse.HumanitecErrorResponse] = dataclasses.field(default=None)
    r"""Error because the Delta is non-existent or incompatible with the state of the Environment."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

