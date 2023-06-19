from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.BillingStatusReferenceModel import BillingStatusReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.BillingTermsReferenceModel import BillingTermsReferenceModel
from pyconnectwise.models.manage.InvoiceTemplateDetailReferenceModel import InvoiceTemplateDetailReferenceModel
from pyconnectwise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.BillingSetupReferenceModel import BillingSetupReferenceModel
from pyconnectwise.models.manage.TicketReferenceModel import TicketReferenceModel
from pyconnectwise.models.manage.ProjectReferenceModel import ProjectReferenceModel
from pyconnectwise.models.manage.ProjectPhaseReferenceModel import ProjectPhaseReferenceModel
from pyconnectwise.models.manage.SalesOrderReferenceModel import SalesOrderReferenceModel
from pyconnectwise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class InvoiceModelType(str, Enum):
    Agreement = 'Agreement'
    CreditMemo = 'CreditMemo'
    DownPayment = 'DownPayment'
    Miscellaneous = 'Miscellaneous'
    Progress = 'Progress'
    Standard = 'Standard'
class ApplyToType(str, Enum):
    All = 'All'
    Agreement = 'Agreement'
    Project = 'Project'
    ProjectPhase = 'ProjectPhase'
    SalesOrder = 'SalesOrder'
    Ticket = 'Ticket'

class InvoiceModel(ConnectWiseModel):
    id: int
    invoice_number: str
    type: InvoiceModelType
    status: BillingStatusReferenceModel
    company: CompanyReferenceModel
    bill_to_company: CompanyReferenceModel
    ship_to_company: CompanyReferenceModel
    account_number: str
    apply_to_type: ApplyToType
    apply_to_id: int
    attention: str
    ship_to_attention: str
    billing_site: SiteReferenceModel
    billing_site_address_line1: str
    billing_site_address_line2: str
    billing_site_city: str
    billing_site_state: str
    billing_site_zip: str
    billing_site_country: str
    shipping_site: SiteReferenceModel
    shipping_site_address_line1: str
    shipping_site_address_line2: str
    shipping_site_city: str
    shipping_site_state: str
    shipping_site_zip: str
    shipping_site_country: str
    billing_terms: BillingTermsReferenceModel
    reference: str
    customer_p_o: str
    template_setup_id: int
    invoice_template: InvoiceTemplateDetailReferenceModel
    email_template_id: int
    add_to_batch_email_list: bool
    date: str
    restrict_downpayment_flag: bool
    location_id: int
    department_id: int
    territory_id: int
    top_comment: str
    bottom_comment: str
    taxable_flag: bool
    tax_code: TaxCodeReferenceModel
    internal_notes: str
    downpayment_previously_taxed_flag: bool
    service_total: float
    override_down_payment_amount_flag: bool
    currency: CurrencyReferenceModel
    due_date: str
    expense_total: float
    product_total: float
    previous_progress_applied: float
    service_adjustment_amount: float
    agreement_amount: float
    downpayment_applied: float
    subtotal: float
    total: float
    remaining_downpayment: float
    sales_tax: float
    adjustment_reason: str
    adjusted_by: str
    payments: float
    credits: float
    balance: float
    special_invoice_flag: bool
    billing_setup_reference: BillingSetupReferenceModel
    ticket: TicketReferenceModel
    project: ProjectReferenceModel
    phase: ProjectPhaseReferenceModel
    sales_order: SalesOrderReferenceModel
    agreement: AgreementReferenceModel
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True