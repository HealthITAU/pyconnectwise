from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.TimeZoneSetupReferenceModel import TimeZoneSetupReferenceModel
from pyconnectwise.models.manage.SecurityRoleReferenceModel import SecurityRoleReferenceModel
from pyconnectwise.models.manage.StructureReferenceModel import StructureReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.BoardReferenceModel import BoardReferenceModel

class ApiMemberModel(ConnectWiseModel):
    id: int
    identifier: str
    name: str
    email_address: str
    inactive_flag: bool
    inactive_date: str
    time_zone: TimeZoneSetupReferenceModel
    security_role: SecurityRoleReferenceModel
    structure_level: StructureReferenceModel
    security_location: SystemLocationReferenceModel
    default_location: SystemLocationReferenceModel
    default_department: SystemDepartmentReferenceModel
    sales_default_location: SystemLocationReferenceModel
    service_default_board: BoardReferenceModel
    notes: str
    excluded_service_board_ids: list[int]
    block_price_flag: bool
    block_cost_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True