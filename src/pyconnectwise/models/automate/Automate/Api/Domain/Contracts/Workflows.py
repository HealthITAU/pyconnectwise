
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class WorkflowStep(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    workflow_step_id: (int | None) = Field(default=None, alias='WorkflowStepId')
    description: (str | None) = Field(default=None, alias='Description')
    is_required: (bool | None) = Field(default=None, alias='IsRequired')
    prerequisite_id: (int | None) = Field(default=None, alias='PrerequisiteId')

class WorkflowStatus(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    workflow_status_id: (int | None) = Field(default=None, alias='WorkflowStatusId')
    description: (str | None) = Field(default=None, alias='Description')

class WorkflowMetadata(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    system_workflow_progress_metadata_id: (int | None) = Field(default=None, alias='SystemWorkflowProgressMetadataId')
    metadata_key: (str | None) = Field(default=None, alias='MetadataKey')
    metadata_value: (str | None) = Field(default=None, alias='MetadataValue')

class SystemWorkflowProgressEntry(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    system_workflow_progress_id: (int | None) = Field(default=None, alias='SystemWorkflowProgressId')
    description: (str | None) = Field(default=None, alias='Description')
    workflow_step: (WorkflowStep | None) = Field(default=None, alias='WorkflowStep')
    workflow_status: (WorkflowStatus | None) = Field(default=None, alias='WorkflowStatus')
    workflow_metadata: (list[WorkflowMetadata] | None) = Field(default=None, alias='WorkflowMetadata')
