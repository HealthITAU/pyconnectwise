from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pyconnectwise.models.manage.ReminderReferenceModel import ReminderReferenceModel
from pyconnectwise.models.manage.ScheduleStatusReferenceModel import ScheduleStatusReferenceModel
from pyconnectwise.models.manage.ScheduleTypeReferenceModel import ScheduleTypeReferenceModel
from pyconnectwise.models.manage.ScheduleSpanReferenceModel import ScheduleSpanReferenceModel

class ScheduleEntryModel(ConnectWiseModel):
    id: int
    object_id: int
    name: str
    member: MemberReferenceModel
    where: ServiceLocationReferenceModel
    date_start: str
    date_end: str
    reminder: ReminderReferenceModel
    status: ScheduleStatusReferenceModel
    type: ScheduleTypeReferenceModel
    span: ScheduleSpanReferenceModel
    done_flag: bool
    acknowledged_flag: bool
    owner_flag: bool
    meeting_flag: bool
    allow_schedule_conflicts_flag: bool
    add_member_to_project_flag: bool
    project_role_id: int
    mobile_guid: str
    acknowledged_date: str
    close_date: str
    hours: float
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True