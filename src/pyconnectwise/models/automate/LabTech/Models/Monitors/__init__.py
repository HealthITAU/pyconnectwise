
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class MonitorAlertTarget(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')
    comp_id: (int | None) = Field(default=None, alias='CompId')

class MonitorState(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class MonitorRoutine(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class MonitorAlertMessages(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    success_subject: (str | None) = Field(default=None, alias='SuccessSubject')
    success_message: (str | None) = Field(default=None, alias='SuccessMessage')
    failure_subject: (str | None) = Field(default=None, alias='FailureSubject')
    failure_message: (str | None) = Field(default=None, alias='FailureMessage')

class InternalMonitorAlertStyle(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class RemoteMonitorAlertStyle(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class MonitorComparer(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class MonitorComparerSettingsFormat(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class MonitorComparerSettingsSmoothingStyle(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class MonitorComparerSettingsResultFormat(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class MonitorPluginOwner(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    control_guid: (str | None) = Field(default=None, alias='ControlGUID')
    plugin_name: (str | None) = Field(default=None, alias='PluginName')
    alteration_instructions: (str | None) = Field(default=None, alias='AlterationInstructions')

class MonitorComparerValueFormat(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class MonitorComparerMultiValueFormat(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    values: (list[str] | None) = Field(default=None, alias='Values')

class MonitorComparerSingleValueFormat(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    value: (str | None) = Field(default=None, alias='Value')

class MonitorAlertStyle(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    internal_monitor_alert_style: (InternalMonitorAlertStyle | None) = Field(default=None, alias='InternalMonitorAlertStyle')
    remote_monitor_alert_style: (RemoteMonitorAlertStyle | None) = Field(default=None, alias='RemoteMonitorAlertStyle')

class Monitor(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    alert_action: (AlertAction | None) = Field(default=None, alias='AlertAction')
    alert_style: (MonitorAlertStyle | None) = Field(default=None, alias='AlertStyle')
    comparer_settings: (MonitorComparerSettings | None) = Field(default=None, alias='ComparerSettings')
    control_guid: (str | None) = Field(default=None, alias='ControlGuid')
    failure_count: (int | None) = Field(default=None, alias='FailureCount')
    id_field: (str | None) = Field(default=None, alias='IdField')
    interval: (int | None) = Field(default=None, alias='Interval')
    installed: (bool | None) = Field(default=None, alias='Installed')
    is_internal_monitor: (bool | None) = Field(default=None, alias='IsInternalMonitor')
    is_network_device_monitor: (bool | None) = Field(default=None, alias='IsNetworkDeviceMonitor')
    last_checked: (datetime | None) = Field(default=None, alias='LastChecked')
    last_failed: (datetime | None) = Field(default=None, alias='LastFailed')
    last_status: (str | None) = Field(default=None, alias='LastStatus')
    guid: (str | None) = Field(default=None, alias='Guid')
    monitor_alert_target: (MonitorAlertTarget | None) = Field(default=None, alias='MonitorAlertTarget')
    monitor_id: (int | None) = Field(default=None, alias='MonitorId')
    monitor_owner: (MonitorOwner | None) = Field(default=None, alias='MonitorOwner')
    monitor_state: (MonitorState | None) = Field(default=None, alias='MonitorState')
    local_state: (MonitorState | None) = Field(default=None, alias='LocalState')
    name: (str | None) = Field(default=None, alias='Name')
    pending_update: (bool | None) = Field(default=None, alias='PendingUpdate')
    report_category: (ReportCategory | None) = Field(default=None, alias='ReportCategory')
    ticket_category: (TicketCategory | None) = Field(default=None, alias='TicketCategory')
    warning_count: (int | None) = Field(default=None, alias='WarningCount')
    script: (Script | None) = Field(default=None, alias='Script')
    version: (int | None) = Field(default=None, alias='Version')
    routine_parameters: (RoutineParameters.MonitorRoutineParameters | None) = Field(default=None, alias='RoutineParameters')
    routine: (MonitorRoutine | None) = Field(default=None, alias='Routine')
    alert_messages: (MonitorAlertMessages | None) = Field(default=None, alias='AlertMessages')
    targets: (MonitorTarget | None) = Field(default=None, alias='Targets')
    is_global_monitor: (bool | None) = Field(default=None, alias='IsGlobalMonitor')
    is_overridden: (bool | None) = Field(default=None, alias='IsOverridden')
    is_collecting_data: (bool | None) = Field(default=None, alias='IsCollectingData')
    affected_entities: (MonitorAffectedEntities | None) = Field(default=None, alias='AffectedEntities')

class MonitorComparerSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    comparer: (MonitorComparer | None) = Field(default=None, alias='Comparer')
    format: (MonitorComparerSettingsFormat | None) = Field(default=None, alias='Format')
    value: (MonitorComparerValue | None) = Field(default=None, alias='Value')
    smoothing_coefficient: (float | None) = Field(default=None, alias='SmoothingCoefficient')
    is_expression: (bool | None) = Field(default=None, alias='IsExpression')
    smoothing_style: (MonitorComparerSettingsSmoothingStyle | None) = Field(default=None, alias='SmoothingStyle')
    language_overrides: (dict[(str, str)] | None) = Field(default=None, alias='LanguageOverrides')
    result_format: (MonitorComparerSettingsResultFormat | None) = Field(default=None, alias='ResultFormat')

class MonitorOwner(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    owner_type: (int | None) = Field(default=None, alias='OwnerType')
    description: (str | None) = Field(default=None, alias='Description')
    owning_group: (Group | None) = Field(default=None, alias='OwningGroup')
    owning_script: (Script | None) = Field(default=None, alias='OwningScript')
    owning_plugin: (MonitorPluginOwner | None) = Field(default=None, alias='OwningPlugin')

class MonitorTarget(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    location: (Location | None) = Field(default=None, alias='Location')
    client: (Client | None) = Field(default=None, alias='Client')
    computer: (Computer | None) = Field(default=None, alias='Computer')
    network_device: (NetworkDevice | None) = Field(default=None, alias='NetworkDevice')
    group_ids: (list[int] | None) = Field(default=None, alias='GroupIds')

class MonitorAffectedEntities(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    remote_monitor_affected_location: (Location | None) = Field(default=None, alias='RemoteMonitorAffectedLocation')
    remote_monitor_affected_client: (Client | None) = Field(default=None, alias='RemoteMonitorAffectedClient')
    internal_monitor_affected_locations: (list[Location] | None) = Field(default=None, alias='InternalMonitorAffectedLocations')
    internal_monitor_affected_clients: (list[Client] | None) = Field(default=None, alias='InternalMonitorAffectedClients')

class MonitorComparerValue(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    format: (MonitorComparerValueFormat | None) = Field(default=None, alias='Format')
    multi_value_format: (MonitorComparerMultiValueFormat | None) = Field(default=None, alias='MultiValueFormat')
    state_based_value_format: (MonitorComparerStateBasedValueFormat | None) = Field(default=None, alias='StateBasedValueFormat')
    single_value_format: (MonitorComparerSingleValueFormat | None) = Field(default=None, alias='SingleValueFormat')

class MonitorComparerStateBasedValueFormat(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    normal_comparer: (MonitorComparerSettings | None) = Field(default=None, alias='NormalComparer')
    warning_comparer: (MonitorComparerSettings | None) = Field(default=None, alias='WarningComparer')
    error_comparer: (MonitorComparerSettings | None) = Field(default=None, alias='ErrorComparer')
from .. import AlertAction, Client, Computer, Group, Location, NetworkDevice, ReportCategory, Script, TicketCategory
from . import RoutineParameters
