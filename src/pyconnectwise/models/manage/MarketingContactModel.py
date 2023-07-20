from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class MarketingContactModel(ConnectWiseModel):
    id: int
    group_id: int
    note: str
    unsubscribe_flag: bool
    _info: dict[str, str]