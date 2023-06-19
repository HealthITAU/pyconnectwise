from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from enum import Enum
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pyconnectwise.models.manage.TicketReferenceModel import TicketReferenceModel
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

class TicketStopwatchModel(ConnectWiseModel):
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
    service_status: ServiceStatusReferenceModel
    start_time: str
    status: Status
    ticket: TicketReferenceModel
    ticket_mobile_guid: str
    total_pause_time: int
    work_role: WorkRoleReferenceModel
    work_type: WorkTypeReferenceModel
    show_notes_in_discussion_flag: bool
    show_notes_in_internal_flag: bool
    show_notes_in_resolution_flag: bool
    email_notes_to_contact_flag: bool
    email_notes_to_resources_flag: bool

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True