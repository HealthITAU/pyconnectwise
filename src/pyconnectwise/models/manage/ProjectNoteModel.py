from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.NoteTypeReferenceModel import NoteTypeReferenceModel

class ProjectNoteModel(ConnectWiseModel):
    id: int
    project_id: int
    text: str
    type: NoteTypeReferenceModel
    flagged: bool
    _info: dict[str, str]