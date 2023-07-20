from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class BoardExcludedMemberModel(ConnectWiseModel):
    id: int
    member_id: int
    board_id: int
    _info: dict[str, str]