from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class WorkRoleModel(ConnectWiseModel):
    id: int
    name: str
    hourly_rate: float
    integration_xref: str
    inactive_flag: bool
    add_all_locations: bool
    remove_all_locations: bool
    add_all_agreement_exclusions: bool
    location_ids: list[int]
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True