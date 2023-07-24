
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class DisableServerPatchRebootWorkstationSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    prompt_message: (str | None) = Field(default=None, alias='PromptMessage')
    prompt_interval: (str | None) = Field(default=None, alias='PromptInterval')
    reboot_deadline: (str | None) = Field(default=None, alias='RebootDeadline')
    reboot_deadline_prompt_message: (str | None) = Field(default=None, alias='RebootDeadlinePromptMessage')
    reboot_deadline_prompt_duration: (str | None) = Field(default=None, alias='RebootDeadlinePromptDuration')
    send_wake_on_lan_packet: (bool | None) = Field(default=None, alias='SendWakeOnLanPacket')
    reboot_if_no_user_logged_in: (bool | None) = Field(default=None, alias='RebootIfNoUserLoggedIn')

class PostPatchInstallTriggerSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    limit_to_microsoft_update_policy_window: (bool | None) = Field(default=None, alias='LimitToMicrosoftUpdatePolicyWindow')
    window_extension: (str | None) = Field(default=None, alias='WindowExtension')

class RebootPolicyPromptSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    use_prompt: (bool | None) = Field(default=None, alias='UsePrompt')
    requires_confirmation: (bool | None) = Field(default=None, alias='RequiresConfirmation')
    reboot_if_no_user_logged_on: (bool | None) = Field(default=None, alias='RebootIfNoUserLoggedOn')

class RebootPolicyMaintenanceModeOptions(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    set_window: (bool | None) = Field(default=None, alias='SetWindow')
    window_ignore_types: (list[str] | None) = Field(default=None, alias='WindowIgnoreTypes')
    window_duration: (str | None) = Field(default=None, alias='WindowDuration')

class PromptWithoutDeadlineSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    reboot_trigger_type: (str | None) = Field(default=None, alias='RebootTriggerType')
    post_patch_install_trigger_settings: (PostPatchInstallTriggerSettings | None) = Field(default=None, alias='PostPatchInstallTriggerSettings')
    schedule_trigger_settings: (Schedule.PatchingPolicySchedule | None) = Field(default=None, alias='ScheduleTriggerSettings')
    prompt_settings: (RebootPolicyPromptSettings | None) = Field(default=None, alias='PromptSettings')
    reboot_prior_to_patch_job_installs: (bool | None) = Field(default=None, alias='RebootPriorToPatchJobInstalls')
    maintenance_mode_options: (RebootPolicyMaintenanceModeOptions | None) = Field(default=None, alias='MaintenanceModeOptions')
    script_options: (PatchingPolicyScriptOptions | None) = Field(default=None, alias='ScriptOptions')

class DisableServerPatchRebootServerSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    alert_template: (AlertTemplates.AlertTemplate | None) = Field(default=None, alias='AlertTemplate')
    alert_message: (str | None) = Field(default=None, alias='AlertMessage')
    ticket_category: (Ticketing.TicketCategory | None) = Field(default=None, alias='TicketCategory')
    report_category: (Reporting.ReportCategory | None) = Field(default=None, alias='ReportCategory')

class DisableServerPatchRebootSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    server_settings: (DisableServerPatchRebootServerSettings | None) = Field(default=None, alias='ServerSettings')
    workstation_settings: (DisableServerPatchRebootWorkstationSettings | None) = Field(default=None, alias='WorkstationSettings')

class RebootPolicy(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    policy_id: (int | None) = Field(default=None, alias='PolicyId')
    policy_name: (str | None) = Field(default=None, alias='PolicyName')
    reboot_policy_type: (str | None) = Field(default=None, alias='RebootPolicyType')
    disable_server_patch_reboot_settings: (DisableServerPatchRebootSettings | None) = Field(default=None, alias='DisableServerPatchRebootSettings')
    prompt_without_deadline_settings: (PromptWithoutDeadlineSettings | None) = Field(default=None, alias='PromptWithoutDeadlineSettings')
from . import PatchingPolicyScriptOptions, Schedule
from ... import AlertTemplates, Reporting, Ticketing
