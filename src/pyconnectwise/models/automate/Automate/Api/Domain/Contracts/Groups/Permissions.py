
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class GroupPermissionSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_inherited: (bool | None) = Field(default=None, alias='IsInherited')
    computer_permission_settings: (dict[(str, list[str])] | None) = Field(default=None, alias='ComputerPermissionSettings')
