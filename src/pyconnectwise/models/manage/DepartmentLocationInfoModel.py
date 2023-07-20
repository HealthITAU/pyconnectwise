from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel

class DepartmentLocationInfoModel(ConnectWiseModel):
    id: int
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    _info: dict[str, str]