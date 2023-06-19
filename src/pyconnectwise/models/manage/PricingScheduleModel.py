from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel

class PricingScheduleModel(ConnectWiseModel):
    id: int
    name: str
    inactive_flag: bool
    default_flag: bool
    currency: CurrencyReferenceModel
    companies: list[int]
    set_all_companies_flag: bool
    remove_all_companies_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True