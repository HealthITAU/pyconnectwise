
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class AgentStatistics(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    total_agents_purchased: (int | None) = Field(default=None, alias='TotalAgentsPurchased')
    total_agents_deployed: (int | None) = Field(default=None, alias='TotalAgentsDeployed')

class ScriptAutomationTimeResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    successful_scripts: (int | None) = Field(default=None, alias='SuccessfulScripts')
    automation_time_minutes: (int | None) = Field(default=None, alias='AutomationTimeMinutes')
    automation_value: (int | None) = Field(default=None, alias='AutomationValue')

class ScriptAutomationTimeUserResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    name: (str | None) = Field(default=None, alias='Name')
    successful_scripts: (int | None) = Field(default=None, alias='SuccessfulScripts')
    automation_time_minutes: (int | None) = Field(default=None, alias='AutomationTimeMinutes')
    automation_value: (int | None) = Field(default=None, alias='AutomationValue')

class GetComputerStatisticsRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    number_of_days: (int | None) = Field(default=None, alias='NumberOfDays')
    entity_ids: (list[int] | None) = Field(default=None, alias='EntityIds')
    entity_type: (str | None) = Field(default=None, alias='EntityType')

class GetScriptStatisticsResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    script_history_count: (int | None) = Field(default=None, alias='ScriptHistoryCount')
    script_pending_count: (int | None) = Field(default=None, alias='ScriptPendingCount')
    script_running_count: (int | None) = Field(default=None, alias='ScriptRunningCount')
    script_failure_count: (int | None) = Field(default=None, alias='ScriptFailureCount')
    script_success_count: (int | None) = Field(default=None, alias='ScriptSuccessCount')

class GetCommandStatisticsResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    command_pending_count: (int | None) = Field(default=None, alias='CommandPendingCount')
    command_failure_count: (int | None) = Field(default=None, alias='CommandFailureCount')

class IndividualScriptStatisticsResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    success_count: (int | None) = Field(default=None, alias='SuccessCount')
    total_run_count: (int | None) = Field(default=None, alias='TotalRunCount')
    last_run_target: (str | None) = Field(default=None, alias='LastRunTarget')
    last_run_date: (datetime | None) = Field(default=None, alias='LastRunDate')
    total_value: (int | None) = Field(default=None, alias='TotalValue')
    last_history_date_available: (datetime | None) = Field(default=None, alias='LastHistoryDateAvailable')
    last_run_status: (str | None) = Field(default=None, alias='LastRunStatus')

class ScriptAutomationTimeCategoryResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    total: (ScriptAutomationTimeResult | None) = Field(default=None, alias='Total')
    system: (ScriptAutomationTimeResult | None) = Field(default=None, alias='System')
    users: (ScriptAutomationTimeResult | None) = Field(default=None, alias='Users')
    maximum_history_days_available: (int | None) = Field(default=None, alias='MaximumHistoryDaysAvailable')

class ScriptAutomationTimeUserResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_list: (list[ScriptAutomationTimeUserResult] | None) = Field(default=None, alias='UserList')
    maximum_history_days_available: (int | None) = Field(default=None, alias='MaximumHistoryDaysAvailable')
