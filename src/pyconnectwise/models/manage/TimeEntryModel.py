from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from enum import Enum
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from pyconnectwise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
from pyconnectwise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from pyconnectwise.models.manage.InvoiceReferenceModel import InvoiceReferenceModel
from pyconnectwise.models.manage.TimeSheetReferenceModel import TimeSheetReferenceModel
from pyconnectwise.models.manage.TicketReferenceModel import TicketReferenceModel
from pyconnectwise.models.manage.ProjectReferenceModel import ProjectReferenceModel
from pyconnectwise.models.manage.ProjectPhaseReferenceModel import ProjectPhaseReferenceModel
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class ChargeToType(str, Enum):
    ServiceTicket = 'ServiceTicket'
    ProjectTicket = 'ProjectTicket'
    ChargeCode = 'ChargeCode'
    Activity = 'Activity'
class BillableOption(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class Status(str, Enum):
    Open = 'Open'
    Rejected = 'Rejected'
    PendingApproval = 'PendingApproval'
    ErrorsCorrected = 'ErrorsCorrected'
    PendingProjectApproval = 'PendingProjectApproval'
    ApprovedByTierOne = 'ApprovedByTierOne'
    RejectBySecondTier = 'RejectBySecondTier'
    ApprovedByTierTwo = 'ApprovedByTierTwo'
    ReadyToBill = 'ReadyToBill'
    Billed = 'Billed'
    WrittenOff = 'WrittenOff'
    BilledAgreement = 'BilledAgreement'

class TimeEntryModel(ConnectWiseModel):
    id: int
    company: CompanyReferenceModel
    charge_to_id: int
    charge_to_type: ChargeToType
    member: MemberReferenceModel
    location_id: int
    business_unit_id: int
    work_type: WorkTypeReferenceModel
    work_role: WorkRoleReferenceModel
    agreement: AgreementReferenceModel
    time_start: str
    time_end: str
    hours_deduct: float
    actual_hours: float
    billable_option: BillableOption
    notes: str
    internal_notes: str
    add_to_detail_description_flag: bool
    add_to_internal_analysis_flag: bool
    add_to_resolution_flag: bool
    email_resource_flag: bool
    email_contact_flag: bool
    email_cc_flag: bool
    email_cc: str
    hours_billed: float
    invoice_hours: float
    entered_by: str
    date_entered: str
    invoice: InvoiceReferenceModel
    mobile_guid: str
    hourly_rate: float
    overage_rate: float
    agreement_hours: float
    agreement_amount: float
    time_sheet: TimeSheetReferenceModel
    status: Status
    ticket: TicketReferenceModel
    project: ProjectReferenceModel
    phase: ProjectPhaseReferenceModel
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True