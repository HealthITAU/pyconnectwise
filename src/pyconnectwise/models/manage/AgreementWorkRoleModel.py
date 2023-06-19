from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
from enum import Enum
class RateType(str, Enum):
    AdjAmount = 'AdjAmount'
    Custom = 'Custom'
    Multiplier = 'Multiplier'

class AgreementWorkRoleModel(ConnectWiseModel):
    id: int
    work_role: WorkRoleReferenceModel
    location_id: int
    rate_type: RateType
    rate: float
    limit_to: float
    effective_date: str
    ending_date: str
    agreement_id: int
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True