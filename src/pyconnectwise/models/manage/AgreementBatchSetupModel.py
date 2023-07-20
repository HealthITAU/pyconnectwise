from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class AgreementBatchSetupModel(ConnectWiseModel):
    id: int
    next_run_date: str
    days_in_advance: int
    _info: dict[str, str]