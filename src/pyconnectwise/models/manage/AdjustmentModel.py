from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel

class AdjustmentModel(ConnectWiseModel):
    id: int
    amount: float
    description: str
    effective_date: str
    agreement_id: int
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True