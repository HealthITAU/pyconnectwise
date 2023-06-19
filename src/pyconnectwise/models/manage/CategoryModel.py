from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class CategoryModel(ConnectWiseModel):
    id: int
    name: str
    inactive_flag: bool
    price_level_xref: str
    integration_xref: str
    location_ids: list[int]
    default_flag: bool
    add_all_locations: bool
    remove_all_locations: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True