from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.CompanyTypeReferenceModel import CompanyTypeReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pyconnectwise.models.manage.PurchaseOrderReferenceModel import PurchaseOrderReferenceModel
from pyconnectwise.models.manage.ProjectReferenceModel import ProjectReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.CompanyTypeReferenceModel import CompanyTypeReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.GLExportTransactionDetailModel import GLExportTransactionDetailModel
from pyconnectwise.models.manage.GLExportTransactionTaxLevelModel import GLExportTransactionTaxLevelModel

class GLExportTransactionModel(ConnectWiseModel):
    id: int
    gl_class: str
    gl_type_id: str
    document_date: str
    document_number: str
    document_type: str
    memo: str
    description: str
    attention: str
    sales_territory: str
    company: CompanyReferenceModel
    company_type: CompanyTypeReferenceModel
    company_account_number: str
    site: SiteReferenceModel
    billing_terms: BillingTermsReferenceModel
    billing_terms_xref: str
    due_days: int
    due_date: str
    email_delivery_flag: bool
    print_delivery_flag: bool
    agreement_pre_payment_flag: bool
    account_number: str
    billing_type: str
    gl_entry_ids: str
    purchase_order: PurchaseOrderReferenceModel
    project: ProjectReferenceModel
    currency: CurrencyReferenceModel
    total: float
    sales_rep_id: str
    sales_rep_name: str
    taxable: bool
    taxable_total: float
    tax_code: TaxCodeReferenceModel
    tax_group_rate: float
    piggy_back_flag: bool
    tax_account_number: str
    sales_tax: float
    state_tax: float
    county_tax: float
    city_tax: float
    taxable_amount1: float
    taxable_amount2: float
    taxable_amount3: float
    taxable_amount4: float
    taxable_amount5: float
    tax_agency_xref: str
    state_tax_xref: str
    county_tax_xref: str
    tax_id: str
    tax_dp_applied_flag: bool
    use_avalara_flag: bool
    send_avalara_tax_flag: bool
    ship_to_company: CompanyReferenceModel
    ship_to_company_account_number: str
    ship_to_company_type: CompanyTypeReferenceModel
    ship_to_tax_id: str
    ship_site: SiteReferenceModel
    ship_contact: str
    detail: list[GLExportTransactionDetailModel]
    tax_levels: list[GLExportTransactionTaxLevelModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True