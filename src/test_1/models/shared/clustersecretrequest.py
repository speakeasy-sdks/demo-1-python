"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from test_1 import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ClusterSecretRequest:
    r"""ClusterSecret represents Kubernetes secret reference."""
    namespace: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespace') }})
    r"""Namespace to look for the Kubernetes secret definition in."""
    secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret') }})
    r"""Name that identifies the Kubernetes secret."""
    

