from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class TaxIntegrationType(str, Enum):
    Avalara = 'Avalara'

class TaxIntegrationModel(ConnectWiseModel):
    tax_integration_type: TaxIntegrationType
    id: int
    account_number: str
    license_key: str
    service_url: str
    company_code: str
    time_tax_code: str
    expense_tax_code: str
    product_tax_code: str
    invoice_amount_tax_code: str
    enabled_flag: bool
    commit_transactions_flag: bool
    sales_invoice_flag: bool
    freight_tax_code: str
    accounting_integration_flag: bool
    tax_line_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True