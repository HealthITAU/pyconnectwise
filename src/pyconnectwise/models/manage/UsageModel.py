from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class UsageModel(ConnectWiseModel):
    type: str
    count: int
    id: int
    description: str
    hyperlink: str
    type_key: str