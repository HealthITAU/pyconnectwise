from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class UserDefinedFieldOptionModel(ConnectWiseModel):
    id: int
    option_value: str
    default_flag: bool
    inactive_flag: bool
    sort_order: int

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True