from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class CycleType(str, Enum):
    ContractYear = 'ContractYear'
    CalendarYear = 'CalendarYear'

class ProductRecurringModel(ConnectWiseModel):
    recurring_revenue: float
    recurring_cost: float
    start_date: str
    end_date: str
    bill_cycle_id: int
    cycles: int
    cycle_type: CycleType

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True