
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class ComputerServiceItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (str | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class ComputerProcessItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (str | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class ServerFileItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (str | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')
    relative_path: (str | None) = Field(default=None, alias='RelativePath')
