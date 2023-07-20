from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class OpportunityStatusInfoModel(ConnectWiseModel):
    id: int
    closed_flag: bool
    inactive_flag: bool
    name: str
    _info: dict[str, str]