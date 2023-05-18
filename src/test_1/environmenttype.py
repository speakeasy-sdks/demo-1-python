"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from test_1.models import operations, shared
from typing import Optional

class EnvironmentType:
    r"""Environment Types are a way of grouping and managing Environments. Every Environment has exactly 1 Environment Type.
    
    Environment Types can be used with External Resources to manage where resources such as databases are provisioned or even which cluster to deploy to.
    <SchemaDefinition schemaRef=\"#/components/schemas/EnvironmentTypeRequest\" />
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
        
    
    def delete_orgs_org_id_env_types_env_type_id_(self, request: operations.DeleteOrgsOrgIDEnvTypesEnvTypeIDRequest) -> operations.DeleteOrgsOrgIDEnvTypesEnvTypeIDResponse:
        r"""Deletes an Environment Type
        Deletes a specific Environment Type from an Organization. If there are Environments with this Type in the Organization, the operation will fail.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteOrgsOrgIDEnvTypesEnvTypeIDRequest, base_url, '/orgs/{orgId}/env-types/{envTypeId}', request)
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrgsOrgIDEnvTypesEnvTypeIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.EnvironmentTypeResponse])
                res.environment_type_response = out
        elif http_res.status_code in [401, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out
        elif http_res.status_code == 409:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[dict[str, str]]])
                res.delete_orgs_org_id_env_types_env_type_id_409_application_json_objects = out

        return res

    
    def get_orgs_org_id_env_types(self, request: operations.GetOrgsOrgIDEnvTypesRequest) -> operations.GetOrgsOrgIDEnvTypesResponse:
        r"""List all Environment Types
        Lists all Environment Types in an Organization.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrgsOrgIDEnvTypesRequest, base_url, '/orgs/{orgId}/env-types', request)
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDEnvTypesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.EnvironmentTypeResponse]])
                res.environment_type_responses = out

        return res

    
    def get_orgs_org_id_env_types_env_type_id_(self, request: operations.GetOrgsOrgIDEnvTypesEnvTypeIDRequest) -> operations.GetOrgsOrgIDEnvTypesEnvTypeIDResponse:
        r"""Get an Environment Type
        Gets a specific Environment Type within an Organization.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrgsOrgIDEnvTypesEnvTypeIDRequest, base_url, '/orgs/{orgId}/env-types/{envTypeId}', request)
        headers = {}
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDEnvTypesEnvTypeIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.EnvironmentTypeResponse])
                res.environment_type_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def post_orgs_org_id_env_types(self, request: operations.PostOrgsOrgIDEnvTypesRequest) -> operations.PostOrgsOrgIDEnvTypesResponse:
        r"""Add a new Environment Type
        Adds a new Environment Type to an Organization.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PostOrgsOrgIDEnvTypesRequest, base_url, '/orgs/{orgId}/env-types', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "environment_type_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDEnvTypesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.EnvironmentTypeResponse])
                res.environment_type_response = out
        elif http_res.status_code in [400, 401, 409]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    