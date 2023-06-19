from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.SLAReferenceModel import SLAReferenceModel
from pyconnectwise.models.manage.BillingCycleReferenceModel import BillingCycleReferenceModel
from pyconnectwise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pyconnectwise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
from pyconnectwise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from pyconnectwise.models.manage.ProjectTypeReferenceModel import ProjectTypeReferenceModel
from pyconnectwise.models.manage.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pyconnectwise.models.manage.EmailTemplateReferenceModel import EmailTemplateReferenceModel
class PrefixSuffixOption(str, Enum):
    Prefix = 'Prefix'
    Suffix = 'Suffix'
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

class AgreementTypeModel(ConnectWiseModel):
    id: int
    name: str
    prefix_suffix_option: PrefixSuffixOption
    default_flag: bool
    inactive_flag: bool
    pre_payment_flag: bool
    invoice_pre_suffix: str
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    restrict_location_flag: bool
    restrict_department_flag: bool
    sla: SLAReferenceModel
    application_units: ApplicationUnits
    application_limit: float
    application_cycle: ApplicationCycle
    application_unlimited_flag: bool
    one_time_flag: bool
    cover_agreement_time_flag: bool
    cover_agreement_product_flag: bool
    cover_agreement_expense_flag: bool
    cover_sales_tax_flag: bool
    carry_over_unused_flag: bool
    allow_overruns_flag: bool
    expired_days: int
    limit: int
    expire_when_zero: bool
    charge_to_firm_flag: bool
    employee_comp_rate: EmployeeCompRate
    employee_comp_not_exceed: EmployeeCompNotExceed
    comp_hourly_rate: float
    comp_limit_amount: float
    billing_cycle: BillingCycleReferenceModel
    bill_one_time_flag: bool
    billing_terms: BillingTermsReferenceModel
    invoicing_cycle: InvoicingCycle
    bill_amount: float
    taxable_flag: bool
    restrict_down_payment_flag: bool
    invoice_description: str
    top_comment_flag: bool
    bottom_comment_flag: bool
    work_role: WorkRoleReferenceModel
    work_type: WorkTypeReferenceModel
    project_type: ProjectTypeReferenceModel
    invoice_template: InvoiceTemplateReferenceModel
    bill_time: BillTime
    bill_expenses: BillExpenses
    bill_products: BillProducts
    billable_time_invoice_flag: bool
    billable_expense_invoice_flag: bool
    billable_product_invoice_flag: bool
    copy_work_roles_flag: bool
    copy_work_types_flag: bool
    exclusion_work_role_ids: list[int]
    add_all_work_role_exclusions: bool
    remove_all_work_role_exclusions: bool
    exclusion_work_type_ids: list[int]
    add_all_work_type_exclusions: bool
    remove_all_work_type_exclusions: bool
    integration_x_ref: str
    prorate_flag: bool
    email_template: EmailTemplateReferenceModel
    auto_invoice_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True