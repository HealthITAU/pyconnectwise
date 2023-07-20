from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ActivityTypeModel(ConnectWiseModel):
    id: int
    name: str
    points: int
    default_flag: bool
    inactive_flag: bool
    email_flag: bool
    memo_flag: bool
    history_flag: bool
    _info: dict[str, str]