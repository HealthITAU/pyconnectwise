from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.StateReferenceModel import StateReferenceModel
from pyconnectwise.models.manage.CountryReferenceModel import CountryReferenceModel
from pyconnectwise.models.manage.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pyconnectwise.models.manage.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pyconnectwise.models.manage.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pyconnectwise.models.manage.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pyconnectwise.models.manage.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pyconnectwise.models.manage.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pyconnectwise.models.manage.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pyconnectwise.models.manage.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from pyconnectwise.models.manage.InvoiceTemplateReferenceModel import InvoiceTemplateReferenceModel
from enum import Enum
from pyconnectwise.models.manage.EmailTemplateReferenceModel import EmailTemplateReferenceModel
from pyconnectwise.models.manage.CountryReferenceModel import CountryReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
class PrefixSuffixFlag(str, Enum):
    Prefix = 'Prefix'
    Suffix = 'Suffix'

class BillingSetupModel(ConnectWiseModel):
    id: int
    remit_name: str
    location: SystemLocationReferenceModel
    address_one: str
    address_two: str
    city: str
    state: StateReferenceModel
    zip: str
    country: CountryReferenceModel
    phone: str
    invoice_title: str
    payable_name: str
    topcomment: str
    invoice_footer: str
    quote_footer: str
    overall_invoice_default: InvoiceTemplateReferenceModel
    standard_invoice_actual: InvoiceTemplateReferenceModel
    standard_invoice_fixed: InvoiceTemplateReferenceModel
    progress_invoice: InvoiceTemplateReferenceModel
    agreement_invoice: InvoiceTemplateReferenceModel
    credit_memo_invoice: InvoiceTemplateReferenceModel
    down_payment_invoice: InvoiceTemplateReferenceModel
    misc_invoice: InvoiceTemplateReferenceModel
    sales_order_invoice: InvoiceTemplateReferenceModel
    exclude_do_not_bill_time_flag: bool
    exclude_do_not_bill_expense_flag: bool
    exclude_do_not_bill_product_flag: bool
    prefix_suffix_flag: PrefixSuffixFlag
    prefix_suffix_text: str
    charge_adj_to_firm_flag: bool
    no_watermark_flag: bool
    display_tax_flag: bool
    allow_restricted_dept_on_routing_flag: bool
    bill_ticket_separately_flag: bool
    bill_ticket_complete_flag: bool
    bill_ticket_unapproved_flag: bool
    bill_project_complete_flag: bool
    bill_project_unapproved_flag: bool
    progress_time_flag: bool
    restrict_project_downpayment_flag: bool
    bill_sales_order_complete_flag: bool
    bill_product_after_ship_flag: bool
    restrict_downpayment_flag: bool
    copy_non_service_products_flag: bool
    copy_service_products_flag: bool
    copy_agreement_products_flag: bool
    print_logo_flag: bool
    read_receipt_flag: bool
    delivery_receipt_flag: bool
    disable_routing_email_flag: bool
    email_template: EmailTemplateReferenceModel
    localized_country: CountryReferenceModel
    business_number: str
    currency: CurrencyReferenceModel
    custom_label: str
    custom_text: str
    company_code: str
    exclude_avalara_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True