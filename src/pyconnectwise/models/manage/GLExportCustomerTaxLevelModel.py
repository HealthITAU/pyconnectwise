from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class GLExportCustomerTaxLevelModel(ConnectWiseModel):
    tax_rate: float
    tax_code_xref: str
    agency_xref: str
    tax_level: int