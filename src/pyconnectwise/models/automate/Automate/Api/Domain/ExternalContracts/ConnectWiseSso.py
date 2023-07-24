
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class SsoUser(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    partner_id: (str | None) = Field(default=None, alias='PartnerId')
    id: (str | None) = Field(default=None, alias='Id')
    user_name: (str | None) = Field(default=None, alias='UserName')
    email: (str | None) = Field(default=None, alias='Email')
    first_name: (str | None) = Field(default=None, alias='FirstName')
    last_name: (str | None) = Field(default=None, alias='LastName')
    login_scheme: (str | None) = Field(default=None, alias='LoginScheme')
    email_confirmed: (bool | None) = Field(default=None, alias='EmailConfirmed')
    is_disabled: (bool | None) = Field(default=None, alias='IsDisabled')
    created: (int | None) = Field(default=None, alias='Created')
    updated: (int | None) = Field(default=None, alias='Updated')
