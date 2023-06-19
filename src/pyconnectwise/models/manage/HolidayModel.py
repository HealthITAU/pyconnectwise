from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.HolidayListReferenceModel import HolidayListReferenceModel

class HolidayModel(ConnectWiseModel):
    id: int
    name: str
    all_day_flag: bool
    date: str
    time_start: str
    time_end: str
    holiday_list: HolidayListReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True