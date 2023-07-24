
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class ProbeCommandHistoryEntry(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    result_set: (list[Contracts.ProbeCommandHistoryEntry] | None) = Field(default=None, alias='ResultSet')
    total_record_count: (int | None) = Field(default=None, alias='TotalRecordCount')
from ......Automate.Api.Domain import Contracts
