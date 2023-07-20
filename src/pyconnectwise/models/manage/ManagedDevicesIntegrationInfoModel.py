from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ManagedDevicesIntegrationInfoModel(ConnectWiseModel):
    id: int
    name: str
    solution: str
    management_it_setup_type: str
    _info: dict[str, str]