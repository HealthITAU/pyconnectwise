
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class UserAuthLinkStatus(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    service_id: (int | None) = Field(default=None, alias='ServiceId')
    is_sso_enabled: (bool | None) = Field(default=None, alias='IsSsoEnabled')
    is_local_login_enabled: (bool | None) = Field(default=None, alias='IsLocalLoginEnabled')
    is_eligible_for_sso: (bool | None) = Field(default=None, alias='IsEligibleForSso')
    is_account_linked: (bool | None) = Field(default=None, alias='IsAccountLinked')
