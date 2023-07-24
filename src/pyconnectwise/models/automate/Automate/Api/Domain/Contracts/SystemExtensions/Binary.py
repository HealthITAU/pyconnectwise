
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class RunStyle(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    run_style_id: (int | None) = Field(default=None, alias='RunStyleId')
    name: (str | None) = Field(default=None, alias='Name')

class BinaryExtensionPermission(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    extension_permission_id: (int | None) = Field(default=None, alias='ExtensionPermissionId')
    extension_guid: (UUID | None) = Field(default=None, alias='ExtensionGuid', example='00000000-0000-0000-0000-000000000000')
    extension_name: (str | None) = Field(default=None, alias='ExtensionName')
    permission_id: (int | None) = Field(default=None, alias='PermissionId')
    permission_name: (str | None) = Field(default=None, alias='PermissionName')

class UserBinaryExtensionPermission(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    has_permission: (bool | None) = Field(default=None, alias='HasPermission')
    extension_permission_id: (int | None) = Field(default=None, alias='ExtensionPermissionId')
    extension_guid: (UUID | None) = Field(default=None, alias='ExtensionGuid', example='00000000-0000-0000-0000-000000000000')
    extension_name: (str | None) = Field(default=None, alias='ExtensionName')
    permission_id: (int | None) = Field(default=None, alias='PermissionId')
    permission_name: (str | None) = Field(default=None, alias='PermissionName')

class BinaryExtension(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    category: (str | None) = Field(default=None, alias='Category')
    description: (str | None) = Field(default=None, alias='Description')
    file_data: (str | None) = Field(default=None, alias='FileData')
    is_enabled: (bool | None) = Field(default=None, alias='IsEnabled')
    is_loaded_in_automation_server: (bool | None) = Field(default=None, alias='IsLoadedInAutomationServer')
    is_loaded_in_iis: (bool | None) = Field(default=None, alias='IsLoadedInIIS')
    is_remote_agent_extension: (bool | None) = Field(default=None, alias='IsRemoteAgentExtension')
    release_date: (datetime | None) = Field(default=None, alias='ReleaseDate')
    run_style: (RunStyle | None) = Field(default=None, alias='RunStyle')
    author: (str | None) = Field(default=None, alias='Author')
    file_checksum: (str | None) = Field(default=None, alias='FileChecksum')
    file_name: (str | None) = Field(default=None, alias='FileName')
    extension_name: (str | None) = Field(default=None, alias='ExtensionName')
    extension_guid: (UUID | None) = Field(default=None, alias='ExtensionGuid', example='00000000-0000-0000-0000-000000000000')
    extension_id: (int | None) = Field(default=None, alias='ExtensionId')
    version: (str | None) = Field(default=None, alias='Version')
from uuid import UUID
