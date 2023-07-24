
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class AuthService(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    service_id: (int | None) = Field(default=None, alias='ServiceId')
    service_name: (str | None) = Field(default=None, alias='ServiceName')
    service_uri: (str | None) = Field(default=None, alias='ServiceURI')
    service_type: (int | None) = Field(default=None, alias='ServiceType')
    client_id: (str | None) = Field(default=None, alias='ClientId')
    is_default: (bool | None) = Field(default=None, alias='IsDefault')
    is_automatic: (bool | None) = Field(default=None, alias='IsAutomatic')
    service_guid: (str | None) = Field(default=None, alias='ServiceGuid')
    is_enabled: (bool | None) = Field(default=None, alias='IsEnabled')
    is_local_login_enabled: (bool | None) = Field(default=None, alias='IsLocalLoginEnabled')
    authentication_type: (int | None) = Field(default=None, alias='AuthenticationType')

class TokenCredentials(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    username: (str | None) = Field(default=None, alias='Username')
    password: (str | None) = Field(default=None, alias='Password')
    two_factor_passcode: (str | None) = Field(default=None, alias='TwoFactorPasscode')

class TokenResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    access_token: (str | None) = Field(default=None, alias='AccessToken')
    token_type: (str | None) = Field(default=None, alias='TokenType')
    expiration_date: (datetime | None) = Field(default=None, alias='ExpirationDate')
    absolute_expiration_date: (datetime | None) = Field(default=None, alias='AbsoluteExpirationDate')
    user_id: (str | None) = Field(default=None, alias='UserId')
    internal_user_name: (str | None) = Field(default=None, alias='InternalUserName')
    is_two_factor_required: (bool | None) = Field(default=None, alias='IsTwoFactorRequired')
    is_internal_two_factor_required: (bool | None) = Field(default=None, alias='IsInternalTwoFactorRequired')
    sso_access_token: (str | None) = Field(default=None, alias='SSOAccessToken')

class PkceRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    authorization_code: (str | None) = Field(default=None, alias='AuthorizationCode')
    code_verifier: (str | None) = Field(default=None, alias='CodeVerifier')
    client_id: (str | None) = Field(default=None, alias='ClientId')
    redirect_uri: (str | None) = Field(default=None, alias='RedirectUri')

class DisableTokenRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    security_token: (str | None) = Field(default=None, alias='SecurityToken')

class ImplicitClientUpgradeRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    implicit_token: (str | None) = Field(default=None, alias='ImplicitToken')

class AuthInformation(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    allow_direct: (bool | None) = Field(default=None, alias='AllowDirect')
    allow_service_registration: (bool | None) = Field(default=None, alias='AllowServiceRegistration')
    automate_redirect_uri: (str | None) = Field(default=None, alias='AutomateRedirectUri')
    services: (list[AuthService] | None) = Field(default=None, alias='Services')
