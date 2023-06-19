from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.PurchaseOrderReferenceModel import PurchaseOrderReferenceModel
from pyconnectwise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
class ProcurementType(str, Enum):
    Purchase = 'Purchase'
    Adjustment = 'Adjustment'
    Transfer = 'Transfer'

class UnpostedProcurementModel(ConnectWiseModel):
    id: int
    description: str
    unposted_product_id: str
    location_id: int
    department_id: int
    procurement_type: ProcurementType
    purchase_order: PurchaseOrderReferenceModel
    purchase_date: str
    tracking_number: str
    billing_terms: BillingTermsReferenceModel
    currency: CurrencyReferenceModel
    total: float
    tax_code: TaxCodeReferenceModel
    avalara_tax_flag: bool
    item_taxable_flag: bool
    purchase_order_taxable_flag: bool
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
    tax_total: float
    customer: CompanyReferenceModel
    vendor: CompanyReferenceModel
    vendor_account_number: str
    vendor_invoice_number: str
    vendor_invoice_date: str
    tax_freight_flag: bool
    freight_tax_total: float
    freight_cost: float
    date_closed: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True