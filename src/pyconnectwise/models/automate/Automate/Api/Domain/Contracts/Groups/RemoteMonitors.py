
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class TargetType(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    target_type_id: (int | None) = Field(default=None, alias='TargetTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class RemoteMonitorTemplate(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    limiting_search: (Searches.Search | None) = Field(default=None, alias='LimitingSearch')
    group_id: (int | None) = Field(default=None, alias='GroupId')
    target_type: (TargetType | None) = Field(default=None, alias='TargetType')
    install_count: (int | None) = Field(default=None, alias='InstallCount')
    sub_type: (str | None) = Field(default=None, alias='SubType')
    details: (str | None) = Field(default=None, alias='Details')
    last_edited_by: (str | None) = Field(default=None, alias='LastEditedBy')
    last_edited_time: (datetime | None) = Field(default=None, alias='LastEditedTime')
    remote_monitor_id: (int | None) = Field(default=None, alias='RemoteMonitorId')
    name: (str | None) = Field(default=None, alias='Name')
    alerting_settings: (Remote.AlertingSettings | None) = Field(default=None, alias='AlertingSettings')
    configuration: (Remote.Configuration | None) = Field(default=None, alias='Configuration')
from ..Monitors import Remote
from .. import Searches
