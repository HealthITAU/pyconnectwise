from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class UnpostedExpenseTaxableLevelModel(ConnectWiseModel):
    id: int
    tax_level: int
    tax_code_xref: str
    tax_amount: float
    _info: dict[str, str]