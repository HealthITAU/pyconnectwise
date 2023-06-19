from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class BillExpenses(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'
class InvoiceMarkupOption(str, Enum):
    Amount = 'Amount'
    Mile = 'Mile'
    Percent = 'Percent'

class ExpenseTypeModel(ConnectWiseModel):
    id: int
    name: str
    amount_caption: str
    reimbursement_rate: float
    bill_expenses: BillExpenses
    invoice_markup_option: InvoiceMarkupOption
    invoice_markup_amount: float
    advanced_amount_flag: bool
    mileage_flag: bool
    quantity_flag: bool
    inactive_flag: bool
    max_amount: float
    integration_x_ref: str
    default_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True