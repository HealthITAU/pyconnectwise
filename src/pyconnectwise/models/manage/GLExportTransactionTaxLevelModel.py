from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class GLExportTransactionTaxLevelModel(ConnectWiseModel):
    tax_amount: float
    taxable_amount: float
    tax_code_xref: str
    tax_level: int