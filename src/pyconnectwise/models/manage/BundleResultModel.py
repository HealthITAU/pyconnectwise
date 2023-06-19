from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.IRestIdentifiedItemModel import IRestIdentifiedItemModel
from pyconnectwise.models.manage.ErrorResponseMessageModel import ErrorResponseMessageModel

class BundleResultModel(ConnectWiseModel):
    sequence_number: int
    resource_type: str
    entities: list[IRestIdentifiedItemModel]
    count: int
    version: str
    success: bool
    status_code: int
    error: ErrorResponseMessageModel

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True