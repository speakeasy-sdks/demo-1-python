"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from .accounttype import AccountType
from .activeresource import ActiveResource
from .application import Application
from .artefact import Artefact
from .artefactversion import ArtefactVersion
from .automationrule import AutomationRule
from .delta import Delta
from .deployment import Deployment
from .driverdefinition import DriverDefinition
from .environment import Environment
from .environmenttype import EnvironmentType
from .event import Event
from .image import Image
from .matchingcriteria import MatchingCriteria
from .organization import Organization
from .public import Public
from .registry import Registry
from .resourceaccount import ResourceAccount
from .resourcedefinition import ResourceDefinition
from .resourcetype import ResourceType
from .runtimeinfo import RuntimeInfo
from .set import Set
from .userinvite import UserInvite
from .userprofile import UserProfile
from .userrole import UserRole
from .value import Value
from .valuesetversion import ValueSetVersion
from .workloadprofile import WorkloadProfile

SERVERS = [
    "https://api.humanitec.io/",
]
"""Contains the list of servers available to the SDK"""

class Test1:
    r"""# Introduction
    The *Humanitec API* allows you to automate and integrate Humanitec into your developer and operational workflows.
    The API is a REST based API. It is based around a set of concepts:
    
    * Core
    * External Resources
    * Sets and Deltas
    
    ## Authentication
    Almost all requests made to the Humanitec API require Authentication. Humanitec provides 2 ways of authenticating with the API: `Bearer` and `JWT`.
    
    ### Bearer Authentication
    This form of authentication makes use of a **static token**. It is intended to be used when machines interact with the Humanitec API. Bearer tokens should be used for very narrow purposes. This allows for the token to be revoked if it is compromised and so limit the scope of exposure.
    New Bearer tokens can be obtained via the UI:
    
    1. Log into Humanitec at https://app.humanitec.io
    1. Go to **Organization Settings**
    1. Select **API tokens**
    1. Enter a *name* for the new token and click on **Generate new token**
    
    The token is passed to the API via the `Authorization` header. Assuming the issued token is `HUMANITEC_TOKEN`, the request could be made as follows:
    
    ```
        curl -H 'Authorization: Bearer HUMANITEC_TOKEN' https://api.humanitec.io/orgs/my-org/apps
    ```
    
    ### JWT Authentication
    This form of authentication makes use of a **JSON Web Token (JWT)**. It is intended to be used when humans interact with the Humanitec API. JWTs expire after a period of time. This means that a new JWT will need to be generated regularly. This makes them well suited to working in short sessions, but not for automation. (See Bearer Authentication.)
    The token is passed to the API via the `Authorization` header. Assuming the issued token is `HUMANITEC_JWT`, the request could be made as follows:
    
    ```
        curl -H 'Authorization: JWT HUMANITEC_JWT' https://api.humanitec.io/orgs/my-org/apps
    ```
    
    ## Content Types
    All of the Humanitec API unless explicitly only accepts content types of `application/json` and will always return valid `application/json` or an empty response.
    
    ## Response Codes
    ### Success
    Any response code in the `2xx` range should be regarded as success.
    
    | **Code** | **Meaning** |
    | --- | --- |
    | `200` | Success |
    | `201` | Success (In future, `201` will be replaced by `200`) |
    | `204` | Success, but no content in response |
    
    _Note: We plan to simplify the interface by replacing 201 with 200 status codes._
    
    ### Failure
    Any response code in the `4xx` should be regarded as an error which can be rectified by the client. `5xx` error codes indicate errors that cannot be corrected by the client.
    
    | **Code** | **Meaning** |
    | --- | --- |
    | `400` | General error. (Body will contain details) |
    | `401` | Attempt to access protected resource without `Authorization` Header. |
    | `403` | The `Bearer` or `JWT` does not grant access to the requested resource. |
    | `404` | Resource not found. |
    | `405` | Method not allowed |
    | `409` | Conflict. Usually indicated a resource with that ID already exists. |
    | `422` | Unprocessable Entity. The body was not valid JSON, was empty or contained an object different from what was expected. |
    | `429` | Too many requests - request rate limit has been reached. |
    | `500` | Internal Error. If it occurs repeatedly, contact support. |
    https://docs.humanitec.com - Find out more about how to use Humanitec in your every-day development work.
    """
    account_type: AccountType
    r"""Resource Account Types define cloud providers or protocols to which a resource account can belong.
    <SchemaDefinition schemaRef=\"#/components/schemas/AccountTypeRequest\" />
    """
    active_resource: ActiveResource
    r"""Active Resources represent the concrete resources provisioned for an Environment. They are provisioned on the first deployment after a dependency on a particular resource type is introduced into an Environment. In general, Active Resources are only deleted when their introductory Environment is deleted.
    
    Active Resources are provisioned based on a Resource Definition. The Resource Definition describes how to provision a concrete resource based on a Resource Type and metadata about the Environment (for example the Environment Type or the Application ID). The criteria for how to choose a Resource Definition is known as a Matching Criteria. If the Matching Criteria changes or the Resource Definition is deleted, the concrete resource represented by an Active Resource might be deleted and reprovisioned when a deployment occurs in the Environment.
    <SchemaDefinition schemaRef=\"#/components/schemas/ActiveResourceRequest\" />
    """
    application: Application
    r"""An Application is a collection of Workloads that work together. When deployed, all Workloads in an Application are deployed to the same namespace.
    
    Apps are the root of the configuration tree holding Environments, Deployments, Shared Values, and Secrets.
    <SchemaDefinition schemaRef=\"#/components/schemas/ApplicationRequest\" />
    """
    artefact: Artefact
    r"""Artefacts can be registered with Humanitec. Continuous Integration (CI) pipelines notify Humanitec when a new version of an Artefact becomes available. Humanitec tracks the Artefact along with metadata about how it was built.
    <SchemaDefinition schemaRef=\"#/components/schemas/ArtefactRequest\" />
    """
    artefact_version: ArtefactVersion
    r"""An Artefact Version represents a particular version of an Artefact that can be added to an Application.
    <SchemaDefinition schemaRef=\"#/components/schemas/ArtefactVersionRequest\" />
    """
    automation_rule: AutomationRule
    r"""An Automation Rule defining how and when artefacts in an environment should be updated.
    <SchemaDefinition schemaRef=\"#/components/schemas/AutomationRuleRequest\" />
    """
    delta: Delta
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
    deployment: Deployment
    r"""Deployments represent updates to the running state of an Environment.
    
    Deployments are made by applying _Deltas_ to a state defined by an existing Deployment. The Environment’s from_deploy property defines the Deployment. This Deployment is usually but not always in the current Environment. If the Deployment is from another Environment, the state of that Environment will be \"cloned\" into the current Environment with the option to apply a Delta.
    <SchemaDefinition schemaRef=\"#/components/schemas/DeploymentRequest\" />
    """
    driver_definition: DriverDefinition
    r"""DriverDefinition describes the resource driver.
    
    Resource Drivers are code that fulfils the Humanitec Resource Driver Interface. This interface allows for certain actions to be performed on resources such as creation and destruction. Humanitec provides numerous Resource Drivers “out of the box”. It is also possible to use 3rd party Resource Drivers or write your own.
    <SchemaDefinition schemaRef=\"#/components/schemas/DriverDefinitionRequest\" />
    """
    environment: Environment
    r"""Environments are independent spaces where Applications can run. An Application is always deployed into an Environment.
    <SchemaDefinition schemaRef=\"#/components/schemas/EnvironmentRequest\" />
    """
    environment_type: EnvironmentType
    r"""Environment Types are a way of grouping and managing Environments. Every Environment has exactly 1 Environment Type.
    
    Environment Types can be used with External Resources to manage where resources such as databases are provisioned or even which cluster to deploy to.
    <SchemaDefinition schemaRef=\"#/components/schemas/EnvironmentTypeRequest\" />
    """
    event: Event
    r"""Webhook is a special type of a Job, it performs a HTTPS request to a specified URL with specified headers.
    <SchemaDefinition schemaRef=\"#/components/schemas/WebhookRequest\" />
    """
    image: Image
    r"""DEPRECATED: This type exists for historical compatibility and should not be used. Please use the [Artefact API](https://api-docs.humanitec.com/#tag/Artefact) instead.
    
    Container Images (known simply as Images) can be registered with Humanitec. Continuous Integration (CI) pipelines can then notify Humanitec when a new build of a Container Image becomes available. Humanitec tracks the Image along with metadata about how it was built.
    <SchemaDefinition schemaRef=\"#/components/schemas/ImageRequest\" />
    """
    matching_criteria: MatchingCriteria
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
    organization: Organization
    r"""An Organization is the top level object in Humanitec. All other objects belong to an Organization.
    <SchemaDefinition schemaRef=\"#/components/schemas/OrganizationRequest\" />
    """
    registry: Registry
    r"""Humanitec can be used to manage registry credentials. The Registry object represents how to match credentials to a particular registry.
    
    Humanitec supports all Docker compatible registries as well as the custom authentication formats used by AWS Elastic Container Registry and Google Container Registry. It also supports the injection of a specific secret to be copied from an existing namespace in the cluster.
    <SchemaDefinition schemaRef=\"#/components/schemas/RegistryRequest\" />
    """
    resource_account: ResourceAccount
    r"""ResourceAccount represents the account being used to access a resource.
    
    Resource Accounts hold credentials that are required to provision and manage resources.
    <SchemaDefinition schemaRef=\"#/components/schemas/ResourceAccountRequest\" />
    """
    resource_definition: ResourceDefinition
    r"""A Resource Definitions describes how and when a resource should be provisioned. It links a driver (the how) along with a Matching Criteria (the when) to a Resource Type. This allows Humanitec to invoke a particular driver for the required Resource Type in the context of a particular Application and Environment.
    
    The schema for the `driver_inputs` is defined by the `input_schema` property on the DriverDefinition identified by the `driver_type` property.
    <SchemaDefinition schemaRef=\"#/components/schemas/ResourceDefinitionRequest\" />
    """
    resource_type: ResourceType
    r"""Resources Types define the technology that Applications can have dependencies on.
    
    Each Resource Type also defines a set of input parameters (`inputs_schema`), and a set of output data (`outputs_schema`). When provisioning a resource, these are treated as inputs and outputs respectively.
    <SchemaDefinition schemaRef=\"#/components/schemas/ResourceTypeRequest\" />
    """
    runtime_info: RuntimeInfo
    r"""RuntimeInfo object returned by the runtime endpoint. Represents a list post statuses grouped by modules and controllers (deployments and stateful sets).
    <SchemaDefinition schemaRef=\"#/components/schemas/RuntimeInfoRequest\" />
    """
    set: Set
    r"""A Deployment Set (or just \\"Set\\") defines all of the non-Environment specific configuration for Modules and External Resources. Each of these Modules or External Resources has a unique name.
    
    Deployment Sets are immutable and their ID is a cryptographic hash of their content. This means that a Deployment Set can be globally identified based on its ID. It also means that referencing a Deployment Set by ID will always return the same Deployment Set.
    
    Deployment Sets cannot be created directly, instead they are created by applying a Deployment Delta to an existing Deployment Set.
    
    **Basic Structure**
    
    ```
     {
       \"id\": <ID of the Deployment Set>,
       \"modules\" : {
         <ID of Module> : {
           \"profile\": <Defines how the optional \"spec\" property is interpreted>
           \"spec\": {
             <Properties that depend on the \"profile\" property.>
           }
           \"externals\": {
             <External Resource Name> : {
               \"type\": <Resource Type>,
               \"params\": {
                 <Properties which parametrize the resource depending on the Resource Type.>
               }
             }
           }
         }
       }
     }
    ```
    
    For details about how the Humanitec provided profiles work, see (Deployment Set Profiles)[].
    <SchemaDefinition schemaRef=\"#/components/schemas/SetRequest\" />
    """
    user_invite: UserInvite
    user_profile: UserProfile
    r"""UserProfile holds the profile information of a user
    <SchemaDefinition schemaRef=\"#/components/schemas/UserProfileRequest\" />
    """
    user_role: UserRole
    r"""UserRole holds the mapping of role to user for a particular object.
    <SchemaDefinition schemaRef=\"#/components/schemas/UserRoleRequest\" />
    """
    value: Value
    r"""Shared Values can be used to manage variables and configuration that might vary between environments. They are also the way that secrets can be stored securely.
    
    Shared Values are by default shared across all environments in an application. However, they can be overridden on an Environment by Environment basis.
    
    For example: There might be 2 API keys that are used in an application. One development key used in the development and staging environments and another used for production. The development API key would be set at the Application level. The value would then be overridden at the Environment level for the production Environment.
    <SchemaDefinition schemaRef=\"#/components/schemas/ValueRequest\" />
    """
    value_set_version: ValueSetVersion
    r"""A Value Set Version can be used as a track record of Shared Values changes, to restore a previous version of a Shared Value or Value Set, or to purge a Shared Value if it shouldn't be accessible anymore.
    <SchemaDefinition schemaRef=\"#/components/schemas/ValueSetVersionResponse\" />
    """
    workload_profile: WorkloadProfile
    r"""Workload Profiles provide the baseline configuration for Workloads in Applications in Humanitec. Developers can configure various features of a workload profile to suit their needs. Examples of features might be `schedules` used in Kubernetes CronJobs or `ingress` which might be used to expose Pods controlled by a Kubernetes Deployment.
    
    Workloads in Humanitec are implemented as Helm Charts which must implement a specific schema.
    <SchemaDefinition schemaRef=\"#/components/schemas/WorkloadProfileRequest\" />
    """
    public: Public

    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "1.7.1"
    _gen_version: str = "2.34.7"

    def __init__(self,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        self._client = requests_http.Session()
        
        
        if server_url is not None:
            if url_params is not None:
                self._server_url = utils.template_url(server_url, url_params)
            else:
                self._server_url = server_url

        if client is not None:
            self._client = client
        
        self._security_client = self._client
        

        self._init_sdks()
    
    def _init_sdks(self):
        self.account_type = AccountType(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.active_resource = ActiveResource(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.application = Application(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.artefact = Artefact(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.artefact_version = ArtefactVersion(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.automation_rule = AutomationRule(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.delta = Delta(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.deployment = Deployment(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.driver_definition = DriverDefinition(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.environment = Environment(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.environment_type = EnvironmentType(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.event = Event(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.image = Image(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.matching_criteria = MatchingCriteria(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.organization = Organization(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.registry = Registry(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.resource_account = ResourceAccount(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.resource_definition = ResourceDefinition(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.resource_type = ResourceType(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.runtime_info = RuntimeInfo(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.set = Set(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.user_invite = UserInvite(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.user_profile = UserProfile(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.user_role = UserRole(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.value = Value(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.value_set_version = ValueSetVersion(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.workload_profile = WorkloadProfile(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.public = Public(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    