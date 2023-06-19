from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.DocumentReferenceModel import DocumentReferenceModel
from enum import Enum
class LicenseClass(str, Enum):
    A = 'A'
    C = 'C'
    F = 'F'
    X = 'X'

class MemberInfoModel(ConnectWiseModel):
    id: int
    identifier: str
    first_name: str
    middle_initial: str
    last_name: str
    full_name: str
    default_email: str
    photo: DocumentReferenceModel
    license_class: LicenseClass
    inactive_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True