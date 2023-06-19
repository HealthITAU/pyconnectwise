from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.ProjectRoleReferenceModel import ProjectRoleReferenceModel
from pyconnectwise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel

class ProjectTeamMemberModel(ConnectWiseModel):
    id: int
    project_id: int
    hours: float
    member: MemberReferenceModel
    project_role: ProjectRoleReferenceModel
    work_role: WorkRoleReferenceModel
    start_date: str
    end_date: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True