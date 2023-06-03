"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from test_1 import utils
from test_1.models import operations, shared
from typing import Optional

class Environment:
    r"""Environments are independent spaces where Applications can run. An Application is always deployed into an Environment.
    <SchemaDefinition schemaRef=\"#/components/schemas/EnvironmentRequest\" />
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def delete_orgs_org_id_apps_app_id_envs_env_id_(self, request: operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDRequest) -> operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDResponse:
        r"""Delete a specific Environment.
        Deletes a specific Environment in an Application.
        
        Deleting an Environment will also delete the Deployment history of the Environment.
        
        _Deletions are currently irreversible._
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code in [400, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def get_orgs_org_id_apps_app_id_envs(self, request: operations.GetOrgsOrgIDAppsAppIDEnvsRequest) -> operations.GetOrgsOrgIDAppsAppIDEnvsResponse:
        r"""List all Environments.
        Lists all of the Environments in the Application.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOrgsOrgIDAppsAppIDEnvsRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDAppsAppIDEnvsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.EnvironmentResponse]])
                res.environment_responses = out

        return res

    
    def get_orgs_org_id_apps_app_id_envs_env_id_(self, request: operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRequest) -> operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDResponse:
        r"""Get a specific Environment.
        Gets a specific Environment in an Application.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.EnvironmentResponse])
                res.environment_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def post_orgs_org_id_apps_app_id_envs(self, request: operations.PostOrgsOrgIDAppsAppIDEnvsRequest) -> operations.PostOrgsOrgIDAppsAppIDEnvsResponse:
        r"""Add a new Environment to an Application.
        Creates a new Environment of the specified Type and associates it with the Application specified by `appId`.
        
        The Environment is also initialized to the **current or past state of Deployment in another Environment**. This ensures that every Environment is derived from a previously known state. This means it is not possible to create a new Environment for an Application until at least one Deployment has occurred. (The Deployment does not have to be successful.)
        
        The Type of the Environment must be already defined in the Organization.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostOrgsOrgIDAppsAppIDEnvsRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "environment_definition_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDAppsAppIDEnvsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.EnvironmentResponse])
                res.environment_response = out
        elif http_res.status_code in [400, 404, 409]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def put_orgs_org_id_apps_app_id_envs_env_id_from_deploy_id(self, request: operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDFromDeployIDRequest) -> operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDFromDeployIDResponse:
        r"""Rebase to a different Deployment.
        Rebasing an Environment means that the next Deployment to the Environment will be based on the Deployment specified in the rebase rather than the last one in the Environment. The Deployment to rebase to can either be current or a previous Deployment. The Deployment can be from any Environment of the same Application.
        
        _Running code will only be affected on the next Deployment to the Environment._
        
        Common use cases for rebasing an Environment:
        
        * _Rollback_: Rebasing to a previous Deployment in the current Environment and then Deploying without additional changes will execute a rollback to the previous Deployment state.
        
        * _Clone_: Rebasing to the current Deployment in a different Environment and then deploying without additional changes will clone all of the configuration of the other Environment into the current one. (NOTE: External Resources will not be cloned in the process - the current External Resources of the Environment will remain unchanged and will be used by the deployed Application in the Environment.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDFromDeployIDRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/from_deploy_id', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'string')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDFromDeployIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code in [400, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    