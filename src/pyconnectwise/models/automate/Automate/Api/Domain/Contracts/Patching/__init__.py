
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class WindowsUpdateCategory(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    category_id: (int | None) = Field(default=None, alias='CategoryId')
    category_name: (str | None) = Field(default=None, alias='CategoryName')

class ApprovalPolicyStats(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    approval_policy_id: (int | None) = Field(default=None, alias='ApprovalPolicyId')
    approval_policy_name: (str | None) = Field(default=None, alias='ApprovalPolicyName')
    pending_approval_count: (int | None) = Field(default=None, alias='PendingApprovalCount')

class ComputerPatchingStats(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    computer_id: (int | None) = Field(default=None, alias='ComputerId')
    overall_compliance: (float | None) = Field(default=None, alias='OverallCompliance')
    installed_patch_count: (int | None) = Field(default=None, alias='InstalledPatchCount')
    missing_patch_count: (int | None) = Field(default=None, alias='MissingPatchCount')
    failed_patch_count: (int | None) = Field(default=None, alias='FailedPatchCount')
    compliant_software_count: (int | None) = Field(default=None, alias='CompliantSoftwareCount')
    non_compliant_software_count: (int | None) = Field(default=None, alias='NonCompliantSoftwareCount')
    failed_software_count: (int | None) = Field(default=None, alias='FailedSoftwareCount')
    incorrect_software_count: (int | None) = Field(default=None, alias='IncorrectSoftwareCount')
    stage: (str | None) = Field(default=None, alias='Stage')
    no_patch_inventory: (bool | None) = Field(default=None, alias='NoPatchInventory')
    wsus_enabled: (bool | None) = Field(default=None, alias='WSUSEnabled')
    patch_job_running: (bool | None) = Field(default=None, alias='PatchJobRunning')
    daytime_patching_enabled: (bool | None) = Field(default=None, alias='DaytimePatchingEnabled')
    wua_out_of_date: (bool | None) = Field(default=None, alias='WUAOutOfDate')
    missing_baseline_patches: (bool | None) = Field(default=None, alias='MissingBaselinePatches')
    wua_version: (str | None) = Field(default=None, alias='WUAVersion')
    last_install_window: (datetime | None) = Field(default=None, alias='LastInstallWindow')
    next_install_window: (datetime | None) = Field(default=None, alias='NextInstallWindow')
    last_software_window: (datetime | None) = Field(default=None, alias='LastSoftwareWindow')
    next_software_window: (datetime | None) = Field(default=None, alias='NextSoftwareWindow')
    last_patched_date: (datetime | None) = Field(default=None, alias='LastPatchedDate')
    last_microsoft_patched_date: (datetime | None) = Field(default=None, alias='LastMicrosoftPatchedDate')
    last_third_party_patched_date: (datetime | None) = Field(default=None, alias='LastThirdPartyPatchedDate')
    last_patch_inventory: (datetime | None) = Field(default=None, alias='LastPatchInventory')
    is_microsoft_managed: (bool | None) = Field(default=None, alias='IsMicrosoftManaged')
    is_third_party_managed: (bool | None) = Field(default=None, alias='IsThirdPartyManaged')

class DevicesSummaryData(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    compliance_score: (float | None) = Field(default=None, alias='ComplianceScore')
    devices_affecting_compliance_count: (int | None) = Field(default=None, alias='DevicesAffectingComplianceCount')
    devices_affecting_pilot_stage_compliance_count: (int | None) = Field(default=None, alias='DevicesAffectingPilotStageComplianceCount')
    devices_affecting_production_stage_compliance_count: (int | None) = Field(default=None, alias='DevicesAffectingProductionStageComplianceCount')
    devices_affecting_test_stage_compliance_count: (int | None) = Field(default=None, alias='DevicesAffectingTestStageComplianceCount')
    devices_needing_attention_count: (int | None) = Field(default=None, alias='DevicesNeedingAttentionCount')
    enabled_wsus_count: (int | None) = Field(default=None, alias='EnabledWsusCount')
    entity_id: (int | None) = Field(default=None, alias='EntityId')
    entity_name: (str | None) = Field(default=None, alias='EntityName')
    in_daytime_patching_count: (int | None) = Field(default=None, alias='InDaytimePatchingCount')
    last_patch_job_failed_count: (int | None) = Field(default=None, alias='LastPatchJobFailedCount')
    missing_baseline_patches_count: (int | None) = Field(default=None, alias='MissingBaselinePatchesCount')
    missing_patch_inventory_count: (int | None) = Field(default=None, alias='MissingPatchInventoryCount')
    out_of_date_wua_count: (int | None) = Field(default=None, alias='OutOfDateWuaCount')
    pending_reboot_count: (int | None) = Field(default=None, alias='PendingRebootCount')
    pending_update_count: (int | None) = Field(default=None, alias='PendingUpdateCount')
    pilot_stage_compliance_score: (float | None) = Field(default=None, alias='PilotStageComplianceScore')
    production_stage_compliance_score: (float | None) = Field(default=None, alias='ProductionStageComplianceScore')
    running_patch_installation_count: (int | None) = Field(default=None, alias='RunningPatchInstallationCount')
    servers_affecting_compliance_count: (int | None) = Field(default=None, alias='ServersAffectingComplianceCount')
    servers_compliance_score: (float | None) = Field(default=None, alias='ServersComplianceScore')
    test_stage_compliance_score: (float | None) = Field(default=None, alias='TestStageComplianceScore')
    workstations_affecting_compliance_count: (int | None) = Field(default=None, alias='WorkstationsAffectingComplianceCount')
    workstations_compliance_score: (float | None) = Field(default=None, alias='WorkstationsComplianceScore')

class WindowsUpdateAgentMode(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class Windows10UpdatePolicySettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    service_branch: (str | None) = Field(default=None, alias='ServiceBranch')
    feature_update_deferment: (int | None) = Field(default=None, alias='FeatureUpdateDeferment')
    quality_update_deferment: (int | None) = Field(default=None, alias='QualityUpdateDeferment')

class UpdatePolicyScheduleDay(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class PatchRebootAction(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class PatchRebootMode(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class PolicyScheduleType(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class DatesScheduleSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    monthly_occurence: (list[str] | None) = Field(default=None, alias='MonthlyOccurence')
    dates: (list[int] | None) = Field(default=None, alias='Dates')
    last_day_of_month: (bool | None) = Field(default=None, alias='LastDayOfMonth')

class DaysScheduleSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    monthly_occurence: (list[str] | None) = Field(default=None, alias='MonthlyOccurence')
    weekly_occurence: (list[str] | None) = Field(default=None, alias='WeeklyOccurence')
    daily_occurence: (list[str] | None) = Field(default=None, alias='DailyOccurence')

class PatchingPolicyScript(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_guid: (UUID | None) = Field(default=None, alias='ScriptGuid', example='00000000-0000-0000-0000-000000000000')
    script_name: (str | None) = Field(default=None, alias='ScriptName')

class NonCompliantSummaryData(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    low_severity_count: (int | None) = Field(default=None, alias='LowSeverityCount')
    moderate_severity_count: (int | None) = Field(default=None, alias='ModerateSeverityCount')
    important_severity_count: (int | None) = Field(default=None, alias='ImportantSeverityCount')
    critical_severity_count: (int | None) = Field(default=None, alias='CriticalSeverityCount')
    unspecified_severity_count: (int | None) = Field(default=None, alias='UnspecifiedSeverityCount')
    low_cvss_count: (int | None) = Field(default=None, alias='LowCvssCount')
    medium_cvss_count: (int | None) = Field(default=None, alias='MediumCvssCount')
    high_cvss_count: (int | None) = Field(default=None, alias='HighCvssCount')
    total_non_compliant_count: (int | None) = Field(default=None, alias='TotalNonCompliantCount')

class ThirdPartyPatchesSummaryData(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    third_party_compliance_score: (float | None) = Field(default=None, alias='ThirdPartyComplianceScore')
    third_party_server_compliance_score: (float | None) = Field(default=None, alias='ThirdPartyServerComplianceScore')
    third_party_workstation_compliance_score: (float | None) = Field(default=None, alias='ThirdPartyWorkstationComplianceScore')
    devices_affecting_compliance_count: (int | None) = Field(default=None, alias='DevicesAffectingComplianceCount')
    servers_affecting_compliance_count: (int | None) = Field(default=None, alias='ServersAffectingComplianceCount')
    workstations_affecting_compliance_count: (int | None) = Field(default=None, alias='WorkstationsAffectingComplianceCount')
    approved_count: (int | None) = Field(default=None, alias='ApprovedCount')
    compliant_count: (int | None) = Field(default=None, alias='CompliantCount')
    failed_count: (int | None) = Field(default=None, alias='FailedCount')
    incorrect_version_count: (int | None) = Field(default=None, alias='IncorrectVersionCount')
    non_compliant_count: (int | None) = Field(default=None, alias='NonCompliantCount')
    not_attempted_count: (int | None) = Field(default=None, alias='NotAttemptedCount')

class ThirdPartyPatchVersion(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    lt_product_key: (UUID | None) = Field(default=None, alias='LTProductKey', example='00000000-0000-0000-0000-000000000000')
    versions: (list[str] | None) = Field(default=None, alias='Versions')

class WindowsReleaseStats(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    release_id: (int | None) = Field(default=None, alias='ReleaseId')
    release_count: (int | None) = Field(default=None, alias='ReleaseCount')

class AutomaticApprovalSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    cvss_lower_bound: (int | None) = Field(default=None, alias='CvssLowerBound')
    severities: (list[str] | None) = Field(default=None, alias='Severities')
    categories: (list[WindowsUpdateCategory] | None) = Field(default=None, alias='Categories')
    titles: (list[str] | None) = Field(default=None, alias='Titles')

class AutomaticPolicySettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    severities: (list[str] | None) = Field(default=None, alias='Severities')
    categories: (list[WindowsUpdateCategory] | None) = Field(default=None, alias='Categories')
    titles: (list[str] | None) = Field(default=None, alias='Titles')

class RebootPolicy(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    minutes_after_install_to_reboot: (int | None) = Field(default=None, alias='MinutesAfterInstallToReboot')
    name: (str | None) = Field(default=None, alias='Name')
    reboot_action: (PatchRebootAction | None) = Field(default=None, alias='RebootAction')
    reboot_mode: (PatchRebootMode | None) = Field(default=None, alias='RebootMode')
    reboot_prior_to_first_patch_install: (bool | None) = Field(default=None, alias='RebootPriorToFirstPatchInstall')
    set_maintenance_window_for_reboot: (bool | None) = Field(default=None, alias='SetMaintenanceWindowForReboot')

class ThirdPartyUpdatePolicy(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    create_restore_point: (bool | None) = Field(default=None, alias='CreateRestorePoint')
    daytime_patching: (bool | None) = Field(default=None, alias='DaytimePatching')
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')
    schedule_day: (UpdatePolicyScheduleDay | None) = Field(default=None, alias='ScheduleDay')
    schedule_start_hour: (str | None) = Field(default=None, alias='ScheduleStartHour')
    schedule_time_span: (str | None) = Field(default=None, alias='ScheduleTimeSpan')
    wake_system: (bool | None) = Field(default=None, alias='WakeSystem')

class PatchingPolicySchedule(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    start_time: (int | None) = Field(default=None, alias='StartTime')
    duration: (str | None) = Field(default=None, alias='Duration')
    policy_schedule_type: (PolicyScheduleType | None) = Field(default=None, alias='PolicyScheduleType')
    dates_schedule_settings: (DatesScheduleSettings | None) = Field(default=None, alias='DatesScheduleSettings')
    days_schedule_settings: (DaysScheduleSettings | None) = Field(default=None, alias='DaysScheduleSettings')

class PatchingPolicyScriptOptions(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    before_script: (PatchingPolicyScript | None) = Field(default=None, alias='BeforeScript')
    after_script: (PatchingPolicyScript | None) = Field(default=None, alias='AfterScript')
    cancel_action_on_before_script_failure: (bool | None) = Field(default=None, alias='CancelActionOnBeforeScriptFailure')

class WindowsServiceBranchStats(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    server_release_counts: (list[WindowsReleaseStats] | None) = Field(default=None, alias='ServerReleaseCounts')
    server_no_channel_count: (int | None) = Field(default=None, alias='ServerNoChannelCount')
    server_semi_annual_channel_count: (int | None) = Field(default=None, alias='ServerSemiAnnualChannelCount')
    server_semi_annual_channel_targeted_count: (int | None) = Field(default=None, alias='ServerSemiAnnualChannelTargetedCount')
    workstation_release_counts: (list[WindowsReleaseStats] | None) = Field(default=None, alias='WorkstationReleaseCounts')
    workstation_no_channel_count: (int | None) = Field(default=None, alias='WorkstationNoChannelCount')
    workstation_semi_annual_channel_count: (int | None) = Field(default=None, alias='WorkstationSemiAnnualChannelCount')
    workstation_semi_annual_channel_targeted_count: (int | None) = Field(default=None, alias='WorkstationSemiAnnualChannelTargetedCount')

class ApprovalPolicy(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')
    is_default_policy: (bool | None) = Field(default=None, alias='IsDefaultPolicy')
    has_staging: (bool | None) = Field(default=None, alias='HasStaging')
    test_duration: (int | None) = Field(default=None, alias='TestDuration')
    pilot_duration: (int | None) = Field(default=None, alias='PilotDuration')
    automatic_approval_settings: (AutomaticApprovalSettings | None) = Field(default=None, alias='AutomaticApprovalSettings')
    automatic_ignore_settings: (AutomaticPolicySettings | None) = Field(default=None, alias='AutomaticIgnoreSettings')
    automatic_deny_settings: (AutomaticPolicySettings | None) = Field(default=None, alias='AutomaticDenySettings')

class MicrosoftUpdatePolicy(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')
    update_mode: (WindowsUpdateAgentMode | None) = Field(default=None, alias='UpdateMode')
    create_restore_point: (bool | None) = Field(default=None, alias='CreateRestorePoint')
    daytime_patching: (bool | None) = Field(default=None, alias='DaytimePatching')
    daytime_patching_minimum_uptime: (int | None) = Field(default=None, alias='DaytimePatchingMinimumUptime')
    install_missing_baseline_patches: (bool | None) = Field(default=None, alias='InstallMissingBaselinePatches')
    wake_system: (bool | None) = Field(default=None, alias='WakeSystem')
    patching_policy_schedule: (PatchingPolicySchedule | None) = Field(default=None, alias='PatchingPolicySchedule')
    windows10_update_policy_settings: (Windows10UpdatePolicySettings | None) = Field(default=None, alias='Windows10UpdatePolicySettings')
    patching_policy_script_options: (PatchingPolicyScriptOptions | None) = Field(default=None, alias='PatchingPolicyScriptOptions')
    schedule_day: (UpdatePolicyScheduleDay | None) = Field(default=None, alias='ScheduleDay')
    schedule_start_hour: (str | None) = Field(default=None, alias='ScheduleStartHour')
    schedule_time_span: (str | None) = Field(default=None, alias='ScheduleTimeSpan')

class LocalOverridePolicy(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    approval_policies: (list[ApprovalPolicy] | None) = Field(default=None, alias='ApprovalPolicies')
    computer_id: (int | None) = Field(default=None, alias='ComputerId')
    microsoft_update_policy: (MicrosoftUpdatePolicy | None) = Field(default=None, alias='MicrosoftUpdatePolicy')
    reboot_policy: (RebootPolicy | None) = Field(default=None, alias='RebootPolicy')
    third_party_update_policy: (ThirdPartyUpdatePolicy | None) = Field(default=None, alias='ThirdPartyUpdatePolicy')

class GroupPatchingPolicy(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    approval_policies: (list[ApprovalPolicy] | None) = Field(default=None, alias='ApprovalPolicies')
    group_id: (int | None) = Field(default=None, alias='GroupId')
    group_name: (str | None) = Field(default=None, alias='GroupName')
    is_manual: (bool | None) = Field(default=None, alias='IsManual')
    is_patching_group: (bool | None) = Field(default=None, alias='IsPatchingGroup')
    microsoft_update_policy: (MicrosoftUpdatePolicy | None) = Field(default=None, alias='MicrosoftUpdatePolicy')
    priority: (int | None) = Field(default=None, alias='Priority')
    reboot_policy: (RebootPolicy | None) = Field(default=None, alias='RebootPolicy')
    third_party_update_policy: (ThirdPartyUpdatePolicy | None) = Field(default=None, alias='ThirdPartyUpdatePolicy')
    auto_join_settings: (Groups.GroupAutoJoinSettings | None) = Field(default=None, alias='AutoJoinSettings')
    windows_computer_count: (int | None) = Field(default=None, alias='WindowsComputerCount')
from .. import Groups
from uuid import UUID
