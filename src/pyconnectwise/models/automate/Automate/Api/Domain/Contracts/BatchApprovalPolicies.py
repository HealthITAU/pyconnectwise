
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class WindowsApprovalPolicyPatch(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    approval_action_id: (int | None) = Field(default=None, alias='ApprovalActionId')
    hotfix_id: (UUID | None) = Field(default=None, alias='HotfixId', example='00000000-0000-0000-0000-000000000000')
    operating_system: (str | None) = Field(default=None, alias='OperatingSystem')

class ApprovalPolicyThirdPartyPatchSetting(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    patch_approval: (int | None) = Field(default=None, alias='PatchApproval')
    lt_product_key: (UUID | None) = Field(default=None, alias='LTProductKey', example='00000000-0000-0000-0000-000000000000')
    version: (str | None) = Field(default=None, alias='Version')

class WindowsApprovalPolicyPatchBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    patch_policies: (list[WindowsApprovalPolicyPatch] | None) = Field(default=None, alias='PatchPolicies')

class ApprovalPolicyThirdPartyPatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    patch_policies: (list[ApprovalPolicyThirdPartyPatchSetting] | None) = Field(default=None, alias='PatchPolicies')
from uuid import UUID
