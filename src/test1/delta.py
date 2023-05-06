"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from test1.models import operations, shared
from typing import Any, Optional

class Delta:
    r"""A Deployment Delta (or just \\"Delta\\") describes the changes that must be applied to one Deployment Set to generate another Deployment Set. Deployment Deltas are the only way to create new Deployment Sets.
    
    Deployment Deltas can be created fully formed or combined together via PATCHing. They can also be generated from the difference between two Deployment Sets.
    
    **Basic Structure**
    
    ```
     {
       \"id\": <ID of the Deployment Delta.>,
       \"metadata\": {
         <Properties such as who created the Delta, which Environment it is associated to and a Human-friendly name>
       }
       \"modules\" : {
         \"add\" : {
           <ID of Module to add to the Deployment Set> : {
             <An entire Modules object>
           }
         },
         \"remove\": [
           <An array of Module IDs that should be removed from the Deployment Set>
         ],
        \"update\": {
           <ID of Module already in the Set to be updated> : [
             <An array of JSON Patch (Search Results (RFC 6902) objects scoped to the module>
           ]
         }
       }
     }
    ```
    <SchemaDefinition schemaRef=\"#/components/schemas/DeltaRequest\" />
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
        
    
    def get_delta(self, request: operations.GetDeltaRequest) -> operations.GetDeltaResponse:
        r"""Fetch an existing Delta"""
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetDeltaRequest, base_url, '/orgs/{orgId}/apps/{appId}/deltas/{deltaId}', request)
        
        
        client = self._client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDeltaResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DeltaResponse])
                res.delta_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                res.get_delta_404_application_json_string = http_res.content

        return res

    
    def get_orgs_org_id_apps_app_id_deltas(self, request: operations.GetOrgsOrgIDAppsAppIDDeltasRequest) -> operations.GetOrgsOrgIDAppsAppIDDeltasResponse:
        r"""List Deltas in an Application"""
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrgsOrgIDAppsAppIDDeltasRequest, base_url, '/orgs/{orgId}/apps/{appId}/deltas', request)
        
        query_params = utils.get_query_params(operations.GetOrgsOrgIDAppsAppIDDeltasRequest, request)
        
        client = self._client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDAppsAppIDDeltasResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.DeltaResponse]])
                res.delta_responses = out

        return res

    
    def patch_orgs_org_id_apps_app_id_deltas_delta_id_(self, request: operations.PatchOrgsOrgIDAppsAppIDDeltasDeltaIDRequest) -> operations.PatchOrgsOrgIDAppsAppIDDeltasDeltaIDResponse:
        r"""Update an existing Delta"""
        base_url = self._server_url
        
        url = utils.generate_url(operations.PatchOrgsOrgIDAppsAppIDDeltasDeltaIDRequest, base_url, '/orgs/{orgId}/apps/{appId}/deltas/{deltaId}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PatchOrgsOrgIDAppsAppIDDeltasDeltaIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DeltaResponse])
                res.delta_response = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                res.patch_orgs_org_id_apps_app_id_deltas_delta_id_404_application_json_string = http_res.content

        return res

    
    def post_orgs_org_id_apps_app_id_deltas(self, request: operations.PostOrgsOrgIDAppsAppIDDeltasRequest) -> operations.PostOrgsOrgIDAppsAppIDDeltasResponse:
        r"""Create a new Delta"""
        base_url = self._server_url
        
        url = utils.generate_url(operations.PostOrgsOrgIDAppsAppIDDeltasRequest, base_url, '/orgs/{orgId}/apps/{appId}/deltas', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "delta_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDAppsAppIDDeltasResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[Any])
                res.post_orgs_org_id_apps_app_id_deltas_200_application_json_one_of = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def put_delta(self, request: operations.PutDeltaRequest) -> operations.PutDeltaResponse:
        r"""Update an existing Delta"""
        base_url = self._server_url
        
        url = utils.generate_url(operations.PutDeltaRequest, base_url, '/orgs/{orgId}/apps/{appId}/deltas/{deltaId}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "delta_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutDeltaResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                res.put_delta_404_application_json_string = http_res.content

        return res

    
    def put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_archived(self, request: operations.PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataArchivedRequest) -> operations.PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataArchivedResponse:
        r"""Mark a Delta as \\"archived\\" 
        Archived Deltas are still accessible but can no longer be updated.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataArchivedRequest, base_url, '/orgs/{orgId}/apps/{appId}/deltas/{deltaId}/metadata/archived', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataArchivedResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                res.put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_archived_404_application_json_string = http_res.content

        return res

    
    def put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_env_id(self, request: operations.PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataEnvIDRequest) -> operations.PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataEnvIDResponse:
        r"""Change the Environment of a Delta"""
        base_url = self._server_url
        
        url = utils.generate_url(operations.PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataEnvIDRequest, base_url, '/orgs/{orgId}/apps/{appId}/deltas/{deltaId}/metadata/env_id', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'string')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataEnvIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                res.put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_env_id_404_application_json_string = http_res.content

        return res

    
    def put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_name(self, request: operations.PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataNameRequest) -> operations.PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataNameResponse:
        r"""Change the name of a Delta"""
        base_url = self._server_url
        
        url = utils.generate_url(operations.PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataNameRequest, base_url, '/orgs/{orgId}/apps/{appId}/deltas/{deltaId}/metadata/name', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'string')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutOrgsOrgIDAppsAppIDDeltasDeltaIDMetadataNameResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                res.put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_name_404_application_json_string = http_res.content

        return res

    