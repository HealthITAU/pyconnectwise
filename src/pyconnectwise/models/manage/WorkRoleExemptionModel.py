from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel

class WorkRoleExemptionModel(ConnectWiseModel):
    id: int
    work_role: WorkRoleReferenceModel
    taxable_levels: list[int]
    _info: dict[str, str]