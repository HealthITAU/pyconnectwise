
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class AlertStyleType(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    alert_style_type_id: (int | None) = Field(default=None, alias='AlertStyleTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class AlertScript(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    alert_script_id: (int | None) = Field(default=None, alias='AlertScriptId')
    name: (str | None) = Field(default=None, alias='Name')

class CheckType(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    check_type_id: (int | None) = Field(default=None, alias='CheckTypeId')
    legacy_check_type_id: (int | None) = Field(default=None, alias='LegacyCheckTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class CheckInterval(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    interval_in_seconds: (int | None) = Field(default=None, alias='IntervalInSeconds')
    name: (str | None) = Field(default=None, alias='Name')

class StateCondition(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    conditional_type_id: (int | None) = Field(default=None, alias='ConditionalTypeId')
    comparand: (str | None) = Field(default=None, alias='Comparand')

class AlertingSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_alerting_enabled: (bool | None) = Field(default=None, alias='IsAlertingEnabled')
    alert_template: (Alerts.AlertTemplate | None) = Field(default=None, alias='AlertTemplate')
    alert_style_type: (AlertStyleType | None) = Field(default=None, alias='AlertStyleType')
    alert_success_subject: (str | None) = Field(default=None, alias='AlertSuccessSubject')
    alert_success_message: (str | None) = Field(default=None, alias='AlertSuccessMessage')
    alert_failure_subject: (str | None) = Field(default=None, alias='AlertFailureSubject')
    alert_failure_message: (str | None) = Field(default=None, alias='AlertFailureMessage')
    should_run_script: (bool | None) = Field(default=None, alias='ShouldRunScript')
    alert_script: (AlertScript | None) = Field(default=None, alias='AlertScript')
    ticket_category: (Ticketing.TicketCategory | None) = Field(default=None, alias='TicketCategory')
    report_category: (Reporting.ReportCategory | None) = Field(default=None, alias='ReportCategory')

class Condition(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    condition_type_id: (int | None) = Field(default=None, alias='ConditionTypeId')
    comparand: (str | None) = Field(default=None, alias='Comparand')
    normal_state_condition: (StateCondition | None) = Field(default=None, alias='NormalStateCondition')
    warning_state_condition: (StateCondition | None) = Field(default=None, alias='WarningStateCondition')
    error_state_condition: (StateCondition | None) = Field(default=None, alias='ErrorStateCondition')

class Configuration(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    check_type: (CheckType | None) = Field(default=None, alias='CheckType')
    interval: (CheckInterval | None) = Field(default=None, alias='Interval')
    condition: (Condition | None) = Field(default=None, alias='Condition')
    ping_settings: (CheckSettings.PingSettings | None) = Field(default=None, alias='PingSettings')
    latency_settings: (CheckSettings.LatencySettings | None) = Field(default=None, alias='LatencySettings')
    tcp_settings: (CheckSettings.TcpSettings | None) = Field(default=None, alias='TcpSettings')
    udp_settings: (CheckSettings.UdpSettings | None) = Field(default=None, alias='UdpSettings')
    snmp_settings: (CheckSettings.SnmpSettings | None) = Field(default=None, alias='SnmpSettings')
    performance_counter_settings: (CheckSettings.PerformanceCounterSettings | None) = Field(default=None, alias='PerformanceCounterSettings')
    file_or_directory_settings: (CheckSettings.FileOrDirectorySettings | None) = Field(default=None, alias='FileOrDirectorySettings')
    service_settings: (CheckSettings.ServiceSettings | None) = Field(default=None, alias='ServiceSettings')
    disk_space_settings: (CheckSettings.DiskSpaceSettings | None) = Field(default=None, alias='DiskSpaceSettings')
    registry_settings: (CheckSettings.RegistrySettings | None) = Field(default=None, alias='RegistrySettings')
    process_settings: (CheckSettings.ProcessSettings | None) = Field(default=None, alias='ProcessSettings')
    event_log_settings: (CheckSettings.EventLogSettings | None) = Field(default=None, alias='EventLogSettings')
    executable_settings: (CheckSettings.ExecutableSettings | None) = Field(default=None, alias='ExecutableSettings')
    wmi_settings: (CheckSettings.WmiSettings | None) = Field(default=None, alias='WmiSettings')
    bandwidth_settings: (CheckSettings.BandwidthSettings | None) = Field(default=None, alias='BandwidthSettings')
    sensor_settings: (CheckSettings.SensorSettings | None) = Field(default=None, alias='SensorSettings')
from .. import CheckSettings
from ... import Alerts, Reporting, Ticketing
