from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from enum import Enum
class VacationAvailableType(str, Enum):
    AnniversaryYear = 'AnniversaryYear'
    CalendarYear = 'CalendarYear'
class SickAvailableType(str, Enum):
    AnniversaryYear = 'AnniversaryYear'
    CalendarYear = 'CalendarYear'
class PtoAvailableType(str, Enum):
    AnniversaryYear = 'AnniversaryYear'
    CalendarYear = 'CalendarYear'
class HolidayAvailableType(str, Enum):
    AnniversaryYear = 'AnniversaryYear'
    CalendarYear = 'CalendarYear'

class TimeAccrualModel(ConnectWiseModel):
    id: int
    location: SystemLocationReferenceModel
    vacation_flag: bool
    vacation_available_type: VacationAvailableType
    vacation_carryover_allowed_flag: bool
    vacation_carryover_limit: float
    sick_flag: bool
    sick_available_type: SickAvailableType
    sick_carryover_allowed_flag: bool
    sick_carryover_limit: float
    pto_flag: bool
    pto_available_type: PtoAvailableType
    pto_carryover_allowed_flag: bool
    pto_carryover_limit: float
    holiday_flag: bool
    holiday_available_type: HolidayAvailableType
    holiday_carryover_allowed_flag: bool
    holiday_carryover_limit: float
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True