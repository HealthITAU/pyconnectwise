from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.HolidayListReferenceModel import HolidayListReferenceModel

class CalendarModel(ConnectWiseModel):
    id: int
    name: str
    holiday_list: HolidayListReferenceModel
    monday_start_time: str
    monday_end_time: str
    tuesday_start_time: str
    tuesday_end_time: str
    wednesday_start_time: str
    wednesday_end_time: str
    thursday_start_time: str
    thursday_end_time: str
    friday_start_time: str
    friday_end_time: str
    saturday_start_time: str
    saturday_end_time: str
    sunday_start_time: str
    sunday_end_time: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True