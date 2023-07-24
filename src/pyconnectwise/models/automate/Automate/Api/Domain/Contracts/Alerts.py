
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class AlertClient(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class AlertComputer(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')
    computer_status: (str | None) = Field(default=None, alias='ComputerStatus')

class AlertDevice(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class AlertLocation(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class AlertMonitor(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class AlertSeverityItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class AlertTemplate(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    alert_template_id: (int | None) = Field(default=None, alias='AlertTemplateId')
    name: (str | None) = Field(default=None, alias='Name')

class Alert(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    alert_id: (int | None) = Field(default=None, alias='AlertId')
    client: (AlertClient | None) = Field(default=None, alias='Client')
    computer: (AlertComputer | None) = Field(default=None, alias='Computer')
    device: (AlertDevice | None) = Field(default=None, alias='Device')
    location: (AlertLocation | None) = Field(default=None, alias='Location')
    monitor: (AlertMonitor | None) = Field(default=None, alias='Monitor')
    alert_date: (datetime | None) = Field(default=None, alias='AlertDate')
    severity: (AlertSeverityItem | None) = Field(default=None, alias='Severity')
    source: (str | None) = Field(default=None, alias='Source')
    message: (str | None) = Field(default=None, alias='Message')
    field_name: (str | None) = Field(default=None, alias='FieldName')
    alert_age: (str | None) = Field(default=None, alias='AlertAge')
