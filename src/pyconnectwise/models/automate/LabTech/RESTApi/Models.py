
from __future__ import annotations
from typing import Any
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class PatchOperation(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    op: (str | None) = Field(default=None, alias='Op')
    path: (str | None) = Field(default=None, alias='Path')
    value: (dict[(str, Any)] | None) = Field(default=None, alias='Value')
