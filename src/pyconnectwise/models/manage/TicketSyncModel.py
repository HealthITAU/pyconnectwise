from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.IntegratorLoginReferenceModel import IntegratorLoginReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
class VendorType(str, Enum):
    Zenith = 'Zenith'

class TicketSyncModel(ConnectWiseModel):
    id: int
    name: str
    vendor_type: VendorType
    integrator_login: IntegratorLoginReferenceModel
    company: CompanyReferenceModel
    url: str
    user_name: str
    password: str
    psg: str
    problem_description_flag: bool
    internal_analysis_flag: bool
    resolution_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True