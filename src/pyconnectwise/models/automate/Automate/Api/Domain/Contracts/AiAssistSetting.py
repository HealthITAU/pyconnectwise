
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class AiAssistSettingBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ai_assist_setting_guids: (list[UUID] | None) = Field(default=None, alias='AiAssistSettingGuids')
from uuid import UUID
