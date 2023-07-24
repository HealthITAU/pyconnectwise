
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class AuthServiceCredentials(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    service_id: (int | None) = Field(default=None, alias='ServiceId')
    service_token: (str | None) = Field(default=None, alias='ServiceToken')

class APIAuthLinkInformation(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    nonce: (str | None) = Field(default=None, alias='Nonce')
