from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ExpenseTypeReferenceModel import ExpenseTypeReferenceModel
from enum import Enum
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.ChargeCodeReferenceModel import ChargeCodeReferenceModel
from pyconnectwise.models.manage.PaymentMethodReferenceModel import PaymentMethodReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from pyconnectwise.models.manage.TicketReferenceModel import TicketReferenceModel
from pyconnectwise.models.manage.ProjectReferenceModel import ProjectReferenceModel
from pyconnectwise.models.manage.ProjectPhaseReferenceModel import ProjectPhaseReferenceModel
from pyconnectwise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
class Classification(str, Enum):
    NonReimbursable = 'NonReimbursable'
    Reimbursable = 'Reimbursable'
    Personal = 'Personal'
class GlType(str, Enum):
    AP = 'AP'
    AR = 'AR'
    EE = 'EE'
    EI = 'EI'
    EO = 'EO'
    IA = 'IA'
    IT = 'IT'
    P = 'P'
    PF = 'PF'
    R = 'R'
    RA = 'RA'
    RD = 'RD'
    RE = 'RE'
    RP = 'RP'
    ST = 'ST'
    SD = 'SD'
    ET = 'ET'
    FT = 'FT'
    PT = 'PT'

class UnpostedExpenseModel(ConnectWiseModel):
    id: int
    location_id: int
    department_id: int
    company: CompanyReferenceModel
    account_number: str
    credit_account: str
    expense_detail_id: int
    expense_type: ExpenseTypeReferenceModel
    classification: Classification
    gl_type: GlType
    member: MemberReferenceModel
    date_expense: str
    charge_code: ChargeCodeReferenceModel
    charge_description: str
    in_policy: bool
    payment_method: PaymentMethodReferenceModel
    currency: CurrencyReferenceModel
    total: float
    billable_amount: float
    non_billable_amount: float
    agreement: AgreementReferenceModel
    agreement_amount_covered: float
    ticket: TicketReferenceModel
    project: ProjectReferenceModel
    project_phase: ProjectPhaseReferenceModel
    tax_code: TaxCodeReferenceModel
    avalara_tax_flag: bool
    item_taxable_flag: bool
    sales_tax_amount: float
    state_tax_flag: bool
    state_tax_xref: str
    state_tax_amount: float
    county_tax_flag: bool
    county_tax_xref: str
    county_tax_amount: float
    city_tax_flag: bool
    city_tax_xref: str
    city_tax_amount: float
    country_tax_flag: bool
    country_tax_xref: str
    country_tax_amount: float
    composite_tax_flag: bool
    composite_tax_xref: str
    composite_tax_amount: float
    level_six_tax_flag: bool
    level_six_tax_xref: str
    level_six_tax_amount: float
    date_closed: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True