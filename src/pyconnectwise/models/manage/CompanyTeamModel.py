from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.TeamRoleReferenceModel import TeamRoleReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel

class CompanyTeamModel(ConnectWiseModel):
    id: int
    company: CompanyReferenceModel
    team_role: TeamRoleReferenceModel
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    contact: ContactReferenceModel
    member: MemberReferenceModel
    account_manager_flag: bool
    tech_flag: bool
    sales_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True