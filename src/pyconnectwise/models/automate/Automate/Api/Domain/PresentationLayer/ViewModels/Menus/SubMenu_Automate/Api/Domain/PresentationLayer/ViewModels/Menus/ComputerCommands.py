
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class CommandMenuItemBase(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    display_name: (str | None) = Field(default=None, alias='DisplayName')
    display_order: (int | None) = Field(default=None, alias='DisplayOrder')
    menu_key: (str | None) = Field(default=None, alias='MenuKey')
    sub_menus: (list[CommandMenuItemBase] | None) = Field(default=None, alias='SubMenus')
    menu_items: (list[ComputerCommands.CommandMenuItemBase] | None) = Field(default=None, alias='MenuItems')
from ....... import ComputerCommands
