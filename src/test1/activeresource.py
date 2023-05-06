"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from test1.models import operations, shared
from typing import Optional

class ActiveResource:
    r"""Active Resources represent the concrete resources provisioned for an Environment. They are provisioned on the first deployment after a dependency on a particular resource type is introduced into an Environment. In general, Active Resources are only deleted when their introductory Environment is deleted.
    
    Active Resources are provisioned based on a Resource Definition. The Resource Definition describes how to provision a concrete resource based on a Resource Type and metadata about the Environment (for example the Environment Type or the Application ID). The criteria for how to choose a Resource Definition is known as a Matching Criteria. If the Matching Criteria changes or the Resource Definition is deleted, the concrete resource represented by an Active Resource might be deleted and reprovisioned when a deployment occurs in the Environment.
    <SchemaDefinition schemaRef=\"#/components/schemas/ActiveResourceRequest\" />
    """
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    
    def delete_orgs_org_id_apps_app_id_envs_env_id_resources_type_res_id_(self, request: operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDResourcesTypeResIDRequest) -> operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDResourcesTypeResIDResponse:
        r"""Delete Active Resources."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDResourcesTypeResIDRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/resources/{type}/{resId}', request)
        
        
        client = self._client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDResourcesTypeResIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def get_orgs_org_id_apps_app_id_envs_env_id_resources(self, request: operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDResourcesRequest) -> operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDResourcesResponse:
        r"""List Active Resources provisioned in an environment."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDResourcesRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/resources', request)
        
        
        client = self._client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDResourcesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.ActiveResourceResponse]])
                res.active_resource_responses = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def get_orgs_org_id_resources_defs_def_id_resources(self, request: operations.GetOrgsOrgIDResourcesDefsDefIDResourcesRequest) -> operations.GetOrgsOrgIDResourcesDefsDefIDResourcesResponse:
        r"""List Active Resources provisioned via a specific Resource Definition."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrgsOrgIDResourcesDefsDefIDResourcesRequest, base_url, '/orgs/{orgId}/resources/defs/{defId}/resources', request)
        
        
        client = self._client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDResourcesDefsDefIDResourcesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.ActiveResourceResponse]])
                res.active_resource_responses = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    