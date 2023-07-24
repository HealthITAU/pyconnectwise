
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class ProbeCommand(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    probe_command_id: (int | None) = Field(default=None, alias='ProbeCommandId')
    probe_id: (int | None) = Field(default=None, alias='ProbeId')
    command: (Contracts.ProbeRemoteCommand | None) = Field(default=None, alias='Command')
    status: (Contracts.ProbeCommandStatus | None) = Field(default=None, alias='Status')
    parameters: (list[str] | None) = Field(default=None, alias='Parameters')
    output: (str | None) = Field(default=None, alias='Output')
    is_fastalk: (bool | None) = Field(default=None, alias='IsFastalk')
    date_updated: (datetime | None) = Field(default=None, alias='DateUpdated')
from .....Automate.Api.Domain import Contracts
