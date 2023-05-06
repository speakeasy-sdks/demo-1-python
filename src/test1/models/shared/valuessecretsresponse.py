"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test1 import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ValuesSecretsResponse:
    r"""ValuesSecrets stores data that should be passed around split by sensitivity."""
    
    secrets: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secrets'), 'exclude': lambda f: f is None }})
    r"""Secrets section of the data set. Sensitive information is stored in the Vault and replaced with the Vault paths when sent outside."""
    values: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('values'), 'exclude': lambda f: f is None }})
    r"""Values section of the data set. Passed around as-is."""
    