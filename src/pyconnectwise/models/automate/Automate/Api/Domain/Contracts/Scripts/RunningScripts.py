
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class RunningScriptTargetType(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    target_type_id: (int | None) = Field(default=None, alias='TargetTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class RunningScript(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_instance_id: (int | None) = Field(default=None, alias='ScriptInstanceId')
    target: (RunningScriptTarget | None) = Field(default=None, alias='Target')
    script: (Script | None) = Field(default=None, alias='Script')
    source: (ScriptSource | None) = Field(default=None, alias='Source')
    state: (ScriptState | None) = Field(default=None, alias='State')
    start_date: (datetime | None) = Field(default=None, alias='StartDate')

class RunningScriptTarget(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    target_type: (RunningScriptTargetType | None) = Field(default=None, alias='TargetType')
    computer: (Computers.Computer | None) = Field(default=None, alias='Computer')
    client: (Clients.Client | None) = Field(default=None, alias='Client')
from . import Script, ScriptSource, ScriptState
from .. import Clients, Computers
