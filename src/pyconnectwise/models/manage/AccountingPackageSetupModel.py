from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.AccountingPackageReferenceModel import AccountingPackageReferenceModel
from enum import Enum
class InvoiceFormat(str, Enum):
    Default = 'Default'
    Condensed = 'Condensed'
    Detailed = 'Detailed'
class ExpenseFormat(str, Enum):
    Default = 'Default'
    Condensed = 'Condensed'

class AccountingPackageSetupModel(ConnectWiseModel):
    id: int
    accounting_package: AccountingPackageReferenceModel
    direct_transfer_flag: bool
    include_invoices_flag: bool
    invoice_format: InvoiceFormat
    include_expenses_flag: bool
    transfer_expenses_as_bill_flag: bool
    expense_format: ExpenseFormat
    suppress_memo_flag: bool
    sync_payment_info_flag: bool
    include_sales_tax_flag: bool
    enable_tax_groups_flag: bool
    zero_dollar_tax_amounts_flag: bool
    include_items_flag: bool
    inventory_s_o_h_flag: bool
    send_component_amount_flag: bool
    send_uom_flag: bool
    include_cogs_entries_flag: bool
    include_cogs_drop_ship_flag: bool

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True