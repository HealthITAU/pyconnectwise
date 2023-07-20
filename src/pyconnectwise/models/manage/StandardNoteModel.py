from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.BoardReferenceModel import BoardReferenceModel

class StandardNoteModel(ConnectWiseModel):
    id: int
    name: str
    contents: str
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    board: BoardReferenceModel
    _info: dict[str, str]