"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test1 import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeploymentResponse:
    r"""Deployments represent updates to the running state of an Environment.
    
    Deployments are made by applying _Deltas_ to a state defined by an existing Deployment. The Environment’s from_deploy property defines the Deployment. This Deployment is usually but not always in the current Environment. If the Deployment is from another Environment, the state of that Environment will be \"cloned\" into the current Environment with the option to apply a Delta.
    """
    
    comment: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('comment') }})
    r"""An optional comment to help communicate the purpose of the Deployment."""
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at') }})
    r"""The Timestamp of when the Deployment was initiated."""
    created_by: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_by') }})
    r"""The user who initiated the Deployment."""
    env_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('env_id') }})
    r"""The Environment where the Deployment occurred."""
    export_file: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('export_file') }})
    export_status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('export_status') }})
    from_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from_id') }})
    r"""The ID of the Deployment that this Deployment was based on."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The ID of the Deployment."""
    set_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('set_id') }})
    r"""ID of the Deployment Set describing the state of the Environment after Deployment."""
    status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""The current status of the Deployment. Can be `pending`, `in progress`, `succeeded`, or `failed`."""
    status_changed_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status_changed_at') }})
    r"""The timestamp of the last `status` change. If `status` is `succeeded` or `failed` it it will indicate when the Deployment finished."""
    delta_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delta_id'), 'exclude': lambda f: f is None }})
    r"""ID of the Deployment Delta describing the changes to the current Environment for this Deployment."""
    value_set_version_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value_set_version_id'), 'exclude': lambda f: f is None }})
    r"""ID of the Value Set Version describe the values to be used for this Deployment."""
    