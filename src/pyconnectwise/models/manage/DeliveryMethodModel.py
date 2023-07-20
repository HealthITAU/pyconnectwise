from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class DeliveryMethodModel(ConnectWiseModel):
    id: int
    name: str
    default_flag: bool
    email_flag: bool
    integration_email_flag: bool
    integration_print_flag: bool
    integration_active_flag: bool
    _info: dict[str, str]