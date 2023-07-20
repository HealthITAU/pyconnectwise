from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ExperimentModel(ConnectWiseModel):
    id: int
    experiment_id: str
    name: str
    description: str
    properties: str
    inactive_flag: bool
    member_inactive_flag: bool
    _info: dict[str, str]