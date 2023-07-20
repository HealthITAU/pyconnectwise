from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.TimeZoneSetupReferenceModel import TimeZoneSetupReferenceModel

class AutoSyncTimeModel(ConnectWiseModel):
    id: int
    sync_time: str
    time_zone: TimeZoneSetupReferenceModel
    _info: dict[str, str]