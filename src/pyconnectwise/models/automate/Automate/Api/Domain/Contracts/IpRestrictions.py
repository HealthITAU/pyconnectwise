
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class IpRestrictionRule(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ip_address_guid: (UUID | None) = Field(default=None, alias='IpAddressGuid', example='00000000-0000-0000-0000-000000000000')
    name: (str | None) = Field(default=None, alias='Name')
    ip_address: (str | None) = Field(default=None, alias='IpAddress')
    windows_client_access: (bool | None) = Field(default=None, alias='WindowsClientAccess')
    web_client_access: (bool | None) = Field(default=None, alias='WebClientAccess')
    created_by: (str | None) = Field(default=None, alias='CreatedBy')
    create_date: (datetime | None) = Field(default=None, alias='CreateDate')
    updated_by: (str | None) = Field(default=None, alias='UpdatedBy')
    update_date: (datetime | None) = Field(default=None, alias='UpdateDate')

class IpRestrictionStatus(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_enabled: (bool | None) = Field(default=None, alias='IsEnabled')
from uuid import UUID
