"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test1 import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WorkloadProfileVersionRequest:
    r"""Each Workload Profile has one or more Versions associated with it. In order to add a version, a Workload Profile must first be created."""
    
    features: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('features'), 'exclude': lambda f: f is None }})
    r"""A map of Features. If referencing built in Humanitec features, the fully qualified feature name must be used: e.g. `humanitec/annotations`.
    
    {
    
    }
    """
    notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notes'), 'exclude': lambda f: f is None }})
    r"""Notes"""
    