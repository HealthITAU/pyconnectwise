from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.CompanyTypeReferenceModel import CompanyTypeReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.CompanyTypeReferenceModel import CompanyTypeReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pyconnectwise.models.manage.GLExportPurchaseTransactionTaxLevelModel import GLExportPurchaseTransactionTaxLevelModel
from pyconnectwise.models.manage.GLExportPurchaseTransactionDetailModel import GLExportPurchaseTransactionDetailModel
from pyconnectwise.models.manage.GLExportPurchaseTransactionDetailTaxModel import GLExportPurchaseTransactionDetailTaxModel

class GLExportPurchaseTransactionModel(ConnectWiseModel):
    id: str
    document_date: str
    document_number: str
    description: str
    memo: str
    ap_account_number: str
    purchase_date: str
    company: CompanyReferenceModel
    company_type: CompanyTypeReferenceModel
    contact: ContactReferenceModel
    site: SiteReferenceModel
    purchase_class: str
    freight_amount: float
    freight_packing_slip: str
    packing_slip: str
    dropship_flag: bool
    currency: CurrencyReferenceModel
    total: float
    billing_terms: BillingTermsReferenceModel
    billing_terms_xref: str
    due_days: int
    vendor_number: str
    vendor_account_number: str
    vendor_invoice_date: str
    vendor_invoice_number: str
    tax_agency_xref: str
    state_tax_xref: str
    county_tax_xref: str
    city_tax_xref: str
    ship_to_company: CompanyReferenceModel
    ship_to_company_account_number: str
    ship_to_company_type: CompanyTypeReferenceModel
    ship_to_contact: ContactReferenceModel
    ship_to_site: SiteReferenceModel
    ship_to_tax_group: str
    tax_code: TaxCodeReferenceModel
    tax_group_rate: float
    use_avalara_tax_flag: bool
    purchase_header_tax_group: str
    purchase_header_taxable_flag: bool
    purchase_header_freight_taxable_flag: bool
    tax_levels: list[GLExportPurchaseTransactionTaxLevelModel]
    purchase_detail: list[GLExportPurchaseTransactionDetailModel]
    purchase_detail_tax: list[GLExportPurchaseTransactionDetailTaxModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True