from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ScheduleColorModel(ConnectWiseModel):
    id: int
    start_percent: int
    end_percent: int
    color: str
    _info: dict[str, str]