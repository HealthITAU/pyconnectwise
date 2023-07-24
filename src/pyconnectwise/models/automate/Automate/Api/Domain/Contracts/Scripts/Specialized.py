
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class RemoteCommand(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    remote_command_id: (int | None) = Field(default=None, alias='RemoteCommandId')
    parameters: (str | None) = Field(default=None, alias='Parameters')

class CreateScriptFromCommandsRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_folder_id: (int | None) = Field(default=None, alias='ScriptFolderId')
    commands: (list[RemoteCommand] | None) = Field(default=None, alias='Commands')
