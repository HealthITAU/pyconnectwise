from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel

class WarehouseBinInfoModel(ConnectWiseModel):
    id: int
    name: str
    warehouse: WarehouseReferenceModel
    inactive_flag: bool
    default_flag: bool
    _info: dict[str, str]