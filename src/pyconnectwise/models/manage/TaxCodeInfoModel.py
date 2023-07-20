from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class TaxCodeInfoModel(ConnectWiseModel):
    id: int
    identifier: str
    description: str
    effective_date: str
    cancel_date: str
    _info: dict[str, str]