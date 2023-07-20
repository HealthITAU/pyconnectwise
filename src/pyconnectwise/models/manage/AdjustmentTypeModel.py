from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class AdjustmentTypeModel(ConnectWiseModel):
    id: int
    identifier: str
    name: str
    audit_trail_flag: bool
    date_created: str
    created_by: str
    _info: dict[str, str]