from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ContactTypeInfoModel(ConnectWiseModel):
    id: int
    description: str
    default_flag: bool
    service_alert_flag: bool
    service_alert_message: str
    _info: dict[str, str]