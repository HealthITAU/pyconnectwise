from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class AddLevel(str, Enum):
    NONE = 'NONE'
    My = 'My'
    All = 'All'
class EditLevel(str, Enum):
    NONE = 'NONE'
    My = 'My'
    All = 'All'
class DeleteLevel(str, Enum):
    NONE = 'NONE'
    My = 'My'
    All = 'All'
class InquireLevel(str, Enum):
    NONE = 'NONE'
    My = 'My'
    All = 'All'

class ProjectSecurityRoleSettingModel(ConnectWiseModel):
    id: int
    add_level: AddLevel
    edit_level: EditLevel
    delete_level: DeleteLevel
    inquire_level: InquireLevel
    module_identifier: str
    my_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True