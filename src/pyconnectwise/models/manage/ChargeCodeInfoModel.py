from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from pyconnectwise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel

class ChargeCodeInfoModel(ConnectWiseModel):
    id: int
    name: str
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    expense_entry_flag: bool
    allow_all_expense_type_flag: bool
    time_entry_flag: bool
    work_type: WorkTypeReferenceModel
    work_role: WorkRoleReferenceModel
    expense_type_ids: list[int]
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True