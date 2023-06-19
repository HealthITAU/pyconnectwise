from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class BillTime(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
class RateType(str, Enum):
    AdjAmount = 'AdjAmount'
    Custom = 'Custom'
    Multiplier = 'Multiplier'
class AccrualType(str, Enum):
    Holiday = 'Holiday'
    PTO = 'PTO'
    Sick = 'Sick'
    Vacation = 'Vacation'

class WorkTypeModel(ConnectWiseModel):
    id: int
    name: str
    bill_time: BillTime
    rate_type: RateType
    rate: float
    hours_min: float
    hours_max: float
    round_bill_hours_to: float
    accrual_type: AccrualType
    inactive_flag: bool
    overall_default_flag: bool
    activity_default_flag: bool
    utilization_flag: bool
    cost_multiplier: float
    integration_x_ref: str
    add_all_agreement_exclusions: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True