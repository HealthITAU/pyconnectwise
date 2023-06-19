from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from enum import Enum
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
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

class AgreementWorkTypeModel(ConnectWiseModel):
    id: int
    work_type: WorkTypeReferenceModel
    location_id: int
    rate_type: RateType
    bill_time: BillTime
    rate: float
    hours_max: float
    hours_min: float
    round_bill_hours: float
    overage_rate: float
    overage_rate_type: OverageRateType
    agreement_limit: float
    site: SiteReferenceModel
    effective_date: str
    ending_date: str
    agreement_id: int
    company: CompanyReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True