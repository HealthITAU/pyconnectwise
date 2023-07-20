from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class BoardStatusInfoModel(ConnectWiseModel):
    id: int
    name: str
    sort_order: int
    default_flag: bool
    inactive_flag: bool
    closed_flag: bool
    _info: dict[str, str]