from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ServiceTicketLinkModel(ConnectWiseModel):
    id: int
    name: str
    enabled_flag: bool
    link_text: str
    url: str
    _info: dict[str, str]