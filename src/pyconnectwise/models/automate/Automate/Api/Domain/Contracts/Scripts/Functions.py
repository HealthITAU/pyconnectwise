
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class ScriptFunctionBase(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_function_id: (int | None) = Field(default=None, alias='ScriptFunctionId')
