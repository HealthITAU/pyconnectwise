from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class CurrencyReferenceModel(ConnectWiseModel):
    id: int
    symbol: str
    currency_code: str
    decimal_separator: str
    number_of_decimals: int
    thousands_separator: str
    negative_parentheses_flag: bool
    display_symbol_flag: bool
    currency_identifier: str
    display_id_flag: bool
    right_align: bool
    name: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True