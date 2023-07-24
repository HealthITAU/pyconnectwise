
from __future__ import annotations
from datetime import datetime
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

class ScheduleScriptBatchResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    entity_id: (int | None) = Field(default=None, alias='EntityId')
    result_details: (ResponseResult | None) = Field(default=None, alias='ResultDetails')

class DeleteScriptBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_ids: (list[int] | None) = Field(default=None, alias='ScriptIds')

class DeleteScriptBatchResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_id: (int | None) = Field(default=None, alias='ScriptId')
    result_details: (ResponseResult | None) = Field(default=None, alias='ResultDetails')

class ScheduleScriptBatchResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_results: (list[ScheduleScriptBatchResult] | None) = Field(default=None, alias='ScriptResults')
    contains_unsuccessful_results: (bool | None) = Field(default=None, alias='ContainsUnsuccessfulResults')

class DeleteScriptBatchResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_results: (list[DeleteScriptBatchResult] | None) = Field(default=None, alias='ScriptResults')
    contains_unsuccessful_results: (bool | None) = Field(default=None, alias='ContainsUnsuccessfulResults')

class ScheduleScriptBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    entity_type: (EntityType | None) = Field(default=None, alias='EntityType')
    entity_ids: (list[int] | None) = Field(default=None, alias='EntityIds')
    script_id: (int | None) = Field(default=None, alias='ScriptId')
    script_guid: (str | None) = Field(default=None, alias='ScriptGuid')
    schedule: (Scripts.ScriptScheduleSettings | None) = Field(default=None, alias='Schedule')
    parameters: (list[String_System.String] | None) = Field(default=None, alias='Parameters')
    use_agent_time: (bool | None) = Field(default=None, alias='UseAgentTime')
    start_date: (datetime | None) = Field(default=None, alias='StartDate')
    expire_date: (datetime | None) = Field(default=None, alias='ExpireDate')
    offline_action_flags: (Scripts.ScheduledScriptOfflineActionFlags | None) = Field(default=None, alias='OfflineActionFlags')
    distribution_window: (ScheduledScripts.DistributionWindow | None) = Field(default=None, alias='DistributionWindow')
    priority: (int | None) = Field(default=None, alias='Priority')
    include_sub_groups: (bool | None) = Field(default=None, alias='IncludeSubGroups')
from .Scripts import ScheduledScripts
from . import ResponseResult, Scripts
from .....System.Collections.Generic.KeyValuePair_System import String_System
