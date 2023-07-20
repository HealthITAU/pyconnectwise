from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class TrackModel(ConnectWiseModel):
    id: int
    name: str
    inactive_flag: bool
    notify_action_ids: list[int]
    _info: dict[str, str]