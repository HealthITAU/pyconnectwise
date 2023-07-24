
from __future__ import annotations
from enum import Enum
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class RequestType(Enum):
    INVITE = 'Invite'
    RESET = 'Reset'

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

class WebClientAccessBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    request_type: (RequestType | None) = Field(default=None, alias='RequestType')
    entity_type: (EntityType | None) = Field(default=None, alias='EntityType')
    entity_ids: (list[int] | None) = Field(default=None, alias='EntityIds')

class RequestTypeModel(Enum):
    ADD = 'Add'
    REMOVE = 'Remove'

class ContactPermissionBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    request_type: (RequestTypeModel | None) = Field(default=None, alias='RequestType')
    contact_ids: (list[int] | None) = Field(default=None, alias='ContactIds')
    permissions: (list[str] | None) = Field(default=None, alias='Permissions')

class ContactPermissionBatchResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    contact_id: (int | None) = Field(default=None, alias='ContactId')
    result_details: (ResponseResult | None) = Field(default=None, alias='ResultDetails')

class WebClientAccessBatchResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    contact_id: (int | None) = Field(default=None, alias='ContactId')
    result_details: (ResponseResult | None) = Field(default=None, alias='ResultDetails')

class ContactPermissionBatchResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    contact_permission_results: (list[ContactPermissionBatchResult] | None) = Field(default=None, alias='ContactPermissionResults')
    contains_unsuccessful_results: (bool | None) = Field(default=None, alias='ContainsUnsuccessfulResults')

class WebClientAccessBatchResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    web_client_access_results: (list[WebClientAccessBatchResult] | None) = Field(default=None, alias='WebClientAccessResults')
    contains_unsuccessful_results: (bool | None) = Field(default=None, alias='ContainsUnsuccessfulResults')
from . import ResponseResult
