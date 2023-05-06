"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import deltametadatarequest as shared_deltametadatarequest
from ..shared import moduledeltasrequest as shared_moduledeltasrequest
from ..shared import updateactionrequest as shared_updateactionrequest
from dataclasses_json import Undefined, dataclass_json
from test1 import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeltaRequest:
    r"""A Deployment Delta (or just \\"Delta\\") describes the changes that must be applied to one Deployment Set to generate another Deployment Set. Deployment Deltas are the only way to create new Deployment Sets.
    
    Deployment Deltas can be created fully formed or combined together via PATCHing. They can also be generated from the difference between two Deployment Sets.
    
    **Basic Structure**
    
    ```
     {
       \"id\": <ID of the Deployment Delta.>,
       \"metadata\": {
         <Properties such as who created the Delta, which Environment it is associated to and a Human-friendly name>
       }
       \"modules\" : {
         \"add\" : {
           <ID of Module to add to the Deployment Set> : {
             <An entire Modules object>
           }
         },
         \"remove\": [
           <An array of Module IDs that should be removed from the Deployment Set>
         ],
        \"update\": {
           <ID of Module already in the Set to be updated> : [
             <An array of JSON Patch (Search Results (RFC 6902) objects scoped to the module>
           ]
         }
       }
     }
    ```
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Ignored, but can be provided."""
    metadata: Optional[shared_deltametadatarequest.DeltaMetadataRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    modules: Optional[shared_moduledeltasrequest.ModuleDeltasRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modules'), 'exclude': lambda f: f is None }})
    r"""ModuleDeltas groups the different operations together."""
    shared: Optional[list[shared_updateactionrequest.UpdateActionRequest]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shared'), 'exclude': lambda f: f is None }})
    