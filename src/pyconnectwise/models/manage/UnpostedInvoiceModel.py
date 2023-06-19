from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from enum import Enum
from pyconnectwise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
class InvoiceType(str, Enum):
    Agreement = 'Agreement'
    CreditMemo = 'CreditMemo'
    DownPayment = 'DownPayment'
    Miscellaneous = 'Miscellaneous'
    Progress = 'Progress'
    Standard = 'Standard'

class UnpostedInvoiceModel(ConnectWiseModel):
    id: int
    billing_log_id: int
    location_id: int
    department_id: int
    company: CompanyReferenceModel
    account_number: str
    bill_to_company: CompanyReferenceModel
    bill_to_site: SiteReferenceModel
    ship_to_company: CompanyReferenceModel
    ship_to_site: SiteReferenceModel
    invoice_number: str
    invoice_date: str
    invoice_type: InvoiceType
    description: str
    billing_terms: BillingTermsReferenceModel
    due_days: str
    due_date: str
    currency: CurrencyReferenceModel
    sub_total: float
    total: float
    invoice_taxable_flag: bool
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
    created_by: str
    date_closed: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True