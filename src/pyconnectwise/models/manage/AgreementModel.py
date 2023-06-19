from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.OpportunityReferenceModel import OpportunityReferenceModel
from pyconnectwise.models.manage.SLAReferenceModel import SLAReferenceModel
from enum import Enum
from pyconnectwise.models.manage.BillingCycleReferenceModel import BillingCycleReferenceModel
from pyconnectwise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pyconnectwise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
from pyconnectwise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from pyconnectwise.models.manage.ProjectTypeReferenceModel import ProjectTypeReferenceModel
from pyconnectwise.models.manage.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class ApplicationUnits(str, Enum):
    Amount = 'Amount'
    Hours = 'Hours'
    Incidents = 'Incidents'
class ApplicationCycle(str, Enum):
    Contract2Weeks = 'Contract2Weeks'
    Contract4Weeks = 'Contract4Weeks'
    ContractYear = 'ContractYear'
    CalendarMonth = 'CalendarMonth'
    CalendarQuarter = 'CalendarQuarter'
    CalendarWeek = 'CalendarWeek'
    ContractQuarter = 'ContractQuarter'
    CalendarYear = 'CalendarYear'
class EmployeeCompRate(str, Enum):
    Actual = 'Actual'
    Hourly = 'Hourly'
class EmployeeCompNotExceed(str, Enum):
    Billing = 'Billing'
    Amount = 'Amount'
    Percent = 'Percent'
class InvoicingCycle(str, Enum):
    ContractYear = 'ContractYear'
    CalendarYear = 'CalendarYear'
class BillTime(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class BillExpenses(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class BillProducts(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class PeriodType(str, Enum):
    Current = 'Current'
    Future = 'Future'
    Both = 'Both'
    Undefined = 'Undefined'
class AgreementStatus(str, Enum):
    Active = 'Active'
    Cancelled = 'Cancelled'
    Expired = 'Expired'
    Inactive = 'Inactive'

class AgreementModel(ConnectWiseModel):
    id: int
    name: str
    type: AgreementTypeReferenceModel
    company: CompanyReferenceModel
    contact: ContactReferenceModel
    site: SiteReferenceModel
    sub_contract_company: CompanyReferenceModel
    sub_contract_contact: ContactReferenceModel
    parent_agreement: AgreementReferenceModel
    customer_p_o: str
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    restrict_location_flag: bool
    restrict_department_flag: bool
    start_date: str
    end_date: str
    no_ending_date_flag: bool
    opportunity: OpportunityReferenceModel
    cancelled_flag: bool
    date_cancelled: str
    reason_cancelled: str
    sla: SLAReferenceModel
    work_order: str
    internal_notes: str
    application_units: ApplicationUnits
    application_limit: float
    application_cycle: ApplicationCycle
    application_unlimited_flag: bool
    one_time_flag: bool
    cover_agreement_time: bool
    cover_agreement_product: bool
    cover_agreement_expense: bool
    cover_sales_tax: bool
    carry_over_unused: bool
    allow_overruns: bool
    expired_days: int
    limit: int
    expire_when_zero: bool
    charge_to_firm: bool
    employee_comp_rate: EmployeeCompRate
    employee_comp_not_exceed: EmployeeCompNotExceed
    comp_hourly_rate: float
    comp_limit_amount: float
    billing_cycle: BillingCycleReferenceModel
    bill_one_time_flag: bool
    billing_terms: BillingTermsReferenceModel
    invoicing_cycle: InvoicingCycle
    bill_to_company: CompanyReferenceModel
    bill_to_contact: ContactReferenceModel
    bill_to_site: SiteReferenceModel
    bill_amount: float
    taxable: bool
    prorate_first_bill: float
    bill_start_date: str
    tax_code: TaxCodeReferenceModel
    restrict_down_payment: bool
    prorate_flag: bool
    invoice_description: str
    top_comment: bool
    bottom_comment: bool
    work_role: WorkRoleReferenceModel
    work_type: WorkTypeReferenceModel
    project_type: ProjectTypeReferenceModel
    invoice_template: InvoiceTemplateReferenceModel
    bill_time: BillTime
    bill_expenses: BillExpenses
    bill_products: BillProducts
    billable_time_invoice: bool
    billable_expense_invoice: bool
    billable_product_invoice: bool
    currency: CurrencyReferenceModel
    period_type: PeriodType
    auto_invoice_flag: bool
    next_invoice_date: str
    company_location: SystemLocationReferenceModel
    agreement_status: AgreementStatus
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True