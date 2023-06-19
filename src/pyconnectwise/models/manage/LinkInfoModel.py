from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class ScreenLink(str, Enum):
    Company = 'Company'
    Contact = 'Contact'
    Service = 'Service'
    Invoice = 'Invoice'
    PurchaseOrder = 'PurchaseOrder'
    SalesOrder = 'SalesOrder'

class LinkInfoModel(ConnectWiseModel):
    id: int
    name: str
    screen_link: ScreenLink
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True