
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class String(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (str | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class Guid(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (UUID | None) = Field(default=None, alias='Id', example='00000000-0000-0000-0000-000000000000')
    name: (str | None) = Field(default=None, alias='Name')

class Int32(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')
from uuid import UUID
