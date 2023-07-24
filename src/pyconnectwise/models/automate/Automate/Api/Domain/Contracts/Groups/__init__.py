
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class MembershipConfiguration(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    membership_type: (str | None) = Field(default=None, alias='MembershipType')
    computer_search_name: (str | None) = Field(default=None, alias='ComputerSearchName')
    is_limited_to_computer_search: (bool | None) = Field(default=None, alias='IsLimitedToComputerSearch')
    network_device_search_name: (str | None) = Field(default=None, alias='NetworkDeviceSearchName')
    is_limited_to_network_device_search: (bool | None) = Field(default=None, alias='IsLimitedToNetworkDeviceSearch')
    contact_search_name: (str | None) = Field(default=None, alias='ContactSearchName')
    is_limited_to_contact_search: (bool | None) = Field(default=None, alias='IsLimitedToContactSearch')
    includes_contact_associated_computers: (bool | None) = Field(default=None, alias='IncludesContactAssociatedComputers')

class GroupType(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    group_type_id: (int | None) = Field(default=None, alias='GroupTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class LinkingSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    group_link_type_id: (int | None) = Field(default=None, alias='GroupLinkTypeId')
    group_link_type_name: (str | None) = Field(default=None, alias='GroupLinkTypeName')
    linked_entity_id: (int | None) = Field(default=None, alias='LinkedEntityId')
    linked_entity_name: (str | None) = Field(default=None, alias='LinkedEntityName')
    is_synchronized: (bool | None) = Field(default=None, alias='IsSynchronized')

class MasterStatus(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    master_status_type_id: (int | None) = Field(default=None, alias='MasterStatusTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class MaintenanceWindowSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    maintenance_window_id: (int | None) = Field(default=None, alias='MaintenanceWindowId')
    name: (str | None) = Field(default=None, alias='Name')

class RemoteAgentTemplate(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    remote_agent_template_id: (int | None) = Field(default=None, alias='RemoteAgentTemplateId')
    name: (str | None) = Field(default=None, alias='Name')

class SearchSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    auto_join_search_id: (int | None) = Field(default=None, alias='AutoJoinSearchId')
    name: (str | None) = Field(default=None, alias='Name')
    is_limited_to_search: (bool | None) = Field(default=None, alias='IsLimitedToSearch')

class ContactSearchSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    should_include_associated_computers: (bool | None) = Field(default=None, alias='ShouldIncludeAssociatedComputers')
    auto_join_search_id: (int | None) = Field(default=None, alias='AutoJoinSearchId')
    name: (str | None) = Field(default=None, alias='Name')
    is_limited_to_search: (bool | None) = Field(default=None, alias='IsLimitedToSearch')

class TemplateSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    remote_agent_template: (RemoteAgentTemplate | None) = Field(default=None, alias='RemoteAgentTemplate')
    priority: (int | None) = Field(default=None, alias='Priority')

class AutoJoinSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    computer_search_settings: (SearchSettings | None) = Field(default=None, alias='ComputerSearchSettings')
    network_device_search_settings: (SearchSettings | None) = Field(default=None, alias='NetworkDeviceSearchSettings')
    contact_search_settings: (ContactSearchSettings | None) = Field(default=None, alias='ContactSearchSettings')

class GroupAutoJoinSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    computer_auto_join_search: (Searches.Search | None) = Field(default=None, alias='ComputerAutoJoinSearch')
    is_limited_to_computer_auto_join: (bool | None) = Field(default=None, alias='IsLimitedToComputerAutoJoin')

class Group(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    group_id: (int | None) = Field(default=None, alias='GroupId')
    name: (str | None) = Field(default=None, alias='Name')
    full_name: (str | None) = Field(default=None, alias='FullName')
    description: (str | None) = Field(default=None, alias='Description')
    group_type: (GroupType | None) = Field(default=None, alias='GroupType')
    template_settings: (TemplateSettings | None) = Field(default=None, alias='TemplateSettings')
    auto_join_settings: (AutoJoinSettings | None) = Field(default=None, alias='AutoJoinSettings')
    linking_settings: (LinkingSettings | None) = Field(default=None, alias='LinkingSettings')
    master_status: (MasterStatus | None) = Field(default=None, alias='MasterStatus')
    maintenance_window_settings: (MaintenanceWindowSettings | None) = Field(default=None, alias='MaintenanceWindowSettings')

class PatchingPolicies(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    microsoft_update_policy: (Patching.MicrosoftUpdatePolicy | None) = Field(default=None, alias='MicrosoftUpdatePolicy')
    reboot_policy: (Patching.RebootPolicy | None) = Field(default=None, alias='RebootPolicy')
    third_party_update_policy: (Patching.ThirdPartyUpdatePolicy | None) = Field(default=None, alias='ThirdPartyUpdatePolicy')
    approval_policies: (list[Patching.ApprovalPolicy] | None) = Field(default=None, alias='ApprovalPolicies')
from .. import Patching, Searches
