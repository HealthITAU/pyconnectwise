
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class CommandMenuItemBase(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    command_key: (str | None) = Field(default=None, alias='CommandKey')
    display_name: (str | None) = Field(default=None, alias='DisplayName')
    display_order: (int | None) = Field(default=None, alias='DisplayOrder')
    route: (str | None) = Field(default=None, alias='Route')
    require_confirmation: (bool | None) = Field(default=None, alias='RequireConfirmation')
