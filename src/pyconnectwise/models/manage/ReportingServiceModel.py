from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ReportingServiceModel(ConnectWiseModel):
    id: int
    reporting_user_name: str
    reporting_password: str
    reporting_domain: str
    reporting_url: str
    _info: dict[str, str]