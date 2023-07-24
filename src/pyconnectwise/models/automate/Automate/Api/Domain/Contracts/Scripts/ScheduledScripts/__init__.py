
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class DistributionWindowType(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    distribution_window_type_id: (int | None) = Field(default=None, alias='DistributionWindowTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class ScheduleTargetType(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    schedule_target_type_id: (int | None) = Field(default=None, alias='ScheduleTargetTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class DistributionWindow(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    distribution_window_type: (DistributionWindowType | None) = Field(default=None, alias='DistributionWindowType')
    amount: (int | None) = Field(default=None, alias='Amount')
