from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ExpenseTypeInfoModel(ConnectWiseModel):
    id: int
    name: str
    inactive_flag: bool
    amount_caption: str
    mileage_flag: bool
    _info: dict[str, str]