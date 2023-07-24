
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class AccountInformation(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_trial_account: (bool | None) = Field(default=None, alias='IsTrialAccount')

class ResponseResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    result_status: (int | None) = Field(default=None, alias='ResultStatus')
    reason_code: (int | None) = Field(default=None, alias='ReasonCode')
    message: (str | None) = Field(default=None, alias='Message')

class CommandPromptCommand(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    run_as_admin: (bool | None) = Field(default=None, alias='RunAsAdmin')
    use_power_shell: (bool | None) = Field(default=None, alias='UsePowerShell')
    command_text: (str | None) = Field(default=None, alias='CommandText')
    directory: (str | None) = Field(default=None, alias='Directory')

class DatabaseInformation(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    database_id: (int | None) = Field(default=None, alias='DatabaseId')
    database_version: (str | None) = Field(default=None, alias='DatabaseVersion')
    uptime: (str | None) = Field(default=None, alias='Uptime')
    current_connections: (int | None) = Field(default=None, alias='CurrentConnections')
    max_connections: (int | None) = Field(default=None, alias='MaxConnections')
    peak_connections: (int | None) = Field(default=None, alias='PeakConnections')
    running_queries: (int | None) = Field(default=None, alias='RunningQueries')
    last_backup_file_path: (str | None) = Field(default=None, alias='LastBackupFilePath')
    last_backup_date: (datetime | None) = Field(default=None, alias='LastBackupDate')
    last_backup_size: (str | None) = Field(default=None, alias='LastBackupSize')
    last_backup_status: (int | None) = Field(default=None, alias='LastBackupStatus')

class ExecuteDeviceScriptRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_id: (int | None) = Field(default=None, alias='ScriptId')
    parameter_list: (list[str] | None) = Field(default=None, alias='ParameterList')
    device_id_list: (list[int] | None) = Field(default=None, alias='DeviceIdList')

class ExecuteDeviceScriptResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    device_id: (int | None) = Field(default=None, alias='DeviceId')
    result_details: (ResponseResult | None) = Field(default=None, alias='ResultDetails')

class ProbeRemoteCommand(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')
    description: (str | None) = Field(default=None, alias='Description')

class ProbeCommandStatus(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class ProbeCommandHistoryEntry(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    probe_command_history_id: (int | None) = Field(default=None, alias='ProbeCommandHistoryId')
    probe_id: (int | None) = Field(default=None, alias='ProbeId')
    date_executed: (datetime | None) = Field(default=None, alias='DateExecuted')
    status: (ProbeCommandStatus | None) = Field(default=None, alias='Status')
    probe_remote_command: (ProbeRemoteCommand | None) = Field(default=None, alias='ProbeRemoteCommand')
    output: (str | None) = Field(default=None, alias='Output')
    user: (str | None) = Field(default=None, alias='User')
    date_finished: (datetime | None) = Field(default=None, alias='DateFinished')

class InstallerRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    location_id: (int | None) = Field(default=None, alias='LocationId')
    installer_type: (int | None) = Field(default=None, alias='InstallerType')

class ExecuteDeviceScriptResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_result_list: (list[ExecuteDeviceScriptResult] | None) = Field(default=None, alias='ScriptResultList')
    contains_unsuccessful_results: (bool | None) = Field(default=None, alias='ContainsUnsuccessfulResults')
