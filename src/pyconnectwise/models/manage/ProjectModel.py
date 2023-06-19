from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from enum import Enum
from pyconnectwise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.ProjectBoardReferenceModel import ProjectBoardReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.OpportunityReferenceModel import OpportunityReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.ProjectStatusReferenceModel import ProjectStatusReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.ProjectTypeReferenceModel import ProjectTypeReferenceModel
from pyconnectwise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class BillExpenses(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class BillingMethod(str, Enum):
    ActualRates = 'ActualRates'
    FixedFee = 'FixedFee'
    NotToExceed = 'NotToExceed'
    OverrideRate = 'OverrideRate'
class BillingRateType(str, Enum):
    StaffMember = 'StaffMember'
    WorkRole = 'WorkRole'
class BillProducts(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class BillTime(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class BudgetAnalysis(str, Enum):
    ActualHours = 'ActualHours'
    BillableHours = 'BillableHours'

class ProjectModel(ConnectWiseModel):
    id: int
    _info: dict[str, str]
    actual_end: str
    actual_hours: float
    actual_start: str
    agreement: AgreementReferenceModel
    bill_expenses: BillExpenses
    billing_amount: float
    billing_attention: str
    billing_method: BillingMethod
    billing_rate_type: BillingRateType
    billing_terms: BillingTermsReferenceModel
    bill_products: BillProducts
    bill_project_after_closed_flag: bool
    bill_time: BillTime
    bill_to_company: CompanyReferenceModel
    bill_to_contact: ContactReferenceModel
    bill_to_site: SiteReferenceModel
    bill_unapproved_time_and_expense: bool
    board: ProjectBoardReferenceModel
    budget_analysis: BudgetAnalysis
    budget_flag: bool
    budget_hours: float
    company: CompanyReferenceModel
    contact: ContactReferenceModel
    customer_p_o: str
    description: str
    currency: CurrencyReferenceModel
    downpayment: float
    estimated_end: str
    percent_complete: float
    estimated_expense_revenue: float
    estimated_hours: float
    estimated_product_revenue: float
    estimated_start: str
    estimated_time_revenue: float
    expense_approver: MemberReferenceModel
    include_dependencies_flag: bool
    include_estimates_flag: bool
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    manager: MemberReferenceModel
    name: str
    opportunity: OpportunityReferenceModel
    project_template_id: int
    restrict_down_payment_flag: bool
    scheduled_end: str
    scheduled_hours: float
    scheduled_start: str
    ship_to_company: CompanyReferenceModel
    ship_to_contact: ContactReferenceModel
    ship_to_site: SiteReferenceModel
    site: SiteReferenceModel
    status: ProjectStatusReferenceModel
    closed_flag: bool
    time_approver: MemberReferenceModel
    type: ProjectTypeReferenceModel
    do_not_display_in_portal_flag: bool
    billing_start_date: str
    estimated_time_cost: float
    estimated_expense_cost: float
    estimated_product_cost: float
    tax_code: TaxCodeReferenceModel
    company_location: SystemLocationReferenceModel
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True