
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class WaitHandle(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    safe_wait_handle: (SafeHandles.SafeWaitHandle | None) = Field(default=None, alias='SafeWaitHandle')

class CancellationToken(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_cancellation_requested: (bool | None) = Field(default=None, alias='IsCancellationRequested')
    can_be_canceled: (bool | None) = Field(default=None, alias='CanBeCanceled')
    wait_handle: (WaitHandle | None) = Field(default=None, alias='WaitHandle')
from ..Microsoft.Win32 import SafeHandles
