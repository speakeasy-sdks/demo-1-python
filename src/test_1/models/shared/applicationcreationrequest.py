"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import environmentbaserequest as shared_environmentbaserequest
from dataclasses_json import Undefined, dataclass_json
from test_1 import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ApplicationCreationRequest:
    r"""The request ID, Human-friendly name and environment of the Application."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The ID which refers to a specific application."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The Human-friendly name for the Application."""
    env: Optional[shared_environmentbaserequest.EnvironmentBaseRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('env'), 'exclude': lambda f: f is None }})
    

