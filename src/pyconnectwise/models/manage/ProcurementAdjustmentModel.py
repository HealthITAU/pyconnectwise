from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.AdjustmentTypeReferenceModel import AdjustmentTypeReferenceModel
from pyconnectwise.models.manage.AdjustmentDetailModel import AdjustmentDetailModel

class ProcurementAdjustmentModel(ConnectWiseModel):
    id: int
    identifier: str
    type: AdjustmentTypeReferenceModel
    reason: str
    notes: str
    closed_flag: bool
    closed_by: str
    closed_date: str
    adjustment_details: list[AdjustmentDetailModel]
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True