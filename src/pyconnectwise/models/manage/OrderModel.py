from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.OrderStatusReferenceModel import OrderStatusReferenceModel
from pyconnectwise.models.manage.OpportunityReferenceModel import OpportunityReferenceModel
from pyconnectwise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pyconnectwise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel

class OrderModel(ConnectWiseModel):
    id: int
    company: CompanyReferenceModel
    contact: ContactReferenceModel
    phone: str
    phone_ext: str
    email: str
    site: SiteReferenceModel
    status: OrderStatusReferenceModel
    opportunity: OpportunityReferenceModel
    order_date: str
    due_date: str
    billing_terms: BillingTermsReferenceModel
    tax_code: TaxCodeReferenceModel
    po_number: str
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    sales_rep: MemberReferenceModel
    notes: str
    bill_closed_flag: bool
    bill_shipped_flag: bool
    restrict_downpayment_flag: bool
    description: str
    top_comment_flag: bool
    bottom_comment_flag: bool
    ship_to_company: CompanyReferenceModel
    ship_to_contact: ContactReferenceModel
    ship_to_site: SiteReferenceModel
    bill_to_company: CompanyReferenceModel
    bill_to_contact: ContactReferenceModel
    bill_to_site: SiteReferenceModel
    product_ids: list[int]
    document_ids: list[int]
    invoice_ids: list[int]
    config_ids: list[int]
    total: float
    tax_total: float
    currency: CurrencyReferenceModel
    company_location: SystemLocationReferenceModel
    sub_total: float
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True