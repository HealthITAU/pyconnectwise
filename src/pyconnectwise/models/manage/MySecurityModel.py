from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
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

class MySecurityModel(ConnectWiseModel):
    id: int
    add_level: AddLevel
    edit_level: EditLevel
    delete_level: DeleteLevel
    inquire_level: InquireLevel
    module_function_name: str
    module_function_description: str
    my_all_flag: bool
    module_function_identifier: str
    report_flag: bool
    restrict_flag: bool
    custom_flag: bool
    module_description: str
    module_identifier: str
    module_name: str
    sort_order: int
    member: MemberReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True