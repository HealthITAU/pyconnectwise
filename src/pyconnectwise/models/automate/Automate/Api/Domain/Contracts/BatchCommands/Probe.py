
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class ExecuteProbeBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    probe_ids: (list[int] | None) = Field(default=None, alias='ProbeIds')

class ExecuteProbeCommandResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    probe_id: (int | None) = Field(default=None, alias='ProbeId')
    result_details: (ResponseResult | None) = Field(default=None, alias='ResultDetails')

class ExecuteToggleProbeCommandBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    computer_ids: (list[int] | None) = Field(default=None, alias='ComputerIds')
    enable_probe: (bool | None) = Field(default=None, alias='EnableProbe')

class ExecuteProbeBatchResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    probe_command_results: (list[ExecuteProbeCommandResult] | None) = Field(default=None, alias='ProbeCommandResults')
    contains_unsuccessful_results: (bool | None) = Field(default=None, alias='ContainsUnsuccessfulResults')
from .. import ResponseResult
