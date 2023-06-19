from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class CallbackEntryModel(ConnectWiseModel):
    id: int
    description: str
    url: str
    object_id: int
    type: str
    level: str
    member_id: int
    payload_version: str
    inactive_flag: bool
    is_soap_callback_flag: bool
    is_self_suppressed_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True