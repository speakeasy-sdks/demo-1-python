"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import controllerresponse as shared_controllerresponse
from ..shared import updateactionresponse as shared_updateactionresponse
from dataclasses_json import Undefined, dataclass_json
from test_1 import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ModuleDeltasResponse:
    r"""ModuleDeltas groups the different operations together."""
    add: dict[str, dict[str, shared_controllerresponse.ControllerResponse]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('add') }})
    remove: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('remove') }})
    update: dict[str, list[shared_updateactionresponse.UpdateActionResponse]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('update') }})
    

