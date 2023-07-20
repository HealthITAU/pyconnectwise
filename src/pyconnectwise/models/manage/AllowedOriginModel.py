from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class AllowedOriginModel(ConnectWiseModel):
    id: int
    origin: str
    description: str
    last_update_utc: str
    updated_by: str
    _info: dict[str, str]