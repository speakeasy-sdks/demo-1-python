"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from test_1 import utils
from test_1.models import operations, shared
from typing import Optional

class Registry:
    r"""Humanitec can be used to manage registry credentials. The Registry object represents how to match credentials to a particular registry.
    
    Humanitec supports all Docker compatible registries as well as the custom authentication formats used by AWS Elastic Container Registry and Google Container Registry. It also supports the injection of a specific secret to be copied from an existing namespace in the cluster.
    <SchemaDefinition schemaRef=\"#/components/schemas/RegistryRequest\" />
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def delete_orgs_org_id_registries_reg_id_(self, request: operations.DeleteOrgsOrgIDRegistriesRegIDRequest) -> operations.DeleteOrgsOrgIDRegistriesRegIDResponse:
        r"""Deletes an existing registry record and all associated credentials and secrets.
        _Deletions are currently irreversible._
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteOrgsOrgIDRegistriesRegIDRequest, base_url, '/orgs/{orgId}/registries/{regId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrgsOrgIDRegistriesRegIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code in [400, 403, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorInfoResponse])
                res.error_info_response = out

        return res

    
    def get_orgs_org_id_registries(self, request: operations.GetOrgsOrgIDRegistriesRequest) -> operations.GetOrgsOrgIDRegistriesResponse:
        r"""Lists available registries for the organization."""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOrgsOrgIDRegistriesRequest, base_url, '/orgs/{orgId}/registries', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDRegistriesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.RegistryResponse]])
                res.registry_responses = out
        elif http_res.status_code in [400, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorInfoResponse])
                res.error_info_response = out

        return res

    
    def get_orgs_org_id_registries_reg_id_(self, request: operations.GetOrgsOrgIDRegistriesRegIDRequest) -> operations.GetOrgsOrgIDRegistriesRegIDResponse:
        r"""Loads a registry record details."""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOrgsOrgIDRegistriesRegIDRequest, base_url, '/orgs/{orgId}/registries/{regId}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDRegistriesRegIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.RegistryResponse])
                res.registry_response = out
        elif http_res.status_code in [400, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorInfoResponse])
                res.error_info_response = out

        return res

    
    def get_orgs_org_id_registries_reg_id_creds(self, request: operations.GetOrgsOrgIDRegistriesRegIDCredsRequest) -> operations.GetOrgsOrgIDRegistriesRegIDCredsResponse:
        r"""Returns current account credentials or secret details for the registry."""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOrgsOrgIDRegistriesRegIDCredsRequest, base_url, '/orgs/{orgId}/registries/{regId}/creds', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDRegistriesRegIDCredsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.RegistryCredsResponse])
                res.registry_creds_response = out
        elif http_res.status_code in [400, 401, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorInfoResponse])
                res.error_info_response = out

        return res

    
    def patch_orgs_org_id_registries_reg_id_(self, request: operations.PatchOrgsOrgIDRegistriesRegIDRequest) -> operations.PatchOrgsOrgIDRegistriesRegIDResponse:
        r"""Updates (patches) an existing registry record."""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PatchOrgsOrgIDRegistriesRegIDRequest, base_url, '/orgs/{orgId}/registries/{regId}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "registry_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PatchOrgsOrgIDRegistriesRegIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.RegistryResponse])
                res.registry_response = out
        elif http_res.status_code in [400, 403, 404, 409]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorInfoResponse])
                res.error_info_response = out

        return res

    
    def post_orgs_org_id_registries(self, request: operations.PostOrgsOrgIDRegistriesRequest) -> operations.PostOrgsOrgIDRegistriesResponse:
        r"""Creates a new registry record."""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostOrgsOrgIDRegistriesRequest, base_url, '/orgs/{orgId}/registries', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "registry_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDRegistriesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.RegistryResponse])
                res.registry_response = out
        elif http_res.status_code in [400, 401, 404, 409]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorInfoResponse])
                res.error_info_response = out

        return res

    