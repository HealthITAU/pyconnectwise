from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class SetupScreenModel(ConnectWiseModel):
    id: int
    category: str
    name: str
    description: str
    module_description: str
    module_identifier: str
    module_name: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True