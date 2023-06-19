from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class GLExportInventoryTransferOffsetModel(ConnectWiseModel):
    id: int
    document_type: str
    document_date: str
    account_number: str
    gl_class: str
    total: float
    memo: str
    description: str
    gl_type_id: str

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True