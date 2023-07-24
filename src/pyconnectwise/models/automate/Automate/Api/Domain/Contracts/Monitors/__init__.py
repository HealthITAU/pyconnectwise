
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class MonitorCount(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    internal_monitor_total_count: (int | None) = Field(default=None, alias='InternalMonitorTotalCount')
    internal_monitor_total_disable_count: (int | None) = Field(default=None, alias='InternalMonitorTotalDisableCount')
    internal_monitor_total_detected_count: (int | None) = Field(default=None, alias='InternalMonitorTotalDetectedCount')
    remote_monitor_total_count: (int | None) = Field(default=None, alias='RemoteMonitorTotalCount')
    remote_monitor_total_failure_count: (int | None) = Field(default=None, alias='RemoteMonitorTotalFailureCount')
    remote_monitor_total_warning_count: (int | None) = Field(default=None, alias='RemoteMonitorTotalWarningCount')

class Monitor(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    monitor_id: (int | None) = Field(default=None, alias='MonitorId')
    name: (str | None) = Field(default=None, alias='Name')
    groups: (list[Groups.Group] | None) = Field(default=None, alias='Groups')
    target_computer: (Computers.Computer | None) = Field(default=None, alias='TargetComputer')
from .. import Computers, Groups
