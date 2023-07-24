
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class WebExtensionBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    web_extension_ids: (list[int] | None) = Field(default=None, alias='WebExtensionIds')
