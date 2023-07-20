from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel

class TodayPageCategoryModel(ConnectWiseModel):
    id: int
    name: str
    sort_order: int
    location: SystemLocationReferenceModel
    _info: dict[str, str]