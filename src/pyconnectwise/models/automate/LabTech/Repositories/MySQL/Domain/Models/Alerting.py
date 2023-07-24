
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class MonitorAlertSuspension(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    computer_id: (int | None) = Field(default=None, alias='ComputerId')
    monitor: (Monitors.Monitor | None) = Field(default=None, alias='Monitor')
    suspension_date: (datetime | None) = Field(default=None, alias='SuspensionDate')
from .....Models import Monitors
