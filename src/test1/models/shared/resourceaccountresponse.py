"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test1 import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ResourceAccountResponse:
    r"""ResourceAccount represents the account being used to access a resource.
    
    Resource Accounts hold credentials that are required to provision and manage resources.
    """
    
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at') }})
    r"""The timestamp of when the account was created."""
    created_by: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_by') }})
    r"""The ID of the user who created the account."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique identifier for the account (in scope of the organization it belongs to)."""
    is_used: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_used') }})
    r"""Indicates if this account is being used (referenced) by any resource definition."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Display name."""
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of the account"""
    