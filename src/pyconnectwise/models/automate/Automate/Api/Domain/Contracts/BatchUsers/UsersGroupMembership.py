
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class UsersGroupMembershipBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_ids: (list[int] | None) = Field(default=None, alias='UserIds')
    group_ids: (list[int] | None) = Field(default=None, alias='GroupIds')
