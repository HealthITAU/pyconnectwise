
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class ScheduledScriptOfflineActionFlags(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    skips_offline_agents: (bool | None) = Field(default=None, alias='SkipsOfflineAgents')
    wakes_offline_agents: (bool | None) = Field(default=None, alias='WakesOfflineAgents')
    only_runs_on_offline_agents: (bool | None) = Field(default=None, alias='OnlyRunsOnOfflineAgents')

class ScriptState(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    state_id: (int | None) = Field(default=None, alias='StateId')
    name: (str | None) = Field(default=None, alias='Name')

class ScriptFolder(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_folder_id: (int | None) = Field(default=None, alias='ScriptFolderId')
    name: (str | None) = Field(default=None, alias='Name')
    child_folders: (list[ScriptFolder] | None) = Field(default=None, alias='ChildFolders')

class ScriptTarget(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_target_type_id: (int | None) = Field(default=None, alias='ScriptTargetTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class ScriptOptions(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_isolated_script: (bool | None) = Field(default=None, alias='IsIsolatedScript')
    is_maintenance_script: (bool | None) = Field(default=None, alias='IsMaintenanceScript')
    is_function_script: (bool | None) = Field(default=None, alias='IsFunctionScript')
    is_offline_script: (bool | None) = Field(default=None, alias='IsOfflineScript')
    is_system_script: (bool | None) = Field(default=None, alias='IsSystemScript')

class SourceType(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    source_type_id: (int | None) = Field(default=None, alias='SourceTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class ScriptFunctionTarget(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    target_type_id: (int | None) = Field(default=None, alias='TargetTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class ScriptFunctionParameter(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: (str | None) = Field(default=None, alias='Name')
    description: (str | None) = Field(default=None, alias='Description')
    type: (str | None) = Field(default=None, alias='Type')

class SubmittableScriptFolder(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_folder_id: (int | None) = Field(default=None, alias='ScriptFolderId')
    name: (str | None) = Field(default=None, alias='Name')

class ScriptSummary(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: (str | None) = Field(default=None, alias='Name')
    description: (str | None) = Field(default=None, alias='Description')
    folder: (ScriptFolder | None) = Field(default=None, alias='Folder')
    script_target_type: (ScriptTarget | None) = Field(default=None, alias='ScriptTargetType')
    script_options: (ScriptOptions | None) = Field(default=None, alias='ScriptOptions')
    automation_minutes: (int | None) = Field(default=None, alias='AutomationMinutes')

class ScriptSource(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    source_type: (SourceType | None) = Field(default=None, alias='SourceType')
    name: (str | None) = Field(default=None, alias='Name')
    alternative_name: (str | None) = Field(default=None, alias='AlternativeName')

class ScriptStep(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    operating_system: (int | None) = Field(default=None, alias='OperatingSystem')
    is_enabled: (bool | None) = Field(default=None, alias='IsEnabled')
    should_continue_on_failure: (bool | None) = Field(default=None, alias='ShouldContinueOnFailure')
    indentation_level: (int | None) = Field(default=None, alias='IndentationLevel')
    function: (Functions.ScriptFunctionBase | None) = Field(default=None, alias='Function')

class ScriptFunction(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    function_id: (int | None) = Field(default=None, alias='FunctionId')
    name: (str | None) = Field(default=None, alias='Name')
    is_conditional_function: (bool | None) = Field(default=None, alias='IsConditionalFunction')
    description: (str | None) = Field(default=None, alias='Description')
    target_type: (ScriptFunctionTarget | None) = Field(default=None, alias='TargetType')
    parameters: (list[ScriptFunctionParameter] | None) = Field(default=None, alias='Parameters')

class Script(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_id: (int | None) = Field(default=None, alias='ScriptId')
    ticket_entry_settings: (Settings.TicketEntrySettings | None) = Field(default=None, alias='TicketEntrySettings')
    time_entry_settings: (Settings.TimeEntrySettings | None) = Field(default=None, alias='TimeEntrySettings')
    user_class_access_settings: (list[Settings.UserClassAccess] | None) = Field(default=None, alias='UserClassAccessSettings')
    is_protected: (bool | None) = Field(default=None, alias='IsProtected')
    uses_enhanced_logging: (bool | None) = Field(default=None, alias='UsesEnhancedLogging')
    steps: (list[ScriptStep] | None) = Field(default=None, alias='Steps')
    global_variables: (dict[(str, str)] | None) = Field(default=None, alias='GlobalVariables')
    parameters: (list[str] | None) = Field(default=None, alias='Parameters')
    name: (str | None) = Field(default=None, alias='Name')
    description: (str | None) = Field(default=None, alias='Description')
    folder: (ScriptFolder | None) = Field(default=None, alias='Folder')
    script_target_type: (ScriptTarget | None) = Field(default=None, alias='ScriptTargetType')
    script_options: (ScriptOptions | None) = Field(default=None, alias='ScriptOptions')
    automation_minutes: (int | None) = Field(default=None, alias='AutomationMinutes')

class ScriptScheduleSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_schedule_frequency: (Frequency.ScriptScheduleFrequency | None) = Field(default=None, alias='ScriptScheduleFrequency')
    minutely_settings: (Frequency.MinutelyScheduleFrequency | None) = Field(default=None, alias='MinutelySettings')
    hourly_settings: (Frequency.HourlyScheduleFrequency | None) = Field(default=None, alias='HourlySettings')
    daily_settings: (Frequency.DailyScheduleFrequency | None) = Field(default=None, alias='DailySettings')
    weekly_settings: (Frequency.WeeklyScheduleFrequency | None) = Field(default=None, alias='WeeklySettings')
    monthly_settings: (Frequency.MonthlyScheduleFrequency | None) = Field(default=None, alias='MonthlySettings')

class ScheduledScript(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    scheduled_script_id: (int | None) = Field(default=None, alias='ScheduledScriptId')
    script: (Script | None) = Field(default=None, alias='Script')
    schedule_target: (ScheduledScriptTarget | None) = Field(default=None, alias='ScheduleTarget')
    schedule: (ScriptScheduleSettings | None) = Field(default=None, alias='Schedule')
    limiting_search: (Searches.Search | None) = Field(default=None, alias='LimitingSearch')
    offline_action_flags: (ScheduledScriptOfflineActionFlags | None) = Field(default=None, alias='OfflineActionFlags')
    distribution_window: (ScheduledScripts.DistributionWindow | None) = Field(default=None, alias='DistributionWindow')
    parameters: (list[String_System.String] | None) = Field(default=None, alias='Parameters')
    use_agent_time: (bool | None) = Field(default=None, alias='UseAgentTime')
    scheduled_by: (str | None) = Field(default=None, alias='ScheduledBy')
    occurrences: (int | None) = Field(default=None, alias='Occurrences')
    start_date: (datetime | None) = Field(default=None, alias='StartDate')
    expire_date: (datetime | None) = Field(default=None, alias='ExpireDate')
    next_run_date: (datetime | None) = Field(default=None, alias='NextRunDate')
    is_disabled: (bool | None) = Field(default=None, alias='IsDisabled')
    priority: (int | None) = Field(default=None, alias='Priority')
    include_sub_groups: (bool | None) = Field(default=None, alias='IncludeSubGroups')
    is_inherited: (bool | None) = Field(default=None, alias='IsInherited')

class ScheduledScriptTarget(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    schedule_target_type: (ScheduledScripts.ScheduleTargetType | None) = Field(default=None, alias='ScheduleTargetType')
    group: (Groups.Group | None) = Field(default=None, alias='Group')
    client: (Clients.Client | None) = Field(default=None, alias='Client')
    location: (Clients.Location | None) = Field(default=None, alias='Location')
    computer: (Computers.Computer | None) = Field(default=None, alias='Computer')
    network_device: (NetworkDevices.NetworkDevice | None) = Field(default=None, alias='NetworkDevice')
    contact: (Clients.Contact | None) = Field(default=None, alias='Contact')

class ScriptReferences(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    schedule_count: (int | None) = Field(default=None, alias='ScheduleCount')
    internal_monitors: (list[Monitors.Monitor] | None) = Field(default=None, alias='InternalMonitors')
    remote_monitors: (list[Monitors.Monitor] | None) = Field(default=None, alias='RemoteMonitors')
    alert_templates: (list[Alerts.AlertTemplate] | None) = Field(default=None, alias='AlertTemplates')
from .ScheduledScripts import Frequency
from .. import Alerts, Clients, Computers, Groups, Monitors, NetworkDevices, Searches
from . import Functions, Settings, ScheduledScripts
from ......System.Collections.Generic.KeyValuePair_System import String_System
