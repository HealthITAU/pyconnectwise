from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pyconnectwise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
from enum import Enum
class RateType(str, Enum):
    AdjAmount = 'AdjAmount'
    Custom = 'Custom'
    Multiplier = 'Multiplier'

class AgreementTypeWorkRoleModel(ConnectWiseModel):
    id: int
    type: AgreementTypeReferenceModel
    work_role: WorkRoleReferenceModel
    effective_date: str
    ending_date: str
    rate: float
    rate_type: RateType
    limit_to: float
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True