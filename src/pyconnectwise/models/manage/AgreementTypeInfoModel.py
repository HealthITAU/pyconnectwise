from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class ApplicationUnits(str, Enum):
    Amount = 'Amount'
    Hours = 'Hours'
    Incidents = 'Incidents'

class AgreementTypeInfoModel(ConnectWiseModel):
    id: int
    name: str
    inactive_flag: bool
    application_units: ApplicationUnits
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True