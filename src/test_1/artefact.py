"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from test_1.models import operations, shared
from typing import Optional

class Artefact:
    r"""Artefacts can be registered with Humanitec. Continuous Integration (CI) pipelines notify Humanitec when a new version of an Artefact becomes available. Humanitec tracks the Artefact along with metadata about how it was built.
    <SchemaDefinition schemaRef=\"#/components/schemas/ArtefactRequest\" />
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
        
    
    def delete_orgs_org_id_artefacts_artefact_id_(self, request: operations.DeleteOrgsOrgIDArtefactsArtefactIDRequest) -> operations.DeleteOrgsOrgIDArtefactsArtefactIDResponse:
        r"""Delete Artefact and all related Artefact Versions
        The specified Artefact and its Artefact Versions will be permanently deleted. Only Administrators can delete an Artefact.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteOrgsOrgIDArtefactsArtefactIDRequest, base_url, '/orgs/{orgId}/artefacts/{artefactId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrgsOrgIDArtefactsArtefactIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code in [403, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def get_orgs_org_id_artefacts(self, request: operations.GetOrgsOrgIDArtefactsRequest) -> operations.GetOrgsOrgIDArtefactsResponse:
        r"""List all Artefacts.
        Returns the Artefacts registered with your organization. If no elements are found, an empty list is returned.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrgsOrgIDArtefactsRequest, base_url, '/orgs/{orgId}/artefacts', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetOrgsOrgIDArtefactsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDArtefactsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.ArtefactResponse]])
                res.artefact_responses = out

        return res

    