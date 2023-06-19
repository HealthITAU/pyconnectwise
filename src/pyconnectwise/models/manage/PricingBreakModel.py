from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class PriceMethod(str, Enum):
    FlatRateForRange = 'FlatRateForRange'
    PercentMarkupFromCost = 'PercentMarkupFromCost'
    PercentMarkdownFromPrice = 'PercentMarkdownFromPrice'
    PricePerUnit = 'PricePerUnit'

class PricingBreakModel(ConnectWiseModel):
    id: int
    detail_id: int
    amount: float
    quantity_start: float
    quantity_end: float
    unlimited: bool
    price_method: PriceMethod
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True