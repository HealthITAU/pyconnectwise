from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class GroupModel(ConnectWiseModel):
    id: int
    name: str
    public_description: str
    public_flag: bool
    inactive_flag: bool
    _info: dict[str, str]