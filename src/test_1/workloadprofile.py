"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from test_1 import utils
from test_1.models import operations, shared
from typing import Optional

class WorkloadProfile:
    r"""Workload Profiles provide the baseline configuration for Workloads in Applications in Humanitec. Developers can configure various features of a workload profile to suit their needs. Examples of features might be `schedules` used in Kubernetes CronJobs or `ingress` which might be used to expose Pods controlled by a Kubernetes Deployment.
    
    Workloads in Humanitec are implemented as Helm Charts which must implement a specific schema.
    <SchemaDefinition schemaRef=\"#/components/schemas/WorkloadProfileRequest\" />
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def delete_orgs_org_id_workload_profiles_profile_id_versions_version_(self, request: operations.DeleteOrgsOrgIDWorkloadProfilesProfileIDVersionsVersionRequest) -> operations.DeleteOrgsOrgIDWorkloadProfilesProfileIDVersionsVersionResponse:
        r"""Delete a Workload Profile Version"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteOrgsOrgIDWorkloadProfilesProfileIDVersionsVersionRequest, base_url, '/orgs/{orgId}/workload-profiles/{profileId}/versions/{version}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrgsOrgIDWorkloadProfilesProfileIDVersionsVersionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def delete_orgs_org_id_workload_profiles_profile_qid_(self, request: operations.DeleteOrgsOrgIDWorkloadProfilesProfileQidRequest) -> operations.DeleteOrgsOrgIDWorkloadProfilesProfileQidResponse:
        r"""Delete a Workload Profile
        This will also delete all versions of a workload profile.
        
        It is not possible to delete profiles of other organizations.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteOrgsOrgIDWorkloadProfilesProfileQidRequest, base_url, '/orgs/{orgId}/workload-profiles/{profileQid}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrgsOrgIDWorkloadProfilesProfileQidResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def get_orgs_org_id_workload_profiles(self, request: operations.GetOrgsOrgIDWorkloadProfilesRequest) -> operations.GetOrgsOrgIDWorkloadProfilesResponse:
        r"""List workload profiles available to the organization."""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOrgsOrgIDWorkloadProfilesRequest, base_url, '/orgs/{orgId}/workload-profiles', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDWorkloadProfilesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.WorkloadProfileResponse]])
                res.workload_profile_responses = out

        return res

    
    def get_orgs_org_id_workload_profiles_profile_qid_(self, request: operations.GetOrgsOrgIDWorkloadProfilesProfileQidRequest) -> operations.GetOrgsOrgIDWorkloadProfilesProfileQidResponse:
        r"""Get a Workload Profile"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOrgsOrgIDWorkloadProfilesProfileQidRequest, base_url, '/orgs/{orgId}/workload-profiles/{profileQid}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDWorkloadProfilesProfileQidResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.WorkloadProfileResponse])
                res.workload_profile_response = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def get_orgs_org_id_workload_profiles_profile_qid_versions(self, request: operations.GetOrgsOrgIDWorkloadProfilesProfileQidVersionsRequest) -> operations.GetOrgsOrgIDWorkloadProfilesProfileQidVersionsResponse:
        r"""List versions of the given workload profile with optional constraint."""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOrgsOrgIDWorkloadProfilesProfileQidVersionsRequest, base_url, '/orgs/{orgId}/workload-profiles/{profileQid}/versions', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetOrgsOrgIDWorkloadProfilesProfileQidVersionsRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgsOrgIDWorkloadProfilesProfileQidVersionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.WorkloadProfileVersionResponse]])
                res.workload_profile_version_responses = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def post_orgs_org_id_workload_profiles(self, request: operations.PostOrgsOrgIDWorkloadProfilesRequest) -> operations.PostOrgsOrgIDWorkloadProfilesResponse:
        r"""Create new Workload Profile"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostOrgsOrgIDWorkloadProfilesRequest, base_url, '/orgs/{orgId}/workload-profiles', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "workload_profile_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDWorkloadProfilesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.WorkloadProfileResponse])
                res.workload_profile_response = out
        elif http_res.status_code in [400, 409]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    
    def post_orgs_org_id_workload_profiles_profile_qid_versions(self, request: operations.PostOrgsOrgIDWorkloadProfilesProfileQidVersionsRequest) -> operations.PostOrgsOrgIDWorkloadProfilesProfileQidVersionsResponse:
        r"""Add new Version of the Workload Profile
        Creates a Workload Profile Version from the uploaded Helm chart. The version is retrieved from the chart's metadata (Charts.yaml file).
        
        The request has content type `multipart/form-data` and the request body includes two parts:
        
        1. `file` with `application/x-gzip` content type which is an archive containing a Helm chart.
        
        2. `metadata` with `application/json` content type which defines the version's metadata.
        
        Request body example:
        
        	Content-Type: multipart/form-data; boundary=----boundary 	----boundary 	Content-Disposition: form-data; name=\"metadata\" 	Content-Type: application/json; charset=UTF-8 	{ 	  \"features\": { 	     \"humanitec/service\": {}, 	     \"humanitec/volumes\": {}, 	     \"custom\": {\"schema\": {}} 	  }, 	  \"notes\": \"Notes related to this version of the profile\" 	} 	----boundary 	Content-Disposition: form-data; name=\"file\"; filename=\"my-workload-1.0.1.tgz\" 	Content-Type: application/x-gzip 	[TGZ_DATA] 	----boundary
        
        **NOTE:**
        
        A Workload Profile must be created before a version can be added to it.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostOrgsOrgIDWorkloadProfilesProfileQidVersionsRequest, base_url, '/orgs/{orgId}/workload-profiles/{profileQid}/versions', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'multipart')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostOrgsOrgIDWorkloadProfilesProfileQidVersionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.WorkloadProfileVersionResponse])
                res.workload_profile_version_response = out
        elif http_res.status_code in [400, 404, 409]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HumanitecErrorResponse])
                res.humanitec_error_response = out

        return res

    