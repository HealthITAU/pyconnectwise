
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class CommandMenuItemBase(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    menu_key: (str | None) = Field(default=None, alias='MenuKey')
    sub_menus: (list[ComputerCommands.CommandMenuItemBase] | None) = Field(default=None, alias='SubMenus')
    menu_items: (list[ComputerCommands_1.CommandMenuItemBase] | None) = Field(default=None, alias='MenuItems')
from .......SubMenu_Automate.Api.Domain.PresentationLayer.ViewModels.Menus import ComputerCommands
from ....... import ComputerCommands as ComputerCommands_1
