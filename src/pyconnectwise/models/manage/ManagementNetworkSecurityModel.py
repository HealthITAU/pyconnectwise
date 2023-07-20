from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ManagementNetworkSecurityModel(ConnectWiseModel):
    id: int
    name: str
    username: str
    password: str
    site: str
    _info: dict[str, str]