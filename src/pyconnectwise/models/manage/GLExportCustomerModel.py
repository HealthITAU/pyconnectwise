from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.CompanyTypeReferenceModel import CompanyTypeReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pyconnectwise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.GLExportCustomerTaxLevelModel import GLExportCustomerTaxLevelModel

class GLExportCustomerModel(ConnectWiseModel):
    company: CompanyReferenceModel
    company_type: CompanyTypeReferenceModel
    contact: ContactReferenceModel
    site: SiteReferenceModel
    account_number: str
    billing_terms: BillingTermsReferenceModel
    billing_terms_xref: str
    due_days: int
    taxable: bool
    tax_code: TaxCodeReferenceModel
    currency: CurrencyReferenceModel
    state_tax_xref: str
    county_tax_xref: str
    city_tax_xref: str
    country_tax_xref: str
    composite_tax_xref: str
    state_tax_rate: float
    county_tax_rate: float
    city_tax_rate: float
    country_tax_rate: float
    composite_tax_rate: float
    tax_group_rate: float
    tax_agency_xref: str
    state_tax_agency_xref: str
    county_tax_agency_xref: str
    city_tax_agency_xref: str
    country_tax_agency_xref: str
    composite_tax_agency_xref: str
    tax_levels: list[GLExportCustomerTaxLevelModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True