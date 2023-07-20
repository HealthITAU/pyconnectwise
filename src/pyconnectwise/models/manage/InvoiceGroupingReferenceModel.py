from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class InvoiceGroupingReferenceModel(ConnectWiseModel):
    id: int
    name: str
    description: str
    show_price_flag: bool
    show_sub_items_flag: bool
    _info: dict[str, str]