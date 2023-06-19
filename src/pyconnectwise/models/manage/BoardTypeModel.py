from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.BoardReferenceModel import BoardReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
class Category(str, Enum):
    Reactive = 'Reactive'
    Proactive = 'Proactive'

class BoardTypeModel(ConnectWiseModel):
    id: int
    name: str
    category: Category
    default_flag: bool
    inactive_flag: bool
    request_for_change_flag: bool
    integration_xref: str
    board: BoardReferenceModel
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True