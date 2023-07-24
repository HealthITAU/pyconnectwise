
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class MaintenanceModeQueueEntry(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    maintenance_mode_queue_id: (int | None) = Field(default=None, alias='MaintenanceModeQueueId')
    computer_id: (int | None) = Field(default=None, alias='ComputerId')
    start_date: (datetime | None) = Field(default=None, alias='StartDate')
    duration_in_minutes: (int | None) = Field(default=None, alias='DurationInMinutes')
    mode: (str | None) = Field(default=None, alias='Mode')
    user_id: (int | None) = Field(default=None, alias='UserId')
    comments: (str | None) = Field(default=None, alias='Comments')

class MaintenanceWindowDefinition(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    maintenance_window_definition_id: (int | None) = Field(default=None, alias='MaintenanceWindowDefinitionId')
    name: (str | None) = Field(default=None, alias='Name')
    comment: (str | None) = Field(default=None, alias='Comment')
