
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class DeleteRemoteMonitorsBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    group_id: (int | None) = Field(default=None, alias='GroupId')
    remote_monitor_ids: (list[int] | None) = Field(default=None, alias='RemoteMonitorIds')

class DeleteRemoteMonitorBatchResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    remote_monitor_id: (int | None) = Field(default=None, alias='RemoteMonitorId')
    result_details: (ResponseResult | None) = Field(default=None, alias='ResultDetails')

class DeleteRemoteMonitorBatchResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    remote_monitor_results: (list[DeleteRemoteMonitorBatchResult] | None) = Field(default=None, alias='RemoteMonitorResults')
    contains_unsuccessful_results: (bool | None) = Field(default=None, alias='ContainsUnsuccessfulResults')
from . import ResponseResult
