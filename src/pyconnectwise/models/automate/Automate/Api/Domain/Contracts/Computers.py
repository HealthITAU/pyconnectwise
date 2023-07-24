
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class ContactAssociatedComputer(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    computer_id: (int | None) = Field(default=None, alias='ComputerId')
    computer_name: (str | None) = Field(default=None, alias='ComputerName')
    has_primary_contact: (bool | None) = Field(default=None, alias='HasPrimaryContact')
    is_primary_contact: (bool | None) = Field(default=None, alias='IsPrimaryContact')
    can_user_set_primary_status: (bool | None) = Field(default=None, alias='CanUserSetPrimaryStatus')
    client_name: (str | None) = Field(default=None, alias='ClientName')
    location_name: (str | None) = Field(default=None, alias='LocationName')

class SetComputerPrimaryContactRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_primary_contact: (bool | None) = Field(default=None, alias='IsPrimaryContact')

class Computer(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    computer_id: (int | None) = Field(default=None, alias='ComputerId')
    name: (str | None) = Field(default=None, alias='Name')
    friendly_name: (str | None) = Field(default=None, alias='FriendlyName')
    is_online: (bool | None) = Field(default=None, alias='IsOnline')
    location: (Clients.Location | None) = Field(default=None, alias='Location')
    client: (Clients.Client | None) = Field(default=None, alias='Client')
from . import Clients
