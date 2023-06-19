from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.BoardReferenceModel import BoardReferenceModel
from pyconnectwise.models.manage.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pyconnectwise.models.manage.ServiceItemReferenceModel import ServiceItemReferenceModel
from pyconnectwise.models.manage.ServiceSubTypeReferenceModel import ServiceSubTypeReferenceModel
from pyconnectwise.models.manage.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pyconnectwise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pyconnectwise.models.manage.ServiceSourceReferenceModel import ServiceSourceReferenceModel
from pyconnectwise.models.manage.PriorityReferenceModel import PriorityReferenceModel
from pyconnectwise.models.manage.ServiceTeamReferenceModel import ServiceTeamReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from enum import Enum
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
class BillingMethod(str, Enum):
    ActualRates = 'ActualRates'
    FixedFee = 'FixedFee'
    NotToExceed = 'NotToExceed'
    OverrideRate = 'OverrideRate'
class Severity(str, Enum):
    Low = 'Low'
    Medium = 'Medium'
    High = 'High'
class Impact(str, Enum):
    Low = 'Low'
    Medium = 'Medium'
    High = 'High'

class ServiceTemplateModel(ConnectWiseModel):
    id: int
    name: str
    board: BoardReferenceModel
    type: ServiceTypeReferenceModel
    item: ServiceItemReferenceModel
    subtype: ServiceSubTypeReferenceModel
    service_location: ServiceLocationReferenceModel
    status: ServiceStatusReferenceModel
    source: ServiceSourceReferenceModel
    priority: PriorityReferenceModel
    team: ServiceTeamReferenceModel
    company: CompanyReferenceModel
    contact: ContactReferenceModel
    site: SiteReferenceModel
    assigned_notify_flag: bool
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    summary: str
    problem: str
    hours_budget: float
    internal_analysis: str
    time_billable_flag: bool
    expense_billable_flag: bool
    purchase_order_number: str
    reference: str
    bill_complete__flag: bool
    bill_service_separately_flag: bool
    billing_amount: float
    bill_unapproved_time_and_expenses_flag: bool
    override_flag: bool
    time_invoice_flag: bool
    expense_invoice_flag: bool
    product_invoice_flag: bool
    agreement: AgreementReferenceModel
    billing_method: BillingMethod
    severity: Severity
    impact: Impact
    assigned_by: MemberReferenceModel
    schedule_days_before: int
    service_days_before: int
    attach_schedule_to_new_service_flag: bool
    template_flag: bool
    email_contact_flag: bool
    email_resource_flag: bool
    email_c_c_flag: bool
    email_c_c: str
    restrict_downpayment_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True