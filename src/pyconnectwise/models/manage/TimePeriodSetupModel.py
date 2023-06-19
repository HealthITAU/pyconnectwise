from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class PeriodApplyTo(str, Enum):
    Both = 'Both'
    Expense = 'Expense'
    Time = 'Time'
class TimePeriodSetupModelType(str, Enum):
    Weekly = 'Weekly'
    BiWeekly = 'BiWeekly'
    SemiMonthly = 'SemiMonthly'
    Monthly = 'Monthly'

class TimePeriodSetupModel(ConnectWiseModel):
    id: int
    period_apply_to: PeriodApplyTo
    year: int
    number_future_periods: int
    type: TimePeriodSetupModelType
    description: str
    first_period_end_date: str
    monthly_period_ends: int
    semi_monthly_first_period: int
    semi_monthly_second_period: int
    semi_monthly_last_day_flag: bool
    last_day_flag: bool
    days_past_end_date: int
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True