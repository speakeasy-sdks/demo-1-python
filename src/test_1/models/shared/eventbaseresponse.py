"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_1 import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class EventBaseResponse:
    r"""Properties which identify an event ."""
    scope: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scope') }})
    r"""Event scope"""
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Event type"""
    

