"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from test_1 import utils
from test_1.models import operations, shared
from typing import Optional

class MatchingCriteria:
    r"""Matching Criteria are a set of rules used to choose which Resource Definition to use to provision a particular Resource Type.
    
    Matching criteria are made up in order of specificity with least specific first:
    
    - Environment Type (`env_type`)
    
    - Application (`app_id`)
    
    - Environment (`env_id`)
    
    - Resource (`res_id`)
    
    When selecting matching criteria, the most specific one is selected. In general, this means of all the Matching Criteria fully matching the context, the Matching Criteria Rule with the most specific element filled is chosen. If there is a tie, the next most specific elements are compared and so on until one is chosen.
    
    **NOTE:**
    
    Humanitec will reject the registration of matching criteria rules that duplicate rules already present for a Resource Type.
    <SchemaDefinition schemaRef=\"#/components/schemas/MatchingCriteriaRequest\" />
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def delete_orgs_org_id_resources_defs_def_id_criteria_criteria_id_(self, request: operations.DeleteOrgsOrgIDResourcesDefsDefIDCriteriaCriteriaIDRequest) -> operations.DeleteOrgsOrgIDResourcesDefsDefIDCriteriaCriteriaIDResponse:
        r"""Delete a Matching Criteria from a Resource Definition.
        If there **are no** Active Resources that would match to a different Resource Definition when the current Matching Criteria is deleted, the Matching Criteria is deleted immediately.
        
        If there **are** Active Resources that would match to a different Resource Definition, the request fails with HTTP status code 409 (Conflict). The response content will list all of affected Active Resources and their new matches.
        
        The request can take an optional `force` query parameter. If set to `true`, the Matching Criteria is deleted immediately. Referenced Active Resources would match to a different Resource Definition during the next deployment in the target environment.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteOrgsOrgIDResourcesDefsDefIDCriteriaCriteriaIDRequest, base_url, '/orgs/{orgId}/resources/defs/{defId}/criteria/{criteriaId}', request)
        headers = {}
        query_params = utils.get_query_params(operations.DeleteOrgsOrgIDResourcesDefsDefIDCriteriaCriteriaIDRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0.7, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('DELETE', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrgsOrgIDResourcesDefsDefIDCriteriaCriteriaIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                res.delete_orgs_org_id_resources_defs_def_id_criteria_criteria_id_404_application_json_string = http_res.content
        elif http_res.status_code == 409:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.ResourceDefinitionChangeResponse]])
                res.resource_definition_change_responses = out
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def post_orgs_org_id_resources_defs_def_id_criteria(self, request: operations.PostOrgsOrgIDResourcesDefsDefIDCriteriaRequest) -> operations.PostOrgsOrgIDResourcesDefsDefIDCriteriaResponse:
        r"""Add a new Matching Criteria to a Resource Definition.
        Matching Criteria are combined with Resource Type to select a specific definition. Matching Criteria can be set for any combination of Application ID, Environment ID, Environment Type, and Resource ID. In the event of multiple matches, the most specific match is chosen.
        
        For example, given 3 sets of matching criteria for the same type:
        
        ```
         1. {\"env_type\":\"test\"}
         2. {\"env_type\":\"development\"}
         3. {\"env_type\":\"test\", \"app_id\":\"my-app\"}
        ```
        
        If, a resource of that time was needed in an Application `my-app`, Environment `qa-team` with Type `test` and Resource ID `modules.my-module-externals.my-resource`, there would be two resources definitions matching the criteria: #1 & #3. Definition #3 will be chosen because it's matching criteria is the most specific.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostOrgsOrgIDResourcesDefsDefIDCriteriaRequest, base_url, '/orgs/{orgId}/resources/defs/{defId}/criteria', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "matching_criteria_rule_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDResourcesDefsDefIDCriteriaResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.MatchingCriteriaResponse])
                res.matching_criteria_response = out
        elif http_res.status_code in [400, 409, 422, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    