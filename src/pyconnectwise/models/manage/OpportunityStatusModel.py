from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class OpportunityStatusModel(ConnectWiseModel):
    id: int
    name: str
    won_flag: bool
    lost_flag: bool
    closed_flag: bool
    inactive_flag: bool
    default_flag: bool
    _info: dict[str, str]
    entered_by: str
    date_entered: str

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True