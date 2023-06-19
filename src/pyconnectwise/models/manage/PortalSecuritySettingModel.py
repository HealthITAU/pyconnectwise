from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class PortalSecuritySettingModel(ConnectWiseModel):
    id: int
    function_identifier: str
    function_description: str
    level_one: bool
    level_two: bool
    level_three: bool
    level_four: bool
    level_five: bool
    level_six: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True