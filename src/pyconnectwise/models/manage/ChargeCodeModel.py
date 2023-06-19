from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from enum import Enum
from pyconnectwise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from pyconnectwise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
class BillTime(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
    NoDefault = 'NoDefault'

class ChargeCodeModel(ConnectWiseModel):
    id: int
    name: str
    company: CompanyReferenceModel
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    bill_time: BillTime
    expense_entry_flag: bool
    allow_all_expense_type_flag: bool
    time_entry_flag: bool
    work_type: WorkTypeReferenceModel
    work_role: WorkRoleReferenceModel
    integration_xref: str
    expense_type_ids: list[int]
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True