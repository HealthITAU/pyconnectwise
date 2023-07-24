
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class GroupTreeItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    group_id: (int | None) = Field(default=None, alias='GroupId')
    parent_id: (int | None) = Field(default=None, alias='ParentId')
    name: (str | None) = Field(default=None, alias='Name')
    full_name: (str | None) = Field(default=None, alias='FullName')
    user_has_direct_access: (bool | None) = Field(default=None, alias='UserHasDirectAccess')
    is_limited_to_computer_auto_join_search: (bool | None) = Field(default=None, alias='IsLimitedToComputerAutoJoinSearch')
    is_limited_to_network_device_auto_join_search: (bool | None) = Field(default=None, alias='IsLimitedToNetworkDeviceAutoJoinSearch')
    is_limited_to_contact_auto_join_search: (bool | None) = Field(default=None, alias='IsLimitedToContactAutoJoinSearch')
    parent_groups: (list[GroupTreeItem] | None) = Field(default=None, alias='ParentGroups')
    child_groups: (list[GroupTreeItem] | None) = Field(default=None, alias='ChildGroups')
    direct_computer_membership_count: (int | None) = Field(default=None, alias='DirectComputerMembershipCount')
    indirect_computer_membership_count: (int | None) = Field(default=None, alias='IndirectComputerMembershipCount')
