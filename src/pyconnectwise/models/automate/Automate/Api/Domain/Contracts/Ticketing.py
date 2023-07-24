
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class TicketCategory(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    category_id: (int | None) = Field(default=None, alias='CategoryId')
    category_name: (str | None) = Field(default=None, alias='CategoryName')

class TicketLevel(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ticket_level_id: (int | None) = Field(default=None, alias='TicketLevelId')
    name: (str | None) = Field(default=None, alias='Name')
