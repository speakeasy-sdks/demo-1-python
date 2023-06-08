"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from test_1 import utils
from test_1.models import operations, shared
from typing import Optional

class Value:
    r"""Shared Values can be used to manage variables and configuration that might vary between environments. They are also the way that secrets can be stored securely.
    
    Shared Values are by default shared across all environments in an application. However, they can be overridden on an Environment by Environment basis.
    
    For example: There might be 2 API keys that are used in an application. One development key used in the development and staging environments and another used for production. The development API key would be set at the Application level. The value would then be overridden at the Environment level for the production Environment.
    <SchemaDefinition schemaRef=\"#/components/schemas/ValueRequest\" />
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def delete_orgs_org_id_apps_app_id_envs_env_id_values(self, request: operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDValuesRequest) -> operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDValuesResponse:
        r"""Delete all Shared Value for an Environment
        All Shared Values will be deleted. If the Shared Values are marked as a secret, they will also be deleted.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDValuesRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/values', request)
        headers = {}
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDValuesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def delete_orgs_org_id_apps_app_id_envs_env_id_values_key_(self, request: operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyRequest) -> operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyResponse:
        r"""Delete Shared Value for an Environment
        The specified Shared Value will be permanently deleted. If the Shared Value is marked as a secret, it will also be permanently deleted.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/values/{key}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code in [400, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def delete_orgs_org_id_apps_app_id_values(self, request: operations.DeleteOrgsOrgIDAppsAppIDValuesRequest) -> operations.DeleteOrgsOrgIDAppsAppIDValuesResponse:
        r"""Delete all Shared Value for an App
        All Shared Values will be deleted. If the Shared Values are marked as a secret, they will also be deleted.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteOrgsOrgIDAppsAppIDValuesRequest, base_url, '/orgs/{orgId}/apps/{appId}/values', request)
        headers = {}
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrgsOrgIDAppsAppIDValuesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def delete_orgs_org_id_apps_app_id_values_key_(self, request: operations.DeleteOrgsOrgIDAppsAppIDValuesKeyRequest) -> operations.DeleteOrgsOrgIDAppsAppIDValuesKeyResponse:
        r"""Delete Shared Value for an Application
        The specified Shared Value will be permanently deleted. If the Shared Value is marked as a secret, it will also be permanently deleted.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteOrgsOrgIDAppsAppIDValuesKeyRequest, base_url, '/orgs/{orgId}/apps/{appId}/values/{key}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrgsOrgIDAppsAppIDValuesKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code in [400, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def get_orgs_org_id_apps_app_id_envs_env_id_values(self, request: operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValuesRequest) -> operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValuesResponse:
        r"""List Shared Values in an Environment
        The returned values will be the base Application values with the Environment overrides where applicable. The `source` field will specify the level from which the value is from.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValuesRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/values', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValuesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.ValueResponse]])
                res.value_responses = out

        return res

    
    def get_orgs_org_id_apps_app_id_values(self, request: operations.GetOrgsOrgIDAppsAppIDValuesRequest) -> operations.GetOrgsOrgIDAppsAppIDValuesResponse:
        r"""List Shared Values in an Application
        The returned values will be the \"base\" values for the Application. The overridden value for the Environment can be retrieved via the `/orgs/{orgId}/apps/{appId}/envs/{envId}/values` endpoint.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOrgsOrgIDAppsAppIDValuesRequest, base_url, '/orgs/{orgId}/apps/{appId}/values', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDAppsAppIDValuesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.ValueResponse]])
                res.value_responses = out

        return res

    
    def patch_orgs_org_id_apps_app_id_envs_env_id_values_key_(self, request: operations.PatchOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyRequest) -> operations.PatchOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyResponse:
        r"""Update Shared Value for an Environment
        Update the value or description of the Shared Value. Shared Values marked as secret can also be updated.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PatchOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/values/{key}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "value_patch_payload_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PatchOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ValueResponse])
                res.value_response = out
        elif http_res.status_code in [400, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def patch_orgs_org_id_apps_app_id_values_key_(self, request: operations.PatchOrgsOrgIDAppsAppIDValuesKeyRequest) -> operations.PatchOrgsOrgIDAppsAppIDValuesKeyResponse:
        r"""Update Shared Value for an Application
        Update the value or description of the Shared Value. Shared Values marked as secret can also be updated.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PatchOrgsOrgIDAppsAppIDValuesKeyRequest, base_url, '/orgs/{orgId}/apps/{appId}/values/{key}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "value_patch_payload_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PatchOrgsOrgIDAppsAppIDValuesKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ValueResponse])
                res.value_response = out
        elif http_res.status_code in [400, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def post_orgs_org_id_apps_app_id_envs_env_id_values(self, request: operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValuesRequest) -> operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValuesResponse:
        r"""Create a Shared Value for an Environment
        The Shared Value created will only be available to the specific Environment.
        
        If a Value is marked as a secret, it will be securely stored. It will not be possible to retrieve the value again through the API. The value of the secret can however be updated.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValuesRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/values', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "value_create_payload_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValuesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ValueResponse])
                res.value_response = out
        elif http_res.status_code in [400, 409]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def post_orgs_org_id_apps_app_id_values(self, request: operations.PostOrgsOrgIDAppsAppIDValuesRequest) -> operations.PostOrgsOrgIDAppsAppIDValuesResponse:
        r"""Create a Shared Value for an Application
        The Shared Value created will be available to all Environments in that Application.
        
        If a Value is marked as a secret, it will be securely stored. It will not be possible to retrieve the value again through the API. The value of the secret can however be updated.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostOrgsOrgIDAppsAppIDValuesRequest, base_url, '/orgs/{orgId}/apps/{appId}/values', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "value_create_payload_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDAppsAppIDValuesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ValueResponse])
                res.value_response = out
        elif http_res.status_code in [400, 409]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def put_orgs_org_id_apps_app_id_envs_env_id_values_key_(self, request: operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyRequest) -> operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyResponse:
        r"""Update Shared Value for an Environment
        Update the value or description of the Shared Value. Shared Values marked as secret can also be updated.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/values/{key}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "value_edit_payload_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDValuesKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ValueResponse])
                res.value_response = out
        elif http_res.status_code in [400, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def put_orgs_org_id_apps_app_id_values_key_(self, request: operations.PutOrgsOrgIDAppsAppIDValuesKeyRequest) -> operations.PutOrgsOrgIDAppsAppIDValuesKeyResponse:
        r"""Update Shared Value for an Application
        Update the value or description of the Shared Value. Shared Values marked as secret can also be updated.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutOrgsOrgIDAppsAppIDValuesKeyRequest, base_url, '/orgs/{orgId}/apps/{appId}/values/{key}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "value_edit_payload_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutOrgsOrgIDAppsAppIDValuesKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ValueResponse])
                res.value_response = out
        elif http_res.status_code in [400, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    