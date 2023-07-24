
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class NetworkDevice(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    network_device_id: (int | None) = Field(default=None, alias='NetworkDeviceId')
    name: (str | None) = Field(default=None, alias='Name')
    friendly_name: (str | None) = Field(default=None, alias='FriendlyName')
