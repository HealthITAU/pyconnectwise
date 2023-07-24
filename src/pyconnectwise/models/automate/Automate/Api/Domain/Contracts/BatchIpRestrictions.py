
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class DeleteIpRestrictionsBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ip_restrictions_ids: (list[UUID] | None) = Field(default=None, alias='IpRestrictionsIds')

class DeleteIpRestrictionsBatchResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ip_restrictions_id: (UUID | None) = Field(default=None, alias='IpRestrictionsId', example='00000000-0000-0000-0000-000000000000')
    result_details: (ResponseResult | None) = Field(default=None, alias='ResultDetails')

class AddIpRestrictionsBatchResult(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ip_address_guid: (UUID | None) = Field(default=None, alias='IpAddressGuid', example='00000000-0000-0000-0000-000000000000')
    name: (str | None) = Field(default=None, alias='Name')
    ip_address: (str | None) = Field(default=None, alias='IpAddress')
    windows_client_access: (bool | None) = Field(default=None, alias='WindowsClientAccess')
    web_client_access: (bool | None) = Field(default=None, alias='WebClientAccess')
    result_details: (ResponseResult | None) = Field(default=None, alias='ResultDetails')

class DeleteIpRestrictionsBatchResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ip_restrictions_results: (list[DeleteIpRestrictionsBatchResult] | None) = Field(default=None, alias='IpRestrictionsResults')
    contains_unsuccessful_results: (bool | None) = Field(default=None, alias='ContainsUnsuccessfulResults')

class AddIpRestrictionsBatchRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ip_restriction_rules: (list[IpRestrictions.IpRestrictionRule] | None) = Field(default=None, alias='IpRestrictionRules')

class AddIpRestrictionsBatchResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ip_restrictions_results: (list[AddIpRestrictionsBatchResult] | None) = Field(default=None, alias='IpRestrictionsResults')
    contains_unsuccessful_results: (bool | None) = Field(default=None, alias='ContainsUnsuccessfulResults')
from . import IpRestrictions, ResponseResult
from uuid import UUID
