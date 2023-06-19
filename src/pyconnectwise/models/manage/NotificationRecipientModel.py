from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class NotificationRecipientModel(ConnectWiseModel):
    id: int
    identifier: str
    name: str
    external_flag: bool
    service_flag: bool
    sales_flag: bool
    invoice_flag: bool
    agreement_flag: bool
    member_flag: bool
    config_flag: bool
    msp_flag: bool
    track_flag: bool
    project_flag: bool
    procurement_flag: bool
    knowledge_base_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True