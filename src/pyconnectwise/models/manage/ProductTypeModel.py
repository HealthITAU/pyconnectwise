from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class TypeXref(str, Enum):
    InventoryPart = 'InventoryPart'
    NonInventoryPart = 'NonInventoryPart'
    OtherCharge = 'OtherCharge'
    Service = 'Service'

class ProductTypeModel(ConnectWiseModel):
    id: int
    name: str
    inactive_flag: bool
    type_xref: TypeXref
    default_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True