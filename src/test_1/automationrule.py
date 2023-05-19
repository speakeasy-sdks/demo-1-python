"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from test_1.models import operations, shared
from typing import Optional

class AutomationRule:
    r"""An Automation Rule defining how and when artefacts in an environment should be updated.
    <SchemaDefinition schemaRef=\"#/components/schemas/AutomationRuleRequest\" />
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
        
    
    def delete_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_(self, request: operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDRequest) -> operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDResponse:
        r"""Delete Automation Rule from an Environment."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/rules/{ruleId}', request)
        headers = {}
        headers['Accept'] = '*/*'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        

        return res

    
    def get_orgs_org_id_apps_app_id_envs_env_id_rules(self, request: operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRulesRequest) -> operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRulesResponse:
        r"""List all Automation Rules in an Environment."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRulesRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/rules', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRulesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.AutomationRuleResponse]])
                res.automation_rule_responses = out
        elif http_res.status_code == 500:
            pass

        return res

    
    def get_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_(self, request: operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDRequest) -> operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDResponse:
        r"""Get a specific Automation Rule for an Environment."""
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/rules/{ruleId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AutomationRuleResponse])
                res.automation_rule_response = out
        elif http_res.status_code == 404:
            pass

        return res

    
    def post_orgs_org_id_apps_app_id_envs_env_id_rules(self, request: operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDRulesRequest) -> operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDRulesResponse:
        r"""Create a new Automation Rule for an Environment.
        Items marked as deprecated are still supported (however not recommended) for use and are incompatible with properties of the latest api version. In particular an error is raised if  `images_filter` (deprecated) and `artefacts_filter` are used in the same payload. The same is true for `exclude_images_filter` (deprecated) and `exclude_artefacts_filter`. `match` and `update_to` are still supported but will trigger an error if combined with `match_ref`.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDRulesRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/rules', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "automation_rule_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDAppsAppIDEnvsEnvIDRulesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AutomationRuleResponse])
                res.automation_rule_response = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorInfoResponse])
                res.error_info_response = out
        elif http_res.status_code == 422:
            pass

        return res

    
    def put_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_(self, request: operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDRequest) -> operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDResponse:
        r"""Update an existing Automation Rule for an Environment.
        Items marked as deprecated are still supported (however not recommended) for use and are incompatible with properties of the latest api version. In particular an error is raised if  `images_filter` (deprecated) and `artefacts_filter` are used in the same payload. The same is true for `exclude_images_filter` (deprecated) and `exclude_artefacts_filter`. `match` and `update_to` are still supported but will trigger an error if combined with `match_ref`.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDRequest, base_url, '/orgs/{orgId}/apps/{appId}/envs/{envId}/rules/{ruleId}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "automation_rule_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = self._client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutOrgsOrgIDAppsAppIDEnvsEnvIDRulesRuleIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AutomationRuleResponse])
                res.automation_rule_response = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorInfoResponse])
                res.error_info_response = out
        elif http_res.status_code in [404, 422]:
            pass

        return res

    