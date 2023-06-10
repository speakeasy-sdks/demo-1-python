# test-1

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/demo-1-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import test_1
from test_1.models import operations

s = test_1.Test1()

req = operations.GetOrgsOrgIDResourcesAccountTypesRequest(
    org_id='corrupti',
)

res = s.account_type.get_orgs_org_id_resources_account_types(req)

if res.account_type_responses is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [account_type](docs/sdks/accounttype/README.md)

* [get_orgs_org_id_resources_account_types](docs/sdks/accounttype/README.md#get_orgs_org_id_resources_account_types) - List Resource Account Types available to the organization.

### [active_resource](docs/sdks/activeresource/README.md)

* [delete_orgs_org_id_apps_app_id_envs_env_id_resources_type_res_id_](docs/sdks/activeresource/README.md#delete_orgs_org_id_apps_app_id_envs_env_id_resources_type_res_id_) - Delete Active Resources.
* [get_orgs_org_id_apps_app_id_envs_env_id_resources](docs/sdks/activeresource/README.md#get_orgs_org_id_apps_app_id_envs_env_id_resources) - List Active Resources provisioned in an environment.
* [get_orgs_org_id_resources_defs_def_id_resources](docs/sdks/activeresource/README.md#get_orgs_org_id_resources_defs_def_id_resources) - List Active Resources provisioned via a specific Resource Definition.

### [application](docs/sdks/application/README.md)

* [delete_orgs_org_id_apps_app_id_](docs/sdks/application/README.md#delete_orgs_org_id_apps_app_id_) - Delete an Application
* [get_orgs_org_id_apps](docs/sdks/application/README.md#get_orgs_org_id_apps) - List all Applications in an Organization.
* [get_orgs_org_id_apps_app_id_](docs/sdks/application/README.md#get_orgs_org_id_apps_app_id_) - Get an existing Application
* [post_orgs_org_id_apps](docs/sdks/application/README.md#post_orgs_org_id_apps) - Add a new Application to an Organization

### [artefact](docs/sdks/artefact/README.md)

* [delete_orgs_org_id_artefacts_artefact_id_](docs/sdks/artefact/README.md#delete_orgs_org_id_artefacts_artefact_id_) - Delete Artefact and all related Artefact Versions
* [get_orgs_org_id_artefacts](docs/sdks/artefact/README.md#get_orgs_org_id_artefacts) - List all Artefacts.

### [artefact_version](docs/sdks/artefactversion/README.md)

* [get_orgs_org_id_artefact_versions](docs/sdks/artefactversion/README.md#get_orgs_org_id_artefact_versions) - List all Artefacts Versions.
* [get_orgs_org_id_artefact_versions_artefact_version_id_](docs/sdks/artefactversion/README.md#get_orgs_org_id_artefact_versions_artefact_version_id_) - Get an Artefacts Versions.
* [get_orgs_org_id_artefacts_artefact_id_versions](docs/sdks/artefactversion/README.md#get_orgs_org_id_artefacts_artefact_id_versions) - List all Artefact Versions of an Artefact.
* [patch_orgs_org_id_artefacts_artefact_id_versions_version_id_](docs/sdks/artefactversion/README.md#patch_orgs_org_id_artefacts_artefact_id_versions_version_id_) - Update Version of an Artefact.
* [post_orgs_org_id_artefact_versions](docs/sdks/artefactversion/README.md#post_orgs_org_id_artefact_versions) - Register a new Artefact Version with your organization.

### [automation_rule](docs/sdks/automationrule/README.md)

* [delete_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_](docs/sdks/automationrule/README.md#delete_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_) - Delete Automation Rule from an Environment.
* [get_orgs_org_id_apps_app_id_envs_env_id_rules](docs/sdks/automationrule/README.md#get_orgs_org_id_apps_app_id_envs_env_id_rules) - List all Automation Rules in an Environment.
* [get_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_](docs/sdks/automationrule/README.md#get_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_) - Get a specific Automation Rule for an Environment.
* [post_orgs_org_id_apps_app_id_envs_env_id_rules](docs/sdks/automationrule/README.md#post_orgs_org_id_apps_app_id_envs_env_id_rules) - Create a new Automation Rule for an Environment.
* [put_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_](docs/sdks/automationrule/README.md#put_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_) - Update an existing Automation Rule for an Environment.

### [delta](docs/sdks/delta/README.md)

* [get_delta](docs/sdks/delta/README.md#get_delta) - Fetch an existing Delta
* [get_orgs_org_id_apps_app_id_deltas](docs/sdks/delta/README.md#get_orgs_org_id_apps_app_id_deltas) - List Deltas in an Application
* [patch_orgs_org_id_apps_app_id_deltas_delta_id_](docs/sdks/delta/README.md#patch_orgs_org_id_apps_app_id_deltas_delta_id_) - Update an existing Delta
* [post_orgs_org_id_apps_app_id_deltas](docs/sdks/delta/README.md#post_orgs_org_id_apps_app_id_deltas) - Create a new Delta
* [put_delta](docs/sdks/delta/README.md#put_delta) - Update an existing Delta
* [put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_archived](docs/sdks/delta/README.md#put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_archived) - Mark a Delta as "archived"
* [put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_env_id](docs/sdks/delta/README.md#put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_env_id) - Change the Environment of a Delta
* [put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_name](docs/sdks/delta/README.md#put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_name) - Change the name of a Delta

### [deployment](docs/sdks/deployment/README.md)

* [get_orgs_org_id_apps_app_id_envs_env_id_deploys](docs/sdks/deployment/README.md#get_orgs_org_id_apps_app_id_envs_env_id_deploys) - List Deployments in an Environment.
* [get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_](docs/sdks/deployment/README.md#get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_) - Get a specific Deployment.
* [get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_errors](docs/sdks/deployment/README.md#get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_errors) - List errors that occurred in a Deployment.
* [post_orgs_org_id_apps_app_id_envs_env_id_deploys](docs/sdks/deployment/README.md#post_orgs_org_id_apps_app_id_envs_env_id_deploys) - Start a new Deployment.

### [driver_definition](docs/sdks/driverdefinition/README.md)

* [delete_orgs_org_id_resources_drivers_driver_id_](docs/sdks/driverdefinition/README.md#delete_orgs_org_id_resources_drivers_driver_id_) - Delete a Resources Driver.
* [get_orgs_org_id_resources_drivers](docs/sdks/driverdefinition/README.md#get_orgs_org_id_resources_drivers) - List Resource Drivers.
* [get_orgs_org_id_resources_drivers_driver_id_](docs/sdks/driverdefinition/README.md#get_orgs_org_id_resources_drivers_driver_id_) - Get a Resource Driver.
* [post_orgs_org_id_resources_drivers](docs/sdks/driverdefinition/README.md#post_orgs_org_id_resources_drivers) - Register a new Resource Driver.
* [put_orgs_org_id_resources_drivers_driver_id_](docs/sdks/driverdefinition/README.md#put_orgs_org_id_resources_drivers_driver_id_) - Update a Resource Driver.

### [environment](docs/sdks/environment/README.md)

* [delete_orgs_org_id_apps_app_id_envs_env_id_](docs/sdks/environment/README.md#delete_orgs_org_id_apps_app_id_envs_env_id_) - Delete a specific Environment.
* [get_orgs_org_id_apps_app_id_envs](docs/sdks/environment/README.md#get_orgs_org_id_apps_app_id_envs) - List all Environments.
* [get_orgs_org_id_apps_app_id_envs_env_id_](docs/sdks/environment/README.md#get_orgs_org_id_apps_app_id_envs_env_id_) - Get a specific Environment.
* [post_orgs_org_id_apps_app_id_envs](docs/sdks/environment/README.md#post_orgs_org_id_apps_app_id_envs) - Add a new Environment to an Application.
* [put_orgs_org_id_apps_app_id_envs_env_id_from_deploy_id](docs/sdks/environment/README.md#put_orgs_org_id_apps_app_id_envs_env_id_from_deploy_id) - Rebase to a different Deployment.

### [environment_type](docs/sdks/environmenttype/README.md)

* [delete_orgs_org_id_env_types_env_type_id_](docs/sdks/environmenttype/README.md#delete_orgs_org_id_env_types_env_type_id_) - Deletes an Environment Type
* [get_orgs_org_id_env_types](docs/sdks/environmenttype/README.md#get_orgs_org_id_env_types) - List all Environment Types
* [get_orgs_org_id_env_types_env_type_id_](docs/sdks/environmenttype/README.md#get_orgs_org_id_env_types_env_type_id_) - Get an Environment Type
* [post_orgs_org_id_env_types](docs/sdks/environmenttype/README.md#post_orgs_org_id_env_types) - Add a new Environment Type

### [event](docs/sdks/event/README.md)

* [delete_orgs_org_id_apps_app_id_jobs](docs/sdks/event/README.md#delete_orgs_org_id_apps_app_id_jobs) - Deletes all Jobs for the Application
* [delete_orgs_org_id_apps_app_id_webhooks_job_id_](docs/sdks/event/README.md#delete_orgs_org_id_apps_app_id_webhooks_job_id_) - Delete a Webhook
* [get_orgs_org_id_apps_app_id_webhooks](docs/sdks/event/README.md#get_orgs_org_id_apps_app_id_webhooks) - List Webhooks
* [get_orgs_org_id_apps_app_id_webhooks_job_id_](docs/sdks/event/README.md#get_orgs_org_id_apps_app_id_webhooks_job_id_) - Get a Webhook
* [get_orgs_org_id_events](docs/sdks/event/README.md#get_orgs_org_id_events) - List Events
* [post_orgs_org_id_apps_app_id_webhooks](docs/sdks/event/README.md#post_orgs_org_id_apps_app_id_webhooks) - Create a new Webhook
* [post_orgs_org_id_apps_app_id_webhooks_job_id_](docs/sdks/event/README.md#post_orgs_org_id_apps_app_id_webhooks_job_id_) - Update a Webhook

### [image](docs/sdks/image/README.md)

* [get_orgs_org_id_images](docs/sdks/image/README.md#get_orgs_org_id_images) - List all Container Images
* [get_orgs_org_id_images_image_id_](docs/sdks/image/README.md#get_orgs_org_id_images_image_id_) - Get a specific Image Object
* [get_orgs_org_id_images_image_id_builds](docs/sdks/image/README.md#get_orgs_org_id_images_image_id_builds) - Lists all the Builds of an Image
* [post_orgs_org_id_images_image_id_builds](docs/sdks/image/README.md#post_orgs_org_id_images_image_id_builds) - Add a new Image Build

### [matching_criteria](docs/sdks/matchingcriteria/README.md)

* [delete_orgs_org_id_resources_defs_def_id_criteria_criteria_id_](docs/sdks/matchingcriteria/README.md#delete_orgs_org_id_resources_defs_def_id_criteria_criteria_id_) - Delete a Matching Criteria from a Resource Definition.
* [post_orgs_org_id_resources_defs_def_id_criteria](docs/sdks/matchingcriteria/README.md#post_orgs_org_id_resources_defs_def_id_criteria) - Add a new Matching Criteria to a Resource Definition.

### [organization](docs/sdks/organization/README.md)

* [get_orgs](docs/sdks/organization/README.md#get_orgs) - List active organizations the user has access to.
* [get_orgs_org_id_](docs/sdks/organization/README.md#get_orgs_org_id_) - Get the specified Organization.

### [registry](docs/sdks/registry/README.md)

* [delete_orgs_org_id_registries_reg_id_](docs/sdks/registry/README.md#delete_orgs_org_id_registries_reg_id_) - Deletes an existing registry record and all associated credentials and secrets.
* [get_orgs_org_id_registries](docs/sdks/registry/README.md#get_orgs_org_id_registries) - Lists available registries for the organization.
* [get_orgs_org_id_registries_reg_id_](docs/sdks/registry/README.md#get_orgs_org_id_registries_reg_id_) - Loads a registry record details.
* [get_orgs_org_id_registries_reg_id_creds](docs/sdks/registry/README.md#get_orgs_org_id_registries_reg_id_creds) - Returns current account credentials or secret details for the registry.
* [patch_orgs_org_id_registries_reg_id_](docs/sdks/registry/README.md#patch_orgs_org_id_registries_reg_id_) - Updates (patches) an existing registry record.
* [post_orgs_org_id_registries](docs/sdks/registry/README.md#post_orgs_org_id_registries) - Creates a new registry record.

### [resource_account](docs/sdks/resourceaccount/README.md)

* [get_orgs_org_id_resources_accounts](docs/sdks/resourceaccount/README.md#get_orgs_org_id_resources_accounts) - List Resource Accounts in the organization.
* [get_orgs_org_id_resources_accounts_acc_id_](docs/sdks/resourceaccount/README.md#get_orgs_org_id_resources_accounts_acc_id_) - Get a Resource Account.
* [patch_orgs_org_id_resources_accounts_acc_id_](docs/sdks/resourceaccount/README.md#patch_orgs_org_id_resources_accounts_acc_id_) - Update a Resource Account.
* [post_orgs_org_id_resources_accounts](docs/sdks/resourceaccount/README.md#post_orgs_org_id_resources_accounts) - Create a new Resource Account in the organization.

### [resource_definition](docs/sdks/resourcedefinition/README.md)

* [delete_orgs_org_id_resources_defs_def_id_](docs/sdks/resourcedefinition/README.md#delete_orgs_org_id_resources_defs_def_id_) - Delete a Resource Definition.
* [delete_orgs_org_id_resources_defs_def_id_criteria_criteria_id_](docs/sdks/resourcedefinition/README.md#delete_orgs_org_id_resources_defs_def_id_criteria_criteria_id_) - Delete a Matching Criteria from a Resource Definition.
* [get_orgs_org_id_resources_defs](docs/sdks/resourcedefinition/README.md#get_orgs_org_id_resources_defs) - List Resource Definitions.
* [get_orgs_org_id_resources_defs_def_id_](docs/sdks/resourcedefinition/README.md#get_orgs_org_id_resources_defs_def_id_) - Get a specific Resource Definition.
* [get_orgs_org_id_resources_defs_def_id_resources](docs/sdks/resourcedefinition/README.md#get_orgs_org_id_resources_defs_def_id_resources) - List Active Resources provisioned via a specific Resource Definition.
* [patch_orgs_org_id_resources_defs_def_id_](docs/sdks/resourcedefinition/README.md#patch_orgs_org_id_resources_defs_def_id_) - Update a Resource Definition.
* [post_orgs_org_id_resources_defs](docs/sdks/resourcedefinition/README.md#post_orgs_org_id_resources_defs) - Create a new Resource Definition.
* [post_orgs_org_id_resources_defs_def_id_criteria](docs/sdks/resourcedefinition/README.md#post_orgs_org_id_resources_defs_def_id_criteria) - Add a new Matching Criteria to a Resource Definition.
* [put_orgs_org_id_resources_defs_def_id_](docs/sdks/resourcedefinition/README.md#put_orgs_org_id_resources_defs_def_id_) - Update a Resource Definition.

### [resource_type](docs/sdks/resourcetype/README.md)

* [get_orgs_org_id_resources_types](docs/sdks/resourcetype/README.md#get_orgs_org_id_resources_types) - List Resource Types.

### [runtime_info](docs/sdks/runtimeinfo/README.md)

* [get_orgs_org_id_apps_app_id_envs_env_id_runtime](docs/sdks/runtimeinfo/README.md#get_orgs_org_id_apps_app_id_envs_env_id_runtime) - Get Runtime information about the environment.
* [get_orgs_org_id_apps_app_id_runtime](docs/sdks/runtimeinfo/README.md#get_orgs_org_id_apps_app_id_runtime) - Get Runtime information about specific environments.
* [patch_orgs_org_id_apps_app_id_envs_env_id_runtime_replicas](docs/sdks/runtimeinfo/README.md#patch_orgs_org_id_apps_app_id_envs_env_id_runtime_replicas) - Set number of replicas for an environment's modules.
* [put_orgs_org_id_apps_app_id_envs_env_id_runtime_paused](docs/sdks/runtimeinfo/README.md#put_orgs_org_id_apps_app_id_envs_env_id_runtime_paused) - Pause / Resume an environment.

### [set](docs/sdks/set/README.md)

* [get_sets](docs/sdks/set/README.md#get_sets) - Get all Deployment Sets
* [get_orgs_org_id_apps_app_id_sets_set_id_](docs/sdks/set/README.md#get_orgs_org_id_apps_app_id_sets_set_id_) - Get a Deployment Set
* [get_orgs_org_id_apps_app_id_sets_set_id_diff_source_set_id_](docs/sdks/set/README.md#get_orgs_org_id_apps_app_id_sets_set_id_diff_source_set_id_) - Get the difference between 2 Deployment Sets
* [post_orgs_org_id_apps_app_id_sets_set_id_](docs/sdks/set/README.md#post_orgs_org_id_apps_app_id_sets_set_id_) - Apply a Deployment Delta to a Deployment Set

### [user_invite](docs/sdks/userinvite/README.md)

* [get_orgs_org_id_invitations](docs/sdks/userinvite/README.md#get_orgs_org_id_invitations) - List the invites issued for the organization.

### [user_profile](docs/sdks/userprofile/README.md)

* [delete_tokens_token_id_](docs/sdks/userprofile/README.md#delete_tokens_token_id_) - DEPRECATED
* [get_current_user](docs/sdks/userprofile/README.md#get_current_user) - Gets the extended profile of the current user
* [get_tokens](docs/sdks/userprofile/README.md#get_tokens) - DEPRECATED
* [get_users_me](docs/sdks/userprofile/README.md#get_users_me) - DEPRECATED
* [patch_current_user](docs/sdks/userprofile/README.md#patch_current_user) - Updates the extended profile of the current user.
* [post_orgs_org_id_users](docs/sdks/userprofile/README.md#post_orgs_org_id_users) - Creates a new service user.

### [user_role](docs/sdks/userrole/README.md)

* [delete_orgs_org_id_apps_app_id_users_user_id_](docs/sdks/userrole/README.md#delete_orgs_org_id_apps_app_id_users_user_id_) - Remove the role of a User on an Application
* [delete_orgs_org_id_env_types_env_type_users_user_id_](docs/sdks/userrole/README.md#delete_orgs_org_id_env_types_env_type_users_user_id_) - Remove the role of a User on an Environment Type
* [delete_orgs_org_id_users_user_id_](docs/sdks/userrole/README.md#delete_orgs_org_id_users_user_id_) - Remove the role of a User on an Organization
* [get_orgs_org_id_apps_app_id_users](docs/sdks/userrole/README.md#get_orgs_org_id_apps_app_id_users) - List Users with roles in an App
* [get_orgs_org_id_apps_app_id_users_user_id_](docs/sdks/userrole/README.md#get_orgs_org_id_apps_app_id_users_user_id_) - Get the role of a User on an Application
* [get_orgs_org_id_env_types_env_type_users_user_id_](docs/sdks/userrole/README.md#get_orgs_org_id_env_types_env_type_users_user_id_) - Get the role of a User on an Environment Type
* [get_orgs_org_id_users](docs/sdks/userrole/README.md#get_orgs_org_id_users) - List Users with roles in an Organization
* [get_orgs_org_id_users_user_id_](docs/sdks/userrole/README.md#get_orgs_org_id_users_user_id_) - Get the role of a User on an Organization
* [patch_orgs_org_id_apps_app_id_users_user_id_](docs/sdks/userrole/README.md#patch_orgs_org_id_apps_app_id_users_user_id_) - Update the role of a User on an Application
* [patch_orgs_org_id_env_types_env_type_users_user_id_](docs/sdks/userrole/README.md#patch_orgs_org_id_env_types_env_type_users_user_id_) - Update the role of a User on an Environment Type
* [patch_orgs_org_id_users_user_id_](docs/sdks/userrole/README.md#patch_orgs_org_id_users_user_id_) - Update the role of a User on an Organization
* [post_orgs_org_id_apps_app_id_users](docs/sdks/userrole/README.md#post_orgs_org_id_apps_app_id_users) - Adds a User to an Application with a Role
* [post_orgs_org_id_env_types_env_type_users](docs/sdks/userrole/README.md#post_orgs_org_id_env_types_env_type_users) - Adds a User to an Environment Type with a Role
* [post_orgs_org_id_invitations](docs/sdks/userrole/README.md#post_orgs_org_id_invitations) - Invites a user to an Organization with a specified role.

### [value](docs/sdks/value/README.md)

* [delete_orgs_org_id_apps_app_id_envs_env_id_values](docs/sdks/value/README.md#delete_orgs_org_id_apps_app_id_envs_env_id_values) - Delete all Shared Value for an Environment
* [delete_orgs_org_id_apps_app_id_envs_env_id_values_key_](docs/sdks/value/README.md#delete_orgs_org_id_apps_app_id_envs_env_id_values_key_) - Delete Shared Value for an Environment
* [delete_orgs_org_id_apps_app_id_values](docs/sdks/value/README.md#delete_orgs_org_id_apps_app_id_values) - Delete all Shared Value for an App
* [delete_orgs_org_id_apps_app_id_values_key_](docs/sdks/value/README.md#delete_orgs_org_id_apps_app_id_values_key_) - Delete Shared Value for an Application
* [get_orgs_org_id_apps_app_id_envs_env_id_values](docs/sdks/value/README.md#get_orgs_org_id_apps_app_id_envs_env_id_values) - List Shared Values in an Environment
* [get_orgs_org_id_apps_app_id_values](docs/sdks/value/README.md#get_orgs_org_id_apps_app_id_values) - List Shared Values in an Application
* [patch_orgs_org_id_apps_app_id_envs_env_id_values_key_](docs/sdks/value/README.md#patch_orgs_org_id_apps_app_id_envs_env_id_values_key_) - Update Shared Value for an Environment
* [patch_orgs_org_id_apps_app_id_values_key_](docs/sdks/value/README.md#patch_orgs_org_id_apps_app_id_values_key_) - Update Shared Value for an Application
* [post_orgs_org_id_apps_app_id_envs_env_id_values](docs/sdks/value/README.md#post_orgs_org_id_apps_app_id_envs_env_id_values) - Create a Shared Value for an Environment
* [post_orgs_org_id_apps_app_id_values](docs/sdks/value/README.md#post_orgs_org_id_apps_app_id_values) - Create a Shared Value for an Application
* [put_orgs_org_id_apps_app_id_envs_env_id_values_key_](docs/sdks/value/README.md#put_orgs_org_id_apps_app_id_envs_env_id_values_key_) - Update Shared Value for an Environment
* [put_orgs_org_id_apps_app_id_values_key_](docs/sdks/value/README.md#put_orgs_org_id_apps_app_id_values_key_) - Update Shared Value for an Application

### [value_set_version](docs/sdks/valuesetversion/README.md)

* [get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions](docs/sdks/valuesetversion/README.md#get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions) - List Value Set Versions in an Environment of an App
* [get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_](docs/sdks/valuesetversion/README.md#get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_) - Get a single Value Set Version in an Environment of an App
* [get_orgs_org_id_apps_app_id_value_set_versions](docs/sdks/valuesetversion/README.md#get_orgs_org_id_apps_app_id_value_set_versions) - List Value Set Versions in the App
* [get_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_](docs/sdks/valuesetversion/README.md#get_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_) - Get a single Value Set Version from the App
* [post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_purge_key_](docs/sdks/valuesetversion/README.md#post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_purge_key_) - Purge the value of a specific Shared Value from the App Environment Version history.
* [post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore](docs/sdks/valuesetversion/README.md#post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore) - Restore a Value Set Version in an Environment of an App
* [post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore_key_](docs/sdks/valuesetversion/README.md#post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore_key_) - Restore a specific key from the Value Set Version in an Environment of an App
* [post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_purge_key_](docs/sdks/valuesetversion/README.md#post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_purge_key_) - Purge the value of a specific Shared Value from the App Version history.
* [post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore](docs/sdks/valuesetversion/README.md#post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore) - Restore a Value Set Version in an App
* [post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore_key_](docs/sdks/valuesetversion/README.md#post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore_key_) - Restore a specific key from the Value Set Version in an App

### [workload_profile](docs/sdks/workloadprofile/README.md)

* [delete_orgs_org_id_workload_profiles_profile_id_versions_version_](docs/sdks/workloadprofile/README.md#delete_orgs_org_id_workload_profiles_profile_id_versions_version_) - Delete a Workload Profile Version
* [delete_orgs_org_id_workload_profiles_profile_qid_](docs/sdks/workloadprofile/README.md#delete_orgs_org_id_workload_profiles_profile_qid_) - Delete a Workload Profile
* [get_orgs_org_id_workload_profiles](docs/sdks/workloadprofile/README.md#get_orgs_org_id_workload_profiles) - List workload profiles available to the organization.
* [get_orgs_org_id_workload_profiles_profile_qid_](docs/sdks/workloadprofile/README.md#get_orgs_org_id_workload_profiles_profile_qid_) - Get a Workload Profile
* [get_orgs_org_id_workload_profiles_profile_qid_versions](docs/sdks/workloadprofile/README.md#get_orgs_org_id_workload_profiles_profile_qid_versions) - List versions of the given workload profile with optional constraint.
* [post_orgs_org_id_workload_profiles](docs/sdks/workloadprofile/README.md#post_orgs_org_id_workload_profiles) - Create new Workload Profile
* [post_orgs_org_id_workload_profiles_profile_qid_versions](docs/sdks/workloadprofile/README.md#post_orgs_org_id_workload_profiles_profile_qid_versions) - Add new Version of the Workload Profile

### [public](docs/sdks/public/README.md)

* [delete_orgs_org_id_apps_app_id_](docs/sdks/public/README.md#delete_orgs_org_id_apps_app_id_) - Delete an Application
* [delete_orgs_org_id_apps_app_id_envs_env_id_](docs/sdks/public/README.md#delete_orgs_org_id_apps_app_id_envs_env_id_) - Delete a specific Environment.
* [delete_orgs_org_id_apps_app_id_envs_env_id_resources_type_res_id_](docs/sdks/public/README.md#delete_orgs_org_id_apps_app_id_envs_env_id_resources_type_res_id_) - Delete Active Resources.
* [delete_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_](docs/sdks/public/README.md#delete_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_) - Delete Automation Rule from an Environment.
* [delete_orgs_org_id_apps_app_id_envs_env_id_values](docs/sdks/public/README.md#delete_orgs_org_id_apps_app_id_envs_env_id_values) - Delete all Shared Value for an Environment
* [delete_orgs_org_id_apps_app_id_envs_env_id_values_key_](docs/sdks/public/README.md#delete_orgs_org_id_apps_app_id_envs_env_id_values_key_) - Delete Shared Value for an Environment
* [delete_orgs_org_id_apps_app_id_jobs](docs/sdks/public/README.md#delete_orgs_org_id_apps_app_id_jobs) - Deletes all Jobs for the Application
* [delete_orgs_org_id_apps_app_id_users_user_id_](docs/sdks/public/README.md#delete_orgs_org_id_apps_app_id_users_user_id_) - Remove the role of a User on an Application
* [delete_orgs_org_id_apps_app_id_values](docs/sdks/public/README.md#delete_orgs_org_id_apps_app_id_values) - Delete all Shared Value for an App
* [delete_orgs_org_id_apps_app_id_values_key_](docs/sdks/public/README.md#delete_orgs_org_id_apps_app_id_values_key_) - Delete Shared Value for an Application
* [delete_orgs_org_id_apps_app_id_webhooks_job_id_](docs/sdks/public/README.md#delete_orgs_org_id_apps_app_id_webhooks_job_id_) - Delete a Webhook
* [delete_orgs_org_id_artefacts_artefact_id_](docs/sdks/public/README.md#delete_orgs_org_id_artefacts_artefact_id_) - Delete Artefact and all related Artefact Versions
* [delete_orgs_org_id_env_types_env_type_id_](docs/sdks/public/README.md#delete_orgs_org_id_env_types_env_type_id_) - Deletes an Environment Type
* [delete_orgs_org_id_env_types_env_type_users_user_id_](docs/sdks/public/README.md#delete_orgs_org_id_env_types_env_type_users_user_id_) - Remove the role of a User on an Environment Type
* [delete_orgs_org_id_registries_reg_id_](docs/sdks/public/README.md#delete_orgs_org_id_registries_reg_id_) - Deletes an existing registry record and all associated credentials and secrets.
* [delete_orgs_org_id_resources_defs_def_id_](docs/sdks/public/README.md#delete_orgs_org_id_resources_defs_def_id_) - Delete a Resource Definition.
* [delete_orgs_org_id_resources_defs_def_id_criteria_criteria_id_](docs/sdks/public/README.md#delete_orgs_org_id_resources_defs_def_id_criteria_criteria_id_) - Delete a Matching Criteria from a Resource Definition.
* [delete_orgs_org_id_resources_drivers_driver_id_](docs/sdks/public/README.md#delete_orgs_org_id_resources_drivers_driver_id_) - Delete a Resources Driver.
* [delete_orgs_org_id_users_user_id_](docs/sdks/public/README.md#delete_orgs_org_id_users_user_id_) - Remove the role of a User on an Organization
* [delete_orgs_org_id_workload_profiles_profile_id_versions_version_](docs/sdks/public/README.md#delete_orgs_org_id_workload_profiles_profile_id_versions_version_) - Delete a Workload Profile Version
* [delete_orgs_org_id_workload_profiles_profile_qid_](docs/sdks/public/README.md#delete_orgs_org_id_workload_profiles_profile_qid_) - Delete a Workload Profile
* [delete_tokens_token_id_](docs/sdks/public/README.md#delete_tokens_token_id_) - DEPRECATED
* [get_delta](docs/sdks/public/README.md#get_delta) - Fetch an existing Delta
* [get_sets](docs/sdks/public/README.md#get_sets) - Get all Deployment Sets
* [get_current_user](docs/sdks/public/README.md#get_current_user) - Gets the extended profile of the current user
* [get_orgs](docs/sdks/public/README.md#get_orgs) - List active organizations the user has access to.
* [get_orgs_org_id_](docs/sdks/public/README.md#get_orgs_org_id_) - Get the specified Organization.
* [get_orgs_org_id_apps](docs/sdks/public/README.md#get_orgs_org_id_apps) - List all Applications in an Organization.
* [get_orgs_org_id_apps_app_id_](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_) - Get an existing Application
* [get_orgs_org_id_apps_app_id_deltas](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_deltas) - List Deltas in an Application
* [get_orgs_org_id_apps_app_id_envs](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_envs) - List all Environments.
* [get_orgs_org_id_apps_app_id_envs_env_id_](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_envs_env_id_) - Get a specific Environment.
* [get_orgs_org_id_apps_app_id_envs_env_id_deploys](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_envs_env_id_deploys) - List Deployments in an Environment.
* [get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_) - Get a specific Deployment.
* [get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_errors](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_envs_env_id_deploys_deploy_id_errors) - List errors that occurred in a Deployment.
* [get_orgs_org_id_apps_app_id_envs_env_id_resources](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_envs_env_id_resources) - List Active Resources provisioned in an environment.
* [get_orgs_org_id_apps_app_id_envs_env_id_rules](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_envs_env_id_rules) - List all Automation Rules in an Environment.
* [get_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_) - Get a specific Automation Rule for an Environment.
* [get_orgs_org_id_apps_app_id_envs_env_id_runtime](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_envs_env_id_runtime) - Get Runtime information about the environment.
* [get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions) - List Value Set Versions in an Environment of an App
* [get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_) - Get a single Value Set Version in an Environment of an App
* [get_orgs_org_id_apps_app_id_envs_env_id_values](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_envs_env_id_values) - List Shared Values in an Environment
* [get_orgs_org_id_apps_app_id_runtime](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_runtime) - Get Runtime information about specific environments.
* [get_orgs_org_id_apps_app_id_sets_set_id_](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_sets_set_id_) - Get a Deployment Set
* [get_orgs_org_id_apps_app_id_sets_set_id_diff_source_set_id_](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_sets_set_id_diff_source_set_id_) - Get the difference between 2 Deployment Sets
* [get_orgs_org_id_apps_app_id_users](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_users) - List Users with roles in an App
* [get_orgs_org_id_apps_app_id_users_user_id_](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_users_user_id_) - Get the role of a User on an Application
* [get_orgs_org_id_apps_app_id_value_set_versions](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_value_set_versions) - List Value Set Versions in the App
* [get_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_) - Get a single Value Set Version from the App
* [get_orgs_org_id_apps_app_id_values](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_values) - List Shared Values in an Application
* [get_orgs_org_id_apps_app_id_webhooks](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_webhooks) - List Webhooks
* [get_orgs_org_id_apps_app_id_webhooks_job_id_](docs/sdks/public/README.md#get_orgs_org_id_apps_app_id_webhooks_job_id_) - Get a Webhook
* [get_orgs_org_id_artefact_versions](docs/sdks/public/README.md#get_orgs_org_id_artefact_versions) - List all Artefacts Versions.
* [get_orgs_org_id_artefact_versions_artefact_version_id_](docs/sdks/public/README.md#get_orgs_org_id_artefact_versions_artefact_version_id_) - Get an Artefacts Versions.
* [get_orgs_org_id_artefacts](docs/sdks/public/README.md#get_orgs_org_id_artefacts) - List all Artefacts.
* [get_orgs_org_id_artefacts_artefact_id_versions](docs/sdks/public/README.md#get_orgs_org_id_artefacts_artefact_id_versions) - List all Artefact Versions of an Artefact.
* [get_orgs_org_id_env_types](docs/sdks/public/README.md#get_orgs_org_id_env_types) - List all Environment Types
* [get_orgs_org_id_env_types_env_type_id_](docs/sdks/public/README.md#get_orgs_org_id_env_types_env_type_id_) - Get an Environment Type
* [get_orgs_org_id_env_types_env_type_users_user_id_](docs/sdks/public/README.md#get_orgs_org_id_env_types_env_type_users_user_id_) - Get the role of a User on an Environment Type
* [get_orgs_org_id_events](docs/sdks/public/README.md#get_orgs_org_id_events) - List Events
* [get_orgs_org_id_images](docs/sdks/public/README.md#get_orgs_org_id_images) - List all Container Images
* [get_orgs_org_id_images_image_id_](docs/sdks/public/README.md#get_orgs_org_id_images_image_id_) - Get a specific Image Object
* [get_orgs_org_id_images_image_id_builds](docs/sdks/public/README.md#get_orgs_org_id_images_image_id_builds) - Lists all the Builds of an Image
* [get_orgs_org_id_invitations](docs/sdks/public/README.md#get_orgs_org_id_invitations) - List the invites issued for the organization.
* [get_orgs_org_id_registries](docs/sdks/public/README.md#get_orgs_org_id_registries) - Lists available registries for the organization.
* [get_orgs_org_id_registries_reg_id_](docs/sdks/public/README.md#get_orgs_org_id_registries_reg_id_) - Loads a registry record details.
* [get_orgs_org_id_registries_reg_id_creds](docs/sdks/public/README.md#get_orgs_org_id_registries_reg_id_creds) - Returns current account credentials or secret details for the registry.
* [get_orgs_org_id_resources_account_types](docs/sdks/public/README.md#get_orgs_org_id_resources_account_types) - List Resource Account Types available to the organization.
* [get_orgs_org_id_resources_accounts](docs/sdks/public/README.md#get_orgs_org_id_resources_accounts) - List Resource Accounts in the organization.
* [get_orgs_org_id_resources_accounts_acc_id_](docs/sdks/public/README.md#get_orgs_org_id_resources_accounts_acc_id_) - Get a Resource Account.
* [get_orgs_org_id_resources_defs](docs/sdks/public/README.md#get_orgs_org_id_resources_defs) - List Resource Definitions.
* [get_orgs_org_id_resources_defs_def_id_](docs/sdks/public/README.md#get_orgs_org_id_resources_defs_def_id_) - Get a specific Resource Definition.
* [get_orgs_org_id_resources_defs_def_id_resources](docs/sdks/public/README.md#get_orgs_org_id_resources_defs_def_id_resources) - List Active Resources provisioned via a specific Resource Definition.
* [get_orgs_org_id_resources_drivers](docs/sdks/public/README.md#get_orgs_org_id_resources_drivers) - List Resource Drivers.
* [get_orgs_org_id_resources_drivers_driver_id_](docs/sdks/public/README.md#get_orgs_org_id_resources_drivers_driver_id_) - Get a Resource Driver.
* [get_orgs_org_id_resources_types](docs/sdks/public/README.md#get_orgs_org_id_resources_types) - List Resource Types.
* [get_orgs_org_id_users](docs/sdks/public/README.md#get_orgs_org_id_users) - List Users with roles in an Organization
* [get_orgs_org_id_users_user_id_](docs/sdks/public/README.md#get_orgs_org_id_users_user_id_) - Get the role of a User on an Organization
* [get_orgs_org_id_workload_profiles](docs/sdks/public/README.md#get_orgs_org_id_workload_profiles) - List workload profiles available to the organization.
* [get_orgs_org_id_workload_profiles_profile_qid_](docs/sdks/public/README.md#get_orgs_org_id_workload_profiles_profile_qid_) - Get a Workload Profile
* [get_orgs_org_id_workload_profiles_profile_qid_versions](docs/sdks/public/README.md#get_orgs_org_id_workload_profiles_profile_qid_versions) - List versions of the given workload profile with optional constraint.
* [get_tokens](docs/sdks/public/README.md#get_tokens) - DEPRECATED
* [get_users_me](docs/sdks/public/README.md#get_users_me) - DEPRECATED
* [patch_current_user](docs/sdks/public/README.md#patch_current_user) - Updates the extended profile of the current user.
* [patch_orgs_org_id_apps_app_id_deltas_delta_id_](docs/sdks/public/README.md#patch_orgs_org_id_apps_app_id_deltas_delta_id_) - Update an existing Delta
* [patch_orgs_org_id_apps_app_id_envs_env_id_runtime_replicas](docs/sdks/public/README.md#patch_orgs_org_id_apps_app_id_envs_env_id_runtime_replicas) - Set number of replicas for an environment's modules.
* [patch_orgs_org_id_apps_app_id_envs_env_id_values_key_](docs/sdks/public/README.md#patch_orgs_org_id_apps_app_id_envs_env_id_values_key_) - Update Shared Value for an Environment
* [patch_orgs_org_id_apps_app_id_users_user_id_](docs/sdks/public/README.md#patch_orgs_org_id_apps_app_id_users_user_id_) - Update the role of a User on an Application
* [patch_orgs_org_id_apps_app_id_values_key_](docs/sdks/public/README.md#patch_orgs_org_id_apps_app_id_values_key_) - Update Shared Value for an Application
* [patch_orgs_org_id_artefacts_artefact_id_versions_version_id_](docs/sdks/public/README.md#patch_orgs_org_id_artefacts_artefact_id_versions_version_id_) - Update Version of an Artefact.
* [patch_orgs_org_id_env_types_env_type_users_user_id_](docs/sdks/public/README.md#patch_orgs_org_id_env_types_env_type_users_user_id_) - Update the role of a User on an Environment Type
* [patch_orgs_org_id_registries_reg_id_](docs/sdks/public/README.md#patch_orgs_org_id_registries_reg_id_) - Updates (patches) an existing registry record.
* [patch_orgs_org_id_resources_accounts_acc_id_](docs/sdks/public/README.md#patch_orgs_org_id_resources_accounts_acc_id_) - Update a Resource Account.
* [patch_orgs_org_id_resources_defs_def_id_](docs/sdks/public/README.md#patch_orgs_org_id_resources_defs_def_id_) - Update a Resource Definition.
* [patch_orgs_org_id_users_user_id_](docs/sdks/public/README.md#patch_orgs_org_id_users_user_id_) - Update the role of a User on an Organization
* [post_orgs_org_id_apps](docs/sdks/public/README.md#post_orgs_org_id_apps) - Add a new Application to an Organization
* [post_orgs_org_id_apps_app_id_deltas](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_deltas) - Create a new Delta
* [post_orgs_org_id_apps_app_id_envs](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_envs) - Add a new Environment to an Application.
* [post_orgs_org_id_apps_app_id_envs_env_id_deploys](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_envs_env_id_deploys) - Start a new Deployment.
* [post_orgs_org_id_apps_app_id_envs_env_id_rules](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_envs_env_id_rules) - Create a new Automation Rule for an Environment.
* [post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_purge_key_](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_purge_key_) - Purge the value of a specific Shared Value from the App Environment Version history.
* [post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore) - Restore a Value Set Version in an Environment of an App
* [post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore_key_](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_envs_env_id_value_set_versions_value_set_version_id_restore_key_) - Restore a specific key from the Value Set Version in an Environment of an App
* [post_orgs_org_id_apps_app_id_envs_env_id_values](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_envs_env_id_values) - Create a Shared Value for an Environment
* [post_orgs_org_id_apps_app_id_sets_set_id_](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_sets_set_id_) - Apply a Deployment Delta to a Deployment Set
* [post_orgs_org_id_apps_app_id_users](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_users) - Adds a User to an Application with a Role
* [post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_purge_key_](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_purge_key_) - Purge the value of a specific Shared Value from the App Version history.
* [post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore) - Restore a Value Set Version in an App
* [post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore_key_](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_value_set_versions_value_set_version_id_restore_key_) - Restore a specific key from the Value Set Version in an App
* [post_orgs_org_id_apps_app_id_values](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_values) - Create a Shared Value for an Application
* [post_orgs_org_id_apps_app_id_webhooks](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_webhooks) - Create a new Webhook
* [post_orgs_org_id_apps_app_id_webhooks_job_id_](docs/sdks/public/README.md#post_orgs_org_id_apps_app_id_webhooks_job_id_) - Update a Webhook
* [post_orgs_org_id_artefact_versions](docs/sdks/public/README.md#post_orgs_org_id_artefact_versions) - Register a new Artefact Version with your organization.
* [post_orgs_org_id_env_types](docs/sdks/public/README.md#post_orgs_org_id_env_types) - Add a new Environment Type
* [post_orgs_org_id_env_types_env_type_users](docs/sdks/public/README.md#post_orgs_org_id_env_types_env_type_users) - Adds a User to an Environment Type with a Role
* [post_orgs_org_id_images_image_id_builds](docs/sdks/public/README.md#post_orgs_org_id_images_image_id_builds) - Add a new Image Build
* [post_orgs_org_id_invitations](docs/sdks/public/README.md#post_orgs_org_id_invitations) - Invites a user to an Organization with a specified role.
* [post_orgs_org_id_registries](docs/sdks/public/README.md#post_orgs_org_id_registries) - Creates a new registry record.
* [post_orgs_org_id_resources_accounts](docs/sdks/public/README.md#post_orgs_org_id_resources_accounts) - Create a new Resource Account in the organization.
* [post_orgs_org_id_resources_defs](docs/sdks/public/README.md#post_orgs_org_id_resources_defs) - Create a new Resource Definition.
* [post_orgs_org_id_resources_defs_def_id_criteria](docs/sdks/public/README.md#post_orgs_org_id_resources_defs_def_id_criteria) - Add a new Matching Criteria to a Resource Definition.
* [post_orgs_org_id_resources_drivers](docs/sdks/public/README.md#post_orgs_org_id_resources_drivers) - Register a new Resource Driver.
* [post_orgs_org_id_users](docs/sdks/public/README.md#post_orgs_org_id_users) - Creates a new service user.
* [post_orgs_org_id_workload_profiles](docs/sdks/public/README.md#post_orgs_org_id_workload_profiles) - Create new Workload Profile
* [post_orgs_org_id_workload_profiles_profile_qid_versions](docs/sdks/public/README.md#post_orgs_org_id_workload_profiles_profile_qid_versions) - Add new Version of the Workload Profile
* [put_delta](docs/sdks/public/README.md#put_delta) - Update an existing Delta
* [put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_archived](docs/sdks/public/README.md#put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_archived) - Mark a Delta as "archived"
* [put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_env_id](docs/sdks/public/README.md#put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_env_id) - Change the Environment of a Delta
* [put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_name](docs/sdks/public/README.md#put_orgs_org_id_apps_app_id_deltas_delta_id_metadata_name) - Change the name of a Delta
* [put_orgs_org_id_apps_app_id_envs_env_id_from_deploy_id](docs/sdks/public/README.md#put_orgs_org_id_apps_app_id_envs_env_id_from_deploy_id) - Rebase to a different Deployment.
* [put_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_](docs/sdks/public/README.md#put_orgs_org_id_apps_app_id_envs_env_id_rules_rule_id_) - Update an existing Automation Rule for an Environment.
* [put_orgs_org_id_apps_app_id_envs_env_id_runtime_paused](docs/sdks/public/README.md#put_orgs_org_id_apps_app_id_envs_env_id_runtime_paused) - Pause / Resume an environment.
* [put_orgs_org_id_apps_app_id_envs_env_id_values_key_](docs/sdks/public/README.md#put_orgs_org_id_apps_app_id_envs_env_id_values_key_) - Update Shared Value for an Environment
* [put_orgs_org_id_apps_app_id_values_key_](docs/sdks/public/README.md#put_orgs_org_id_apps_app_id_values_key_) - Update Shared Value for an Application
* [put_orgs_org_id_resources_defs_def_id_](docs/sdks/public/README.md#put_orgs_org_id_resources_defs_def_id_) - Update a Resource Definition.
* [put_orgs_org_id_resources_drivers_driver_id_](docs/sdks/public/README.md#put_orgs_org_id_resources_drivers_driver_id_) - Update a Resource Driver.
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
