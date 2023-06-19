from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
class DefaultSpecialInvoiceType(str, Enum):
    Agreement = 'Agreement'
    CreditMemo = 'CreditMemo'
    DownPayment = 'DownPayment'
    Miscellaneous = 'Miscellaneous'
    Progress = 'Progress'
    Standard = 'Standard'

class TimeExpenseModel(ConnectWiseModel):
    id: int
    tier1_approval_flag: bool
    tier2_approval_flag: bool
    disable_time_entry_flag: bool
    require_time_note_flag: bool
    require_expense_note_flag: bool
    rounding_factor: float
    invoice_start: int
    default_special_invoice_type: DefaultSpecialInvoiceType
    internal_company: CompanyReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True