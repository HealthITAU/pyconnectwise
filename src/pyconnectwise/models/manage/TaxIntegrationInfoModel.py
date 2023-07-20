from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class TaxIntegrationType(str, Enum):
    Avalara = 'Avalara'

class TaxIntegrationInfoModel(ConnectWiseModel):
    id: int
    enabled_flag: bool
    tax_integration_type: TaxIntegrationType
    _info: dict[str, str]