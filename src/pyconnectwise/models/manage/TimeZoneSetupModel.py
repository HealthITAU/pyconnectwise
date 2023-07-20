from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.TimeZoneReferenceModel import TimeZoneReferenceModel

class TimeZoneSetupModel(ConnectWiseModel):
    id: int
    name: str
    time_zone: TimeZoneReferenceModel
    offset: float
    default_flag: bool
    daylight_savings_flag: bool
    _info: dict[str, str]