from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.RmaStatusEmailTemplateReferenceModel import RmaStatusEmailTemplateReferenceModel

class RmaStatusModel(ConnectWiseModel):
    id: int
    name: str
    default_flag: bool
    sort_order: int
    closed_flag: bool
    email_template: RmaStatusEmailTemplateReferenceModel
    _info: dict[str, str]