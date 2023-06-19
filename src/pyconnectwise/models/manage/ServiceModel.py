from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.CalendarSetupReferenceModel import CalendarSetupReferenceModel
class SrNotify(str, Enum):
    All = 'All'
    NewAndClosedRequests = 'NewAndClosedRequests'
    ClosedRequestsOnly = 'ClosedRequestsOnly'
    NewRequestsOnly = 'NewRequestsOnly'
    NONE = 'NONE'
class ScheduleSpan(str, Enum):
    Standard = 'Standard'
    OfficeHours = 'OfficeHours'
    Overnight = 'Overnight'

class ServiceModel(ConnectWiseModel):
    id: int
    sr_notify: SrNotify
    schedule_span: ScheduleSpan
    hide_delimiter_flag: bool
    allow_c_c_flag: bool
    allow_t_o_flag: bool
    header_color: str
    member_color: str
    contact_color: str
    unknown_color: str
    calendar_setup: CalendarSetupReferenceModel
    header_color_disable_flag: bool
    member_color_disable_flag: bool
    contact_color_disable_flag: bool
    unknown_color_disable_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True