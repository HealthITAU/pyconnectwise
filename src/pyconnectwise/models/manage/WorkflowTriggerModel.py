from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.UserDefinedFieldReferenceModel import UserDefinedFieldReferenceModel

class WorkflowTriggerModel(ConnectWiseModel):
    id: int
    name: str
    description: str
    has_options_flag: bool
    has_operator_flag: bool
    custom_field: UserDefinedFieldReferenceModel
    expected_type: str
    _info: dict[str, str]