
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class PatchActionInformation(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    computer_id: (int | None) = Field(default=None, alias='ComputerId')
    product_key_id_list: (list[str] | None) = Field(default=None, alias='ProductKeyIdList')

class ExecutePatchActionRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    patch_action_detail_list: (list[PatchActionInformation] | None) = Field(default=None, alias='PatchActionDetailList')
