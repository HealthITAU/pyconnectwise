from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel

class GLPathModel(ConnectWiseModel):
    id: int
    location: SystemLocationReferenceModel
    path: str
    sql_server_name: str
    database_name: str
    last_payment_sync: str
    last_payment_sync_by: MemberReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True