from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel

class GLExportExpenseOffsetModel(ConnectWiseModel):
    id: int
    document_date: str
    document_type: str
    account_number: str
    gl_type_id: str
    gl_class: str
    member: MemberReferenceModel
    memo: str
    description: str
    total: float

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True