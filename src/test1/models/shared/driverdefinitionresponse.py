"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test1 import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DriverDefinitionResponse:
    r"""DriverDefinition describes the resource driver.
    
    Resource Drivers are code that fulfils the Humanitec Resource Driver Interface. This interface allows for certain actions to be performed on resources such as creation and destruction. Humanitec provides numerous Resource Drivers “out of the box”. It is also possible to use 3rd party Resource Drivers or write your own.
    """
    
    account_types: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_types') }})
    r"""List of resources accounts types supported by the driver"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The ID for this driver. Is used as `driver_type`."""
    inputs_schema: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inputs_schema') }})
    r"""A JSON Schema specifying the driver-specific input parameters."""
    is_public: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_public') }})
    r"""Defines whether this driver is accessible to all Organizations."""
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_id') }})
    r"""The Organization this driver exists under. Useful as public drivers are accessible to other orgs."""
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of resource produced by this driver"""
    target: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target'), 'exclude': lambda f: f is None }})
    r"""The prefix where the driver resides or, if the driver is a virtual driver, the reference to an existing driver using the `driver://` schema of the format `driver://{orgId}/{driverId}`. Only members of the organization the driver belongs to can see `target`."""
    template: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('template'), 'exclude': lambda f: f is None }})
    r"""If the driver is a virtual driver, template defines a Go template that converts the driver inputs supplied in the resource definition into the driver inputs for the target driver."""
    