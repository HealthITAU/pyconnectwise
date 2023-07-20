from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class GenericBoardTeamReferenceModel(ConnectWiseModel):
    id: int
    name: str
    is_project_team_flag: bool
    _info: dict[str, str]