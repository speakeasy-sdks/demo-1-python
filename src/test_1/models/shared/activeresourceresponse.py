"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_1 import utils
from typing import Any


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ActiveResourceResponse:
    r"""Active Resources represent the concrete resources provisioned for an Environment. They are provisioned on the first deployment after a dependency on a particular resource type is introduced into an Environment. In general, Active Resources are only deleted when their introductory Environment is deleted.
    
    Active Resources are provisioned based on a Resource Definition. The Resource Definition describes how to provision a concrete resource based on a Resource Type and metadata about the Environment (for example the Environment Type or the Application ID). The criteria for how to choose a Resource Definition is known as a Matching Criteria. If the Matching Criteria changes or the Resource Definition is deleted, the concrete resource represented by an Active Resource might be deleted and reprovisioned when a deployment occurs in the Environment.
    """
    app_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app_id') }})
    r"""The ID of the App the resource is associated with."""
    def_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('def_id') }})
    r"""The Resource Definition that this resource was provisioned from."""
    deploy_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deploy_id') }})
    r"""The deployment that the resource was last provisioned in."""
    env_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('env_id') }})
    r"""The ID of the Environment the resource is associated with."""
    env_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('env_type') }})
    r"""The Environment Type of the Environment specified by env_id."""
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_id') }})
    r"""the ID of the Organization the Active Resource is associated with."""
    res_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('res_id') }})
    r"""The ID of the resource"""
    resource: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource') }})
    r"""The data that the resource passes into the deployment ('values' only)."""
    status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Current resource status: 'pending', 'active', or 'deleting'."""
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The Resource Type of the resource"""
    updated_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at') }})
    r"""The time the resource was last provisioned as part of a deployment."""
    

