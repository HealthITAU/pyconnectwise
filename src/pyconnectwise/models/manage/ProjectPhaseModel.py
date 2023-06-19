from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ProjectBoardReferenceModel import ProjectBoardReferenceModel
from pyconnectwise.models.manage.PhaseStatusReferenceModel import PhaseStatusReferenceModel
from pyconnectwise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from pyconnectwise.models.manage.OpportunityReferenceModel import OpportunityReferenceModel
from pyconnectwise.models.manage.ProjectPhaseReferenceModel import ProjectPhaseReferenceModel
from enum import Enum
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel
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
class BillingMethod(str, Enum):
    ActualRates = 'ActualRates'
    FixedFee = 'FixedFee'
    NotToExceed = 'NotToExceed'
    OverrideRate = 'OverrideRate'

class ProjectPhaseModel(ConnectWiseModel):
    id: int
    project_id: int
    description: str
    board: ProjectBoardReferenceModel
    status: PhaseStatusReferenceModel
    agreement: AgreementReferenceModel
    opportunity: OpportunityReferenceModel
    parent_phase: ProjectPhaseReferenceModel
    wbs_code: str
    bill_time: BillTime
    bill_expenses: BillExpenses
    bill_products: BillProducts
    mark_as_milestone_flag: bool
    notes: str
    deadline_date: str
    bill_separately_flag: bool
    billing_method: BillingMethod
    scheduled_hours: float
    scheduled_start: str
    scheduled_end: str
    actual_hours: float
    actual_start: str
    actual_end: str
    budget_hours: float
    location_id: int
    business_unit_id: int
    hourly_rate: float
    billing_start_date: str
    bill_phase_closed_flag: bool
    bill_project_closed_flag: bool
    downpayment: float
    po_number: str
    po_amount: float
    estimated_time_cost: float
    estimated_expense_cost: float
    estimated_product_cost: float
    estimated_time_revenue: float
    estimated_expense_revenue: float
    estimated_product_revenue: float
    currency: CurrencyReferenceModel
    bill_to_company: CompanyReferenceModel
    bill_to_contact: ContactReferenceModel
    bill_to_site: SiteReferenceModel
    ship_to_company: CompanyReferenceModel
    ship_to_contact: ContactReferenceModel
    ship_to_site: SiteReferenceModel
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True