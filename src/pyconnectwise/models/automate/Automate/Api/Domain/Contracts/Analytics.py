
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class RecordedActionType(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    recorded_action_type_id: (int | None) = Field(default=None, alias='RecordedActionTypeId')

class RecordedActionSource(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    recorded_action_source_id: (int | None) = Field(default=None, alias='RecordedActionSourceId')

class RecordedAction(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    type: (RecordedActionType | None) = Field(default=None, alias='Type')
    object_id: (int | None) = Field(default=None, alias='ObjectId')
    secondary_identifier: (str | None) = Field(default=None, alias='SecondaryIdentifier')
    description: (str | None) = Field(default=None, alias='Description')
    source: (RecordedActionSource | None) = Field(default=None, alias='Source')
