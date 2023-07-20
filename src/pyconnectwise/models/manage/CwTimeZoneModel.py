from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class CwTimeZoneModel(ConnectWiseModel):
    id: int
    name: str
    offset: float
    start_date: str
    end_date: str
    daylight_savings_flag: bool
    _info: dict[str, str]