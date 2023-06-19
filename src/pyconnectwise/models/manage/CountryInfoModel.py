from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class CountryInfoModel(ConnectWiseModel):
    id: int
    name: str
    default_flag: bool
    city_caption: str
    state_caption: str
    zip_caption: str
    dialing_prefix: str
    localization_caption_one: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True