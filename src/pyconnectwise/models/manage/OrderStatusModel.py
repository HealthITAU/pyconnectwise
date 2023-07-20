from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.OrderStatusEmailTemplateReferenceModel import OrderStatusEmailTemplateReferenceModel

class OrderStatusModel(ConnectWiseModel):
    id: int
    name: str
    default_flag: bool
    inactive_flag: bool
    sort_order: int
    closed_flag: bool
    email_template: OrderStatusEmailTemplateReferenceModel
    _info: dict[str, str]