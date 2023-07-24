
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class GroupItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class TicketPriorityItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class RoleDefinitionItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (str | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class ReportItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class ServerFileItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (str | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class TemplatePropertyItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (str | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class UserItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class HotfixDataItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (str | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class StartupDefinitionItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class SmartAttributeItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class LicenseTypeItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class ExtraFieldDefinitionItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')
