from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class BillingOptions(str, Enum):
    BiMonthly = 'BiMonthly'
    BiWeekly = 'BiWeekly'
    Monthly = 'Monthly'
    NotRecurring = 'NotRecurring'
    Quarterly = 'Quarterly'
    SemiAnnual = 'SemiAnnual'
    Weekly = 'Weekly'
    Yearly = 'Yearly'

class BillingCycleModel(ConnectWiseModel):
    id: int
    identifier: str
    name: str
    default_flag: bool
    billing_options: BillingOptions
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True