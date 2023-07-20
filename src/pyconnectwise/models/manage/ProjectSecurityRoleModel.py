from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ProjectSecurityRoleModel(ConnectWiseModel):
    id: int
    name: str
    manager_role_flag: bool
    default_contact_flag: bool
    _info: dict[str, str]