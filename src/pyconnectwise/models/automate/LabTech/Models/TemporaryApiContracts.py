
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class MaintenanceWindowDefinition(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    maintenance_window_definition_id: (int | None) = Field(default=None, alias='MaintenanceWindowDefinitionId')
    name: (str | None) = Field(default=None, alias='Name')
    comment: (str | None) = Field(default=None, alias='Comment')

class DeploymentLogin(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    deployment_login_id: (int | None) = Field(default=None, alias='DeploymentLoginId')
    title: (str | None) = Field(default=None, alias='Title')

class AgentDeploymentReadinessCheck(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    agent_deployment_readiness_check_id: (int | None) = Field(default=None, alias='AgentDeploymentReadinessCheckId')
    network_device_id: (int | None) = Field(default=None, alias='NetworkDeviceId')
    agent_deployment_readiness_check_status_id: (int | None) = Field(default=None, alias='AgentDeploymentReadinessCheckStatusId')
    readiness_check_status: (str | None) = Field(default=None, alias='ReadinessCheckStatus')
    deployment_attempt_count: (int | None) = Field(default=None, alias='DeploymentAttemptCount')
    date_last_checked_for_readiness: (datetime | None) = Field(default=None, alias='DateLastCheckedForReadiness')
    date_last_deployment_attempted: (datetime | None) = Field(default=None, alias='DateLastDeploymentAttempted')
