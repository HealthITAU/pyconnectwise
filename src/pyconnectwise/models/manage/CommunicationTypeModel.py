from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class CommunicationTypeModel(ConnectWiseModel):
    id: int
    description: str
    phone_flag: bool
    fax_flag: bool
    email_flag: bool
    default_flag: bool
    exchange_xref: str
    iphone_xref: str
    android_xref: str
    google_xref: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True