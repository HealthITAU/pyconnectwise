
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class WindowsUpdateAgentSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    use_windows_update_agent_mode: (bool | None) = Field(default=None, alias='UseWindowsUpdateAgentMode')
    mode: (str | None) = Field(default=None, alias='Mode')
    disable_user_interface: (bool | None) = Field(default=None, alias='DisableUserInterface')

class MicrosoftUpdatePolicyOptions(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    install_missing_baseline_patches: (bool | None) = Field(default=None, alias='InstallMissingBaselinePatches')

class DaytimePatchingOptions(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    allow_daytime_patching: (bool | None) = Field(default=None, alias='AllowDaytimePatching')
    require_minimum_uptime: (bool | None) = Field(default=None, alias='RequireMinimumUptime')
    minimum_uptime: (str | None) = Field(default=None, alias='MinimumUptime')
    update_only: (bool | None) = Field(default=None, alias='UpdateOnly')
    prompt_interval: (str | None) = Field(default=None, alias='PromptInterval')
    prompt_deadline: (int | None) = Field(default=None, alias='PromptDeadline')
    prompt_message: (str | None) = Field(default=None, alias='PromptMessage')

class ServiceBranchSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    use_service_branch: (bool | None) = Field(default=None, alias='UseServiceBranch')
    is_targeted: (bool | None) = Field(default=None, alias='IsTargeted')

class UpdateDefermentSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    use_deferment: (bool | None) = Field(default=None, alias='UseDeferment')
    deferment_period_days: (int | None) = Field(default=None, alias='DefermentPeriodDays')

class PatchingPolicyWorkstationOptions(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    send_wake_on_lan_packet: (bool | None) = Field(default=None, alias='SendWakeOnLanPacket')
    create_windows_restore_point: (bool | None) = Field(default=None, alias='CreateWindowsRestorePoint')
    daytime_patching_options: (DaytimePatchingOptions | None) = Field(default=None, alias='DaytimePatchingOptions')

class MicrosoftUpdatePolicyWindows10Options(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    service_branch_settings: (ServiceBranchSettings | None) = Field(default=None, alias='ServiceBranchSettings')
    feature_update_deferment_settings: (UpdateDefermentSettings | None) = Field(default=None, alias='FeatureUpdateDefermentSettings')
    quality_update_deferment_settings: (UpdateDefermentSettings | None) = Field(default=None, alias='QualityUpdateDefermentSettings')

class ThirdPartyUpdatePolicy(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    policy_id: (int | None) = Field(default=None, alias='PolicyId')
    policy_name: (str | None) = Field(default=None, alias='PolicyName')
    patching_policy_schedule: (Schedule.PatchingPolicySchedule | None) = Field(default=None, alias='PatchingPolicySchedule')
    workstation_options: (PatchingPolicyWorkstationOptions | None) = Field(default=None, alias='WorkstationOptions')
    script_options: (PatchingPolicyScriptOptions | None) = Field(default=None, alias='ScriptOptions')

class MicrosoftUpdatePolicy(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    policy_id: (int | None) = Field(default=None, alias='PolicyId')
    policy_name: (str | None) = Field(default=None, alias='PolicyName')
    schedule_settings: (Schedule.PatchingPolicySchedule | None) = Field(default=None, alias='ScheduleSettings')
    windows_update_agent_settings: (WindowsUpdateAgentSettings | None) = Field(default=None, alias='WindowsUpdateAgentSettings')
    policy_options: (MicrosoftUpdatePolicyOptions | None) = Field(default=None, alias='PolicyOptions')
    workstation_options: (PatchingPolicyWorkstationOptions | None) = Field(default=None, alias='WorkstationOptions')
    windows10_update_options: (MicrosoftUpdatePolicyWindows10Options | None) = Field(default=None, alias='Windows10UpdateOptions')
    script_options: (PatchingPolicyScriptOptions | None) = Field(default=None, alias='ScriptOptions')
from . import PatchingPolicyScriptOptions, Schedule
