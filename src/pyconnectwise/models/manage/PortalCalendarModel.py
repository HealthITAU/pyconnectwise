from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class WeekStart(str, Enum):
    Sunday = 'Sunday'
    Monday = 'Monday'
    Tuesday = 'Tuesday'
    Wednesday = 'Wednesday'
    Thursday = 'Thursday'
    Friday = 'Friday'
    Saturday = 'Saturday'

class PortalCalendarModel(ConnectWiseModel):
    id: int
    week_start: WeekStart
    adjust1_start: str
    adjust1_end: str
    adjust1_hours: float
    adjust2_start: str
    adjust2_end: str
    adjust2_hours: float
    adjust3_start: str
    adjust3_end: str
    adjust3_hours: float
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True