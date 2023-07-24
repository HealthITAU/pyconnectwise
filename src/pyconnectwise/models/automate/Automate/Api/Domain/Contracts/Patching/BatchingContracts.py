
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class HotfixOperatingSystemCombination(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    hotfix_id: (UUID | None) = Field(default=None, alias='HotfixId', example='00000000-0000-0000-0000-000000000000')
    operating_system: (str | None) = Field(default=None, alias='OperatingSystem')

class AdvanceStageRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    hotfixes_to_advance: (list[HotfixOperatingSystemCombination] | None) = Field(default=None, alias='HotfixesToAdvance')
from uuid import UUID
