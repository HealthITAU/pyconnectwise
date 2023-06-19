from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from enum import Enum
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
from pyconnectwise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
class BillableOption(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class Status(str, Enum):
    Reset = 'Reset'
    Running = 'Running'
    Paused = 'Paused'
    Stopped = 'Stopped'

class ScheduleStopwatchModel(ConnectWiseModel):
    _info: dict[str, str]
    agreement: AgreementReferenceModel
    billable_option: BillableOption
    business_unit_id: int
    date_entered: str
    end_time: str
    id: int
    internal_notes: str
    location_id: int
    member: MemberReferenceModel
    mobile_guid: str
    notes: str
    schedule_id: int
    schedule_mobile_guid: str
    start_time: str
    status: Status
    total_pause_time: int
    work_role: WorkRoleReferenceModel
    work_type: WorkTypeReferenceModel

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True