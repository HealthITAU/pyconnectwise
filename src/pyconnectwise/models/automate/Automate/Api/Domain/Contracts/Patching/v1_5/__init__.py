
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class PatchingPolicyScript(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    run_script: (bool | None) = Field(default=None, alias='RunScript')
    script_guid: (UUID | None) = Field(default=None, alias='ScriptGuid', example='00000000-0000-0000-0000-000000000000')
    script_name: (str | None) = Field(default=None, alias='ScriptName')
    cancel_action_on_script_failure: (bool | None) = Field(default=None, alias='CancelActionOnScriptFailure')

class PatchingGroup(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    group_id: (int | None) = Field(default=None, alias='GroupId')
    group_name: (str | None) = Field(default=None, alias='GroupName')

class PatchingPolicyScriptOptions(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    before_script_options: (PatchingPolicyScript | None) = Field(default=None, alias='BeforeScriptOptions')
    after_script_options: (PatchingPolicyScript | None) = Field(default=None, alias='AfterScriptOptions')
from uuid import UUID
