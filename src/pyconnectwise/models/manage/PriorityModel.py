from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class Color(str, Enum):
    Black = 'Black'
    Blue = 'Blue'
    Cyan = 'Cyan'
    Gray = 'Gray'
    Green = 'Green'
    Lime = 'Lime'
    Orange = 'Orange'
    Pink = 'Pink'
    Purple = 'Purple'
    Red = 'Red'
    White = 'White'
    Yellow = 'Yellow'
    Custom = 'Custom'

class PriorityModel(ConnectWiseModel):
    id: int
    name: str
    color: Color
    sort_order: int
    default_flag: bool
    image_link: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True