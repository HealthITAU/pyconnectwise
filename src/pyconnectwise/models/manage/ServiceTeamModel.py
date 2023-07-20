from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel

class ServiceTeamModel(ConnectWiseModel):
    id: int
    name: str
    leader: MemberReferenceModel
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    delete_notify_flag: bool
    _info: dict[str, str]