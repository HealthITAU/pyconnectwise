
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class PatchesSummaryData(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    entity_id: (int | None) = Field(default=None, alias='EntityId')
    entity_name: (str | None) = Field(default=None, alias='EntityName')
    test_stage_failed_patches_count: (int | None) = Field(default=None, alias='TestStageFailedPatchesCount')
    test_stage_not_attempted_patches_count: (int | None) = Field(default=None, alias='TestStageNotAttemptedPatchesCount')
    test_stage_installed_patches_count: (int | None) = Field(default=None, alias='TestStageInstalledPatchesCount')
    pilot_stage_failed_patches_count: (int | None) = Field(default=None, alias='PilotStageFailedPatchesCount')
    pilot_stage_not_attempted_patches_count: (int | None) = Field(default=None, alias='PilotStageNotAttemptedPatchesCount')
    pilot_stage_installed_patches_count: (int | None) = Field(default=None, alias='PilotStageInstalledPatchesCount')
    production_stage_failed_patches_count: (int | None) = Field(default=None, alias='ProductionStageFailedPatchesCount')
    production_stage_not_attempted_patches_count: (int | None) = Field(default=None, alias='ProductionStageNotAttemptedPatchesCount')
    production_stage_installed_patches_count: (int | None) = Field(default=None, alias='ProductionStageInstalledPatchesCount')

class PatchStage(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class PatchManagerDevice(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    computer_id: (int | None) = Field(default=None, alias='ComputerId')
    computer_name: (str | None) = Field(default=None, alias='ComputerName')
    stage: (PatchStage | None) = Field(default=None, alias='Stage')
    operating_system_name: (str | None) = Field(default=None, alias='OperatingSystemName')
    normalized_operating_system_name: (str | None) = Field(default=None, alias='NormalizedOperatingSystemName')
    company: (Models.Client | None) = Field(default=None, alias='Company')
    site: (Models.Location | None) = Field(default=None, alias='Site')
    last_microsoft_window: (datetime | None) = Field(default=None, alias='LastMicrosoftWindow')
    last_third_party_window: (datetime | None) = Field(default=None, alias='LastThirdPartyWindow')
    next_microsoft_window: (datetime | None) = Field(default=None, alias='NextMicrosoftWindow')
    next_third_party_window: (datetime | None) = Field(default=None, alias='NextThirdPartyWindow')
    did_last_patch_job_fail: (bool | None) = Field(default=None, alias='DidLastPatchJobFail')
    is_daytime_patching_enabled: (bool | None) = Field(default=None, alias='IsDaytimePatchingEnabled')
    is_missing_baseline: (bool | None) = Field(default=None, alias='IsMissingBaseline')
    is_missing_patch_inventory: (bool | None) = Field(default=None, alias='IsMissingPatchInventory')
    is_patch_job_running: (bool | None) = Field(default=None, alias='IsPatchJobRunning')
    is_pending_update: (bool | None) = Field(default=None, alias='IsPendingUpdate')
    is_reboot_pending: (bool | None) = Field(default=None, alias='IsRebootPending')
    is_wsus_enabled: (bool | None) = Field(default=None, alias='IsWsusEnabled')
    is_wua_out_of_date: (bool | None) = Field(default=None, alias='IsWuaOutOfDate')
    missing_patch_count: (int | None) = Field(default=None, alias='MissingPatchCount')
    microsoft_compliance_percent: (float | None) = Field(default=None, alias='MicrosoftCompliancePercent')
    third_party_compliance_percent: (float | None) = Field(default=None, alias='ThirdPartyCompliancePercent')
    has_approved_patches: (bool | None) = Field(default=None, alias='HasApprovedPatches')
    has_approved_microsoft_patches: (bool | None) = Field(default=None, alias='HasApprovedMicrosoftPatches')
    has_approved_third_party_patches: (bool | None) = Field(default=None, alias='HasApprovedThirdPartyPatches')
    release_id: (int | None) = Field(default=None, alias='ReleaseId')
from ..... import Models
