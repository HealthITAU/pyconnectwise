from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class AccountingBatchModel(ConnectWiseModel):
    id: int
    batch_identifier: str
    export_invoices_flag: bool
    export_expenses_flag: bool
    export_products_flag: bool
    closed_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True