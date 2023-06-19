from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.StatusIndicatorReferenceModel import StatusIndicatorReferenceModel

class PhaseStatusModel(ConnectWiseModel):
    id: int
    name: str
    default_flag: bool
    inactive_flag: bool
    collapsed_flag: bool
    closed_flag: bool
    board_association_ids: list[int]
    status_indicator: StatusIndicatorReferenceModel
    custom_status_indicator_name: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True