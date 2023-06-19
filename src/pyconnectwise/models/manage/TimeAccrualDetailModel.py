from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.TimeAccrualReferenceModel import TimeAccrualReferenceModel
class AccrualType(str, Enum):
    Holiday = 'Holiday'
    PTO = 'PTO'
    Sick = 'Sick'
    Vacation = 'Vacation'

class TimeAccrualDetailModel(ConnectWiseModel):
    id: int
    accrual_type: AccrualType
    start_year: int
    end_year: int
    hours: float
    time_accrual: TimeAccrualReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True