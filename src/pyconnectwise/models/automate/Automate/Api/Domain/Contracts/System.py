
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class ClientPermissionsResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    client_id: (int | None) = Field(default=None, alias='ClientId')
    permissions: (list[str] | None) = Field(default=None, alias='Permissions')

class PasswordResetConfigurationResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    can_generate_password_reset_token: (bool | None) = Field(default=None, alias='CanGeneratePasswordResetToken')

class PasswordResetTokenRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    username: (str | None) = Field(default=None, alias='Username')
    password_reset_token: (str | None) = Field(default=None, alias='PasswordResetToken')

class PasswordResetTokenResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_valid: (bool | None) = Field(default=None, alias='IsValid')

class ValidatePasswordResetRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    password_reset_token: (str | None) = Field(default=None, alias='PasswordResetToken')

class ServerInformation(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    server_id: (int | None) = Field(default=None, alias='ServerId')
    operating_system: (str | None) = Field(default=None, alias='OperatingSystem')
    mac_address: (str | None) = Field(default=None, alias='MacAddress')
    machine_name: (str | None) = Field(default=None, alias='MachineName')
    cpu_name: (str | None) = Field(default=None, alias='CPUName')
    cpu_sockets: (int | None) = Field(default=None, alias='CPUSockets')
    cpu_cores: (int | None) = Field(default=None, alias='CPUCores')
    logical_processors: (int | None) = Field(default=None, alias='LogicalProcessors')
    memory_total: (int | None) = Field(default=None, alias='MemoryTotal')
    is_database_server: (bool | None) = Field(default=None, alias='IsDatabaseServer')
    is_web_server: (bool | None) = Field(default=None, alias='IsWebServer')
