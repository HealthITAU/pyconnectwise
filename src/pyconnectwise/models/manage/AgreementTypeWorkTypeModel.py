from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pyconnectwise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from enum import Enum
class RateType(str, Enum):
    AdjAmount = 'AdjAmount'
    Custom = 'Custom'
    Multiplier = 'Multiplier'
class BillTime(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class OverageRateType(str, Enum):
    AdjAmount = 'AdjAmount'
    Custom = 'Custom'
    Multiplier = 'Multiplier'

class AgreementTypeWorkTypeModel(ConnectWiseModel):
    id: int
    type: AgreementTypeReferenceModel
    work_type: WorkTypeReferenceModel
    effective_date: str
    ending_date: str
    rate: float
    rate_type: RateType
    bill_time: BillTime
    hours_min: float
    hours_max: float
    round_bill_hours: float
    overage_rate: float
    overage_rate_type: OverageRateType
    limit_to: float
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True