
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class CommandHistory(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    computer_id: (int | None) = Field(default=None, alias='ComputerId')
    date_executed: (datetime | None) = Field(default=None, alias='DateExecuted')
    command_id: (int | None) = Field(default=None, alias='CommandId')
    command: (str | None) = Field(default=None, alias='Command')
    status: (str | None) = Field(default=None, alias='Status')
    output: (str | None) = Field(default=None, alias='Output')
    parameters: (str | None) = Field(default=None, alias='Parameters')
    user: (str | None) = Field(default=None, alias='User')
    date_finished: (datetime | None) = Field(default=None, alias='DateFinished')
