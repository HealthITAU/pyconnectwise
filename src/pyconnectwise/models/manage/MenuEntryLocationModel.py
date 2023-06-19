from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemMenuEntryReferenceModel import SystemMenuEntryReferenceModel

class MenuEntryLocationModel(ConnectWiseModel):
    id: int
    location: SystemLocationReferenceModel
    menu_entry: SystemMenuEntryReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True