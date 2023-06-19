from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MenuLocationReferenceModel import MenuLocationReferenceModel

class MenuEntryModel(ConnectWiseModel):
    id: int
    menu_location: MenuLocationReferenceModel
    caption: str
    link: str
    new_window_flag: bool
    location_ids: list[int]
    origin: str
    client_id: str
    add_all_locations: bool
    remove_all_locations: bool
    small_menu_icon_id: int
    large_menu_icon_id: int
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True