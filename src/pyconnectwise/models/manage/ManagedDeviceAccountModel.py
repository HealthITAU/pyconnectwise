from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ManagedDevicesIntegrationReferenceModel import ManagedDevicesIntegrationReferenceModel

class ManagedDeviceAccountModel(ConnectWiseModel):
    id: int
    username: str
    password: str
    managed_devices_integration: ManagedDevicesIntegrationReferenceModel
    _info: dict[str, str]