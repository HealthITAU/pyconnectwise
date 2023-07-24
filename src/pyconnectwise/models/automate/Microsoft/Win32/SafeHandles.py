
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class SafeWaitHandle(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_invalid: (bool | None) = Field(default=None, alias='IsInvalid')
    is_closed: (bool | None) = Field(default=None, alias='IsClosed')
