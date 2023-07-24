
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class Search(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    search_id: (int | None) = Field(default=None, alias='SearchId')
    name: (str | None) = Field(default=None, alias='Name')
    folder_name: (str | None) = Field(default=None, alias='FolderName')

class Client(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    client_id: (int | None) = Field(default=None, alias='ClientId')
    name: (str | None) = Field(default=None, alias='Name')

class Location(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    location_id: (int | None) = Field(default=None, alias='LocationId')
    name: (str | None) = Field(default=None, alias='Name')
    client: (Client | None) = Field(default=None, alias='Client')

class MaintenanceWindow(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    maintenance_window_id: (int | None) = Field(default=None, alias='MaintenanceWindowId')
    name: (str | None) = Field(default=None, alias='Name')

class UserClass(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_class_id: (int | None) = Field(default=None, alias='UserClassId')
    name: (str | None) = Field(default=None, alias='Name')

class GroupType(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    group_type_id: (int | None) = Field(default=None, alias='GroupTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class RemoteAgentTemplate(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    remote_agent_template_id: (int | None) = Field(default=None, alias='RemoteAgentTemplateId')
    name: (str | None) = Field(default=None, alias='Name')

class GroupTypeInformation(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    inherited_group_type_id: (int | None) = Field(default=None, alias='InheritedGroupTypeId')
    is_modifiable: (bool | None) = Field(default=None, alias='IsModifiable')
    group_types: (list[GroupType] | None) = Field(default=None, alias='GroupTypes')

class RemoteAgentTemplateInformation(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    inherited_remote_agent_template_id: (int | None) = Field(default=None, alias='InheritedRemoteAgentTemplateId')
    is_modifiable: (bool | None) = Field(default=None, alias='IsModifiable')
    remote_agent_templates: (list[RemoteAgentTemplate] | None) = Field(default=None, alias='RemoteAgentTemplates')

class ComputerSearchInformation(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_modifiable: (bool | None) = Field(default=None, alias='IsModifiable')
    searches: (list[Search] | None) = Field(default=None, alias='Searches')

class GroupConfigurationViewModel(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    group_type_information: (GroupTypeInformation | None) = Field(default=None, alias='GroupTypeInformation')
    remote_agent_template_information: (RemoteAgentTemplateInformation | None) = Field(default=None, alias='RemoteAgentTemplateInformation')
    computer_search_information: (ComputerSearchInformation | None) = Field(default=None, alias='ComputerSearchInformation')
    network_device_searches: (list[Search] | None) = Field(default=None, alias='NetworkDeviceSearches')
    contact_searches: (list[Search] | None) = Field(default=None, alias='ContactSearches')
    clients: (list[Client] | None) = Field(default=None, alias='Clients')
    locations: (list[Location] | None) = Field(default=None, alias='Locations')
    maintenance_windows: (list[MaintenanceWindow] | None) = Field(default=None, alias='MaintenanceWindows')
    user_classes: (list[UserClass] | None) = Field(default=None, alias='UserClasses')
