from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel

class AgreementWorkRoleExclusionModel(ConnectWiseModel):
    id: int
    work_role: WorkRoleReferenceModel
    agreement_id: int
    _info: dict[str, str]