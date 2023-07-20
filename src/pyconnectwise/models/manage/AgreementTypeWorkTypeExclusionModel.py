from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pyconnectwise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel

class AgreementTypeWorkTypeExclusionModel(ConnectWiseModel):
    id: int
    type: AgreementTypeReferenceModel
    work_type: WorkTypeReferenceModel
    _info: dict[str, str]