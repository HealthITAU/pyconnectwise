from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from enum import Enum
class ClearPickerRequestModelType(str, Enum):
    Company = 'Company'
    Vendor = 'Vendor'

class ClearPickerRequestModel(ConnectWiseModel):
    member: MemberReferenceModel
    type: ClearPickerRequestModelType

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True