"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from test_1.models import operations, shared
from typing import Optional

class Deployment:
    r"""Deployments represent updates to the running state of an Environment.
    
    Deployments are made by applying _Deltas_ to a state defined by an existing Deployment. The Environment’s from_deploy property defines the Deployment. This Deployment is usually but not always in the current Environment. If the Deployment is from another Environment, the state of that Environment will be \"cloned\" into the current Environment with the option to apply a Delta.
    <SchemaDefinition schemaRef=\"#/components/schemas/DeploymentRequest\" />
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
        
    
    def get_orgs_org_id_apps_app_id_envs_env_id_deploys(self, request: operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDDeploysRequest) -> operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDDeploysResponse:
        r"""List Deployments in an Environment.
        List all of the Deployments that have been carried out in the current Environment. Deployments are returned with the newest first.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDDeploysRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/deploys', request)
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDDeploysResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.DeploymentResponse]])
                res.deployment_responses = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_(self, request: operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDDeploysDeployIDRequest) -> operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDDeploysDeployIDResponse:
        r"""Get a specific Deployment.
        Gets a specific Deployment in an Application and an Environment.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDDeploysDeployIDRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/deploys/{deployId}', request)
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDDeploysDeployIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DeploymentResponse])
                res.deployment_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_errors(self, request: operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDDeploysDeployIDErrorsRequest) -> operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDDeploysDeployIDErrorsResponse:
        r"""List errors that occurred in a Deployment."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDDeploysDeployIDErrorsRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/deploys/{deployId}/errors', request)
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDDeploysDeployIDErrorsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.DeploymentErrorResponse]])
                res.deployment_error_responses = out

        return res

    
    def post_orgs_org_id_apps_app_id_envs_env_id_deploys(self, request: operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDDeploysRequest) -> operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDDeploysResponse:
        r"""Start a new Deployment.
        At Humanitec, Deployments are defined as changes to the state of the Environment. The state can be changed by defining a set of desired changes to the current state via a Deployment Delta or by resetting the current state after a previous Deployment. (See Environment Rebase.) Both types of changes can be combined into a single Deployment during which the Delta is applied to the Rebased state.
        
        When specifying a Delta, a Delta ID must be used. That Delta must have been committed to the Delta store prior to the Deployment.
        
        A Set ID can also be defined in the deployment to force the state of the environment to a particular state. This will be ignored if the Delta is specified.
        
        **NOTE:**
        
        Directly setting a `set_id` in a deployment is not recommended as it will not record history of where the set came from. If the intention is to replicate an existing environment, use the environment rebasing approach described above.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDDeploysRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/deploys', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "deployment_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDDeploysResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DeploymentResponse])
                res.deployment_response = out
        elif http_res.status_code in [400, 404, 409]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    