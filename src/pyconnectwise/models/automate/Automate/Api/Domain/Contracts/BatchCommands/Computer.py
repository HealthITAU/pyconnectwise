
from __future__ import annotations
from enum import Enum
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class EntityType(Enum):
    SYSTEM = 'System'
    COMPUTER = 'Computer'
    SITE = 'Site'
    COMPANY = 'Company'
    PROBE = 'Probe'
    NETWORK_DEVICE = 'NetworkDevice'
    TICKET = 'Ticket'
    GROUP = 'Group'
    MOBILE_DEVICE = 'MobileDevice'
    VENDOR = 'Vendor'
    VENDOR_PRODUCT = 'VendorProduct'
    POSSIBILITY = 'Possibility'
    OPPORTUNITY = 'Opportunity'
    CONTACT = 'Contact'
    USER = 'User'
    SCRIPT = 'Script'
    PLUGIN = 'Plugin'
    SERVICE = 'Service'
    SERVICE_BUNDLE = 'ServiceBundle'
    SEARCH = 'Search'
    SEARCH_FOLDER = 'SearchFolder'
    DATAVIEW = 'Dataview'
    DATAVIEW_FOLDER = 'DataviewFolder'
    USER_FOLDER = 'UserFolder'
    USER_CLASS = 'UserClass'
    SCRIPT_FOLDER = 'ScriptFolder'
    REMOTE_MONITOR_TEMPLATE = 'RemoteMonitorTemplate'
    EXTRA_FIELD = 'ExtraField'

class ExecuteResendInventoryCommandBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    inventory_types: (list[int] | None) = Field(default=None, alias='InventoryTypes')
    entity_type: (EntityType | None) = Field(default=None, alias='EntityType')
    entity_ids: (list[int] | None) = Field(default=None, alias='EntityIds')

class ExecuteComputersBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    entity_type: (EntityType | None) = Field(default=None, alias='EntityType')
    entity_ids: (list[int] | None) = Field(default=None, alias='EntityIds')

class ExecuteRebootCommandBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    reboot_type: (int | None) = Field(default=None, alias='RebootType')
    entity_type: (EntityType | None) = Field(default=None, alias='EntityType')
    entity_ids: (list[int] | None) = Field(default=None, alias='EntityIds')

class ExecuteComputerCommandResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    computer_id: (int | None) = Field(default=None, alias='ComputerId')
    command_id: (int | None) = Field(default=None, alias='CommandId')
    result_details: (ResponseResult | None) = Field(default=None, alias='ResultDetails')

class ToggleServiceUserLocalAccountCredentials(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    username: (str | None) = Field(default=None, alias='Username')
    password: (str | None) = Field(default=None, alias='Password')

class ExecuteComputersBatchResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    computer_command_result_list: (list[ExecuteComputerCommandResult] | None) = Field(default=None, alias='ComputerCommandResultList')
    contains_unsuccessful_results: (bool | None) = Field(default=None, alias='ContainsUnsuccessfulResults')

class ExecuteToggleServiceUserCommandBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    use_local_account: (bool | None) = Field(default=None, alias='UseLocalAccount')
    local_account_credentials: (ToggleServiceUserLocalAccountCredentials | None) = Field(default=None, alias='LocalAccountCredentials')
    entity_type: (EntityType | None) = Field(default=None, alias='EntityType')
    entity_ids: (list[int] | None) = Field(default=None, alias='EntityIds')
from .. import ResponseResult
