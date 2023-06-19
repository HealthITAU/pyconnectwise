from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.KPICategoryReferenceModel import KPICategoryReferenceModel

class KPIModel(ConnectWiseModel):
    id: int
    name: str
    category: KPICategoryReferenceModel
    date_filter: str
    sort_order: int
    inactive_flag: bool

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True