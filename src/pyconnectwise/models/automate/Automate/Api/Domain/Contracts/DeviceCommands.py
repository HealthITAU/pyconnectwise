
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class ExecuteDeviceCommandsRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    device_id_list: (list[int] | None) = Field(default=None, alias='DeviceIdList')

class ExecuteDeviceCommandResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    device_id: (int | None) = Field(default=None, alias='DeviceId')
    result_details: (ResponseResult | None) = Field(default=None, alias='ResultDetails')

class ExecuteDeviceCommandResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    command_result_list: (list[ExecuteDeviceCommandResult] | None) = Field(default=None, alias='CommandResultList')
    contains_unsuccessful_results: (bool | None) = Field(default=None, alias='ContainsUnsuccessfulResults')
from . import ResponseResult
