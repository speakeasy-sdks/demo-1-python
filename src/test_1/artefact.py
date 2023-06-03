"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from test_1 import utils
from test_1.models import operations, shared
from typing import Optional

class Artefact:
    r"""Artefacts can be registered with Humanitec. Continuous Integration (CI) pipelines notify Humanitec when a new version of an Artefact becomes available. Humanitec tracks the Artefact along with metadata about how it was built.
    <SchemaDefinition schemaRef=\"#/components/schemas/ArtefactRequest\" />
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def delete_orgs_org_id_artefacts_artefact_id_(self, request: operations.DeleteOrgsOrgIDArtefactsArtefactIDRequest) -> operations.DeleteOrgsOrgIDArtefactsArtefactIDResponse:
        r"""Delete Artefact and all related Artefact Versions
        The specified Artefact and its Artefact Versions will be permanently deleted. Only Administrators can delete an Artefact.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteOrgsOrgIDArtefactsArtefactIDRequest, base_url, '/orgs/{orgId}/artefacts/{artefactId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
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
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOrgsOrgIDArtefactsRequest, base_url, '/orgs/{orgId}/artefacts', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetOrgsOrgIDArtefactsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDArtefactsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.ArtefactResponse]])
                res.artefact_responses = out

        return res

    