from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class Where(str, Enum):
    OnSite = 'OnSite'
    Remote = 'Remote'
    InHouse = 'InHouse'

class ServiceLocationModel(ConnectWiseModel):
    id: int
    name: str
    where: Where
    default_flag: bool
    _info: dict[str, str]