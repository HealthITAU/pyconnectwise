from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.PurchaseOrderStatusEmailTemplateReferenceModel import PurchaseOrderStatusEmailTemplateReferenceModel

class PurchaseOrderStatusModel(ConnectWiseModel):
    id: int
    name: str
    default_flag: bool
    closed_flag: bool
    inactive_flag: bool
    default_closed_flag: bool
    sort_order: int
    email_template: PurchaseOrderStatusEmailTemplateReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True