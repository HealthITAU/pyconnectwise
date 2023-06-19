from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class Task(str, Enum):
    All = 'All'
    Closed = 'Closed'
    Open = 'Open'

class ServiceSignoffModel(ConnectWiseModel):
    id: int
    name: str
    default_flag: bool
    visible_logo_flag: bool
    company_info_flag: bool
    billing_terms_flag: bool
    summary_flag: bool
    discussion_flag: bool
    task_flag: bool
    task: Task
    configurations_flag: bool
    internal_notes_flag: bool
    resolution_flag: bool
    time_flag: bool
    time_member_flag: bool
    time_date_flag: bool
    time_start_end_flag: bool
    time_bill_flag: bool
    time_hours_flag: bool
    time_rate_flag: bool
    time_extended_amount_flag: bool
    time_work_type_flag: bool
    time_agreement_flag: bool
    time_notes_flag: bool
    time_manual_flag: bool
    time_manual_entry: int
    time_tax_flag: bool
    expense_flag: bool
    expense_date_flag: bool
    expense_member_flag: bool
    expense_type_flag: bool
    expense_bill_flag: bool
    expense_amount_flag: bool
    expense_agreement_flag: bool
    expense_notes_flag: bool
    expense_tax_flag: bool
    expense_manual_flag: bool
    expense_manual_entry: int
    product_flag: bool
    product_description_flag: bool
    product_bill_flag: bool
    product_quantity_flag: bool
    product_price_flag: bool
    product_extended_amount_flag: bool
    product_agreement_flag: bool
    product_manual_flag: bool
    product_manual_entry: int
    product_tax_flag: bool
    technician_signoff_flag: bool
    customer_signoff_text_flag: bool
    customer_signoff_text: str
    customer_signoff_fields_flag: bool
    billing_methods_text_flag: bool
    billing_methods_text: str
    credit_card_fields_flag: bool
    default_f_f_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True