"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class PutOrgsOrgIDAppsAppIDEnvsEnvIDRuntimePausedRequest:
    
    app_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'appId', 'style': 'simple', 'explode': False }})
    r"""The Application ID."""
    env_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'envId', 'style': 'simple', 'explode': False }})
    r"""The Environment ID."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'orgId', 'style': 'simple', 'explode': False }})
    r"""The Organization ID."""
    request_body: bool = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""If the value is `true` the request is to pause an environment, if it is `false` is to resume an environment."""
    

@dataclasses.dataclass
class PutOrgsOrgIDAppsAppIDEnvsEnvIDRuntimePausedResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    