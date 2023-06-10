"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_1 import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class EnvironmentDefinitionRequest:
    r"""The ID, Name, Type, and Deployment the Environment will be derived from."""
    from_deploy_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from_deploy_id') }})
    r"""Defines the existing Deployment the new Environment will be based on."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The ID the Environment is referenced as."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The Human-friendly name for the Environment."""
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The Environment Type. This is used for organizing and managing Environments."""
    

