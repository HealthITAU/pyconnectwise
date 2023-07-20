from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ExpenseRevenueReferenceModel(ConnectWiseModel):
    id: int
    revenue: float
    cost: float
    margin: float
    percentage: float
    _info: dict[str, str]