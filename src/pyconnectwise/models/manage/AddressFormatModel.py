from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class AddressFormatModel(ConnectWiseModel):
    id: int
    name: str
    format: str
    default_flag: bool
    country_ids: list[int]
    add_all_countries: bool
    remove_all_countries: bool
    _info: dict[str, str]