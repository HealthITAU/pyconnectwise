from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.NoteTypeReferenceModel import NoteTypeReferenceModel

class OpportunityNoteModel(ConnectWiseModel):
    id: int
    opportunity_id: int
    type: NoteTypeReferenceModel
    text: str
    flagged: bool
    entered_by: str
    mobile_guid: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True