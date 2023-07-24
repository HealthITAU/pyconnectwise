
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class RegisterSsoRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    registration_token: (str | None) = Field(default=None, alias='RegistrationToken')
    enabled_user_folders: (list[int] | None) = Field(default=None, alias='EnabledUserFolders')

class UnregisterSsoRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    client_id: (str | None) = Field(default=None, alias='ClientId')

class LinkToSsoRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    service_identifier: (str | None) = Field(default=None, alias='ServiceIdentifier')
