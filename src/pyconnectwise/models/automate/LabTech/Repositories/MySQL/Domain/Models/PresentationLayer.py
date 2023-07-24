
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class UserProfile(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_super_admin: (bool | None) = Field(default=None, alias='IsSuperAdmin')
    is_folder_limited: (bool | None) = Field(default=None, alias='IsFolderLimited')
    user_class_id_list: (list[int] | None) = Field(default=None, alias='UserClassIdList')
