from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class RateType(str, Enum):
    Amount = 'Amount'
    Percent = 'Percent'

class TaxCodeLevelModel(ConnectWiseModel):
    id: int
    tax_level: int
    tax_rate: float
    rate_type: RateType
    taxable_max: float
    caption: str
    tax_code_xref: str
    agency_xref: str
    tax_services_flag: bool
    tax_expenses_flag: bool
    tax_products_flag: bool
    single_unit_flag: bool
    single_unit_minimum: float
    single_unit_maximum: float
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True