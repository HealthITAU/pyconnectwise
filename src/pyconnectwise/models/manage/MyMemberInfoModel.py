from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.DocumentReferenceModel import DocumentReferenceModel
from enum import Enum
from pyconnectwise.models.manage.TimeZoneSetupReferenceModel import TimeZoneSetupReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
from pyconnectwise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from pyconnectwise.models.manage.BoardReferenceModel import BoardReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.ProjectBoardReferenceModel import ProjectBoardReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel
from pyconnectwise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
class LicenseClass(str, Enum):
    A = 'A'
    C = 'C'
    F = 'F'
    X = 'X'

class MyMemberInfoModel(ConnectWiseModel):
    id: int
    identifier: str
    first_name: str
    middle_initial: str
    last_name: str
    full_name: str
    default_email: str
    photo: DocumentReferenceModel
    license_class: LicenseClass
    inactive_flag: bool
    time_zone: TimeZoneSetupReferenceModel
    use_browser_language_flag: bool
    default_location: SystemLocationReferenceModel
    default_department: SystemDepartmentReferenceModel
    work_role: WorkRoleReferenceModel
    work_type: WorkTypeReferenceModel
    daily_capacity: float
    require_expense_entry_flag: bool
    require_time_sheet_entry_flag: bool
    require_start_and_end_time_on_time_entry_flag: bool
    enter_time_against_company_flag: bool
    allow_expenses_entered_against_companies_flag: bool
    service_default_board: BoardReferenceModel
    service_default_location: SystemLocationReferenceModel
    service_default_department: SystemDepartmentReferenceModel
    restrict_service_default_location_flag: bool
    restrict_service_default_department_flag: bool
    excluded_service_board_ids: list[int]
    project_default_location: SystemLocationReferenceModel
    project_default_department: SystemDepartmentReferenceModel
    project_default_board: ProjectBoardReferenceModel
    restrict_project_default_location_flag: bool
    restrict_project_default_department_flag: bool
    excluded_project_board_ids: list[int]
    schedule_default_location: SystemLocationReferenceModel
    schedule_default_department: SystemDepartmentReferenceModel
    schedule_capacity: float
    service_location: ServiceLocationReferenceModel
    sales_default_location: SystemLocationReferenceModel
    warehouse: WarehouseReferenceModel
    warehouse_bin: WarehouseBinReferenceModel
    restrict_default_warehouse_flag: bool
    restrict_default_warehouse_bin_flag: bool
    sso_session_flag: bool
    sso_client_id: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True