"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from test_1.models import operations, shared
from typing import Optional

class ValueSetVersion:
    r"""A Value Set Version can be used as a track record of Shared Values changes, to restore a previous version of a Shared Value or Value Set, or to purge a Shared Value if it shouldn't be accessible anymore.
    <SchemaDefinition schemaRef=\"#/components/schemas/ValueSetVersionResponse\" />
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
        
    
    def get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions(self, request: operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsRequest) -> operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsResponse:
        r"""List Value Set Versions in an Environment of an App
        A new Value Set Version is created on every modification of a Value inside the an Environment of an App. In case this environment has no overrides the response is the same as the App level endpoint.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/value-set-versions', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.ValueSetVersionResponse]])
                res.value_set_version_responses = out

        return res

    
    def get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_(self, request: operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDRequest) -> operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDResponse:
        r"""Get a single Value Set Version in an Environment of an App"""
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/value-set-versions/{valueSetVersionId}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ValueSetVersionResponse])
                res.value_set_version_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def get_orgs_org_id_apps_app_id_value_set_versions(self, request: operations.GetOrgsOrgIDAppsAppIDValueSetVersionsRequest) -> operations.GetOrgsOrgIDAppsAppIDValueSetVersionsResponse:
        r"""List Value Set Versions in the App
        A new Value Set Version is created on every modification of a Value inside the app.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrgsOrgIDAppsAppIDValueSetVersionsRequest, base_url, '/orgs/{orgId}/apps/{appId}/value-set-versions', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetOrgsOrgIDAppsAppIDValueSetVersionsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDAppsAppIDValueSetVersionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.ValueSetVersionResponse]])
                res.value_set_version_responses = out

        return res

    
    def get_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_(self, request: operations.GetOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDRequest) -> operations.GetOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDResponse:
        r"""Get a single Value Set Version from the App"""
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDRequest, base_url, '/orgs/{orgId}/apps/{appId}/value-set-versions/{valueSetVersionId}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ValueSetVersionResponse])
                res.value_set_version_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_purge_key_(self, request: operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDPurgeKeyRequest) -> operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDPurgeKeyResponse:
        r"""Purge the value of a specific Shared Value from the App Environment Version history.
        Purging permanently removes the value of a specific Shared Value in an application. A purged value is no longer accessible, can't be restored and can't be used
        by deployments referencing a Value Set Version where the value was present.
        
        Learn more about purging in our [docs](https://docs.humanitec.com/reference/concepts/app-config/shared-app-values#purge).
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDPurgeKeyRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/value-set-versions/{valueSetVersionId}/purge/{key}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "value_set_action_payload_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDPurgeKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code in [400, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore(self, request: operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDRestoreRequest) -> operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDRestoreResponse:
        r"""Restore a Value Set Version in an Environment of an App
        Restore the values of all Shared Values in an environment from a specific version. Keys not existing in the selected version are deleted.
        
        Learn more about reverting in our [docs](https://docs.humanitec.com/reference/concepts/app-config/shared-app-values#revert).
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDRestoreRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/value-set-versions/{valueSetVersionId}/restore', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "value_set_action_payload_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDRestoreResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ValueSetVersionResponse])
                res.value_set_version_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore_key_(self, request: operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDRestoreKeyRequest) -> operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDRestoreKeyResponse:
        r"""Restore a specific key from the Value Set Version in an Environment of an App
        Restore the values of a single Shared Value in an Environment from a specific version.
        
        Learn more about reverting in our [docs](https://docs.humanitec.com/reference/concepts/app-config/shared-app-values#revert).
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDRestoreKeyRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/value-set-versions/{valueSetVersionId}/restore/{key}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "value_set_action_payload_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDValueSetVersionsValueSetVersionIDRestoreKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ValueSetVersionResponse])
                res.value_set_version_response = out
        elif http_res.status_code in [400, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_purge_key_(self, request: operations.PostOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDPurgeKeyRequest) -> operations.PostOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDPurgeKeyResponse:
        r"""Purge the value of a specific Shared Value from the App Version history.
        Purging permanently removes the value of a specific Shared Value in an Application. A purged value is no longer accessible, can't be restored and can't be used
        by deployments referencing a Value Set Version where the value was present.
        
        Learn more about purging in our [docs](https://docs.humanitec.com/reference/concepts/app-config/shared-app-values#purge).
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PostOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDPurgeKeyRequest, base_url, '/orgs/{orgId}/apps/{appId}/value-set-versions/{valueSetVersionId}/purge/{key}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "value_set_action_payload_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDPurgeKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code in [400, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore(self, request: operations.PostOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDRestoreRequest) -> operations.PostOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDRestoreResponse:
        r"""Restore a Value Set Version in an App
        Restore the values of all Shared Values in an application from a specific version. Keys not existing in the selected version are deleted.
        
        Learn more about reverting in our [docs](https://docs.humanitec.com/reference/concepts/app-config/shared-app-values#revert).
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PostOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDRestoreRequest, base_url, '/orgs/{orgId}/apps/{appId}/value-set-versions/{valueSetVersionId}/restore', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "value_set_action_payload_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDRestoreResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ValueSetVersionResponse])
                res.value_set_version_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore_key_(self, request: operations.PostOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDRestoreKeyRequest) -> operations.PostOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDRestoreKeyResponse:
        r"""Restore a specific key from the Value Set Version in an App
        Restore the values of a single Shared Value in an application from a specific version.
        
        Learn more about reverting in our [docs](https://docs.humanitec.com/reference/concepts/app-config/shared-app-values#revert).
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PostOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDRestoreKeyRequest, base_url, '/orgs/{orgId}/apps/{appId}/value-set-versions/{valueSetVersionId}/restore/{key}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "value_set_action_payload_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDAppsAppIDValueSetVersionsValueSetVersionIDRestoreKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ValueSetVersionResponse])
                res.value_set_version_response = out
        elif http_res.status_code in [400, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    