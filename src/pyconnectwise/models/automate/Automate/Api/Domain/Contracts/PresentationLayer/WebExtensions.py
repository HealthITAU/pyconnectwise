
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class ExtensionClaimViewModel(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    extension_claim_type_id: (int | None) = Field(default=None, alias='ExtensionClaimTypeId')
    display_name: (str | None) = Field(default=None, alias='DisplayName')
    description: (str | None) = Field(default=None, alias='Description')
    is_assigned: (bool | None) = Field(default=None, alias='IsAssigned')
    is_default_claim: (bool | None) = Field(default=None, alias='IsDefaultClaim')

class AssignedWebExtension(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    web_extension_id: (int | None) = Field(default=None, alias='WebExtensionId')
    assigned_claims: (list[int] | None) = Field(default=None, alias='AssignedClaims')

class UserClassWebExtensionViewModel(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    web_extension_id: (int | None) = Field(default=None, alias='WebExtensionId')
    web_extension_name: (str | None) = Field(default=None, alias='WebExtensionName')
    extension_claims: (list[ExtensionClaimViewModel] | None) = Field(default=None, alias='ExtensionClaims')

class UserClassWebExtensionRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    assigned_extensions: (list[AssignedWebExtension] | None) = Field(default=None, alias='AssignedExtensions')
