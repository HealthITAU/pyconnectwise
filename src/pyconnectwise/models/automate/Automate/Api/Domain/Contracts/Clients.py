
from __future__ import annotations
from datetime import datetime
from typing import Any
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class FilterByComputerPermissionsRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    computer_permissions: (list[str] | None) = Field(default=None, alias='ComputerPermissions')

class Client(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    client_id: (int | None) = Field(default=None, alias='ClientId')
    name: (str | None) = Field(default=None, alias='Name')

class ContactSource(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    contact_source_type_id: (int | None) = Field(default=None, alias='ContactSourceTypeId')
    name: (str | None) = Field(default=None, alias='Name')

class DeploymentLogin(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    deployment_login_id: (int | None) = Field(default=None, alias='DeploymentLoginId')
    client: (Client | None) = Field(default=None, alias='Client')
    location: (Location | None) = Field(default=None, alias='Location')
    title: (str | None) = Field(default=None, alias='Title')
    username: (str | None) = Field(default=None, alias='Username')
    password: (str | None) = Field(default=None, alias='Password')
    url: (str | None) = Field(default=None, alias='Url')
    notes: (str | None) = Field(default=None, alias='Notes')

class Location(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    location_id: (int | None) = Field(default=None, alias='LocationId')
    name: (str | None) = Field(default=None, alias='Name')
    fax_number: (str | None) = Field(default=None, alias='FaxNumber')
    maintenance_window: (TemporaryApiContracts.MaintenanceWindowDefinition | None) = Field(default=None, alias='MaintenanceWindow')
    deployment_template: (Models.RemoteAgentTemplate | None) = Field(default=None, alias='DeploymentTemplate')
    router: (Models.Router | None) = Field(default=None, alias='Router')
    probe_id: (int | None) = Field(default=None, alias='ProbeId')
    external_id: (int | None) = Field(default=None, alias='ExternalId')
    script_extra2: (str | None) = Field(default=None, alias='ScriptExtra2')
    script_extra1: (str | None) = Field(default=None, alias='ScriptExtra1')
    script_router_address: (str | None) = Field(default=None, alias='ScriptRouterAddress')
    script_password: (str | None) = Field(default=None, alias='ScriptPassword')
    script_username: (str | None) = Field(default=None, alias='ScriptUsername')
    script_drive: (str | None) = Field(default=None, alias='ScriptDrive')
    router_port: (int | None) = Field(default=None, alias='RouterPort')
    comments: (str | None) = Field(default=None, alias='Comments')
    contact: (Models.Contact | None) = Field(default=None, alias='Contact')
    default_deployment_login: (TemporaryApiContracts.DeploymentLogin | None) = Field(default=None, alias='DefaultDeploymentLogin')
    phone_number: (str | None) = Field(default=None, alias='PhoneNumber')
    country: (str | None) = Field(default=None, alias='Country')
    zip_code: (str | None) = Field(default=None, alias='ZipCode')
    state: (str | None) = Field(default=None, alias='State')
    city: (str | None) = Field(default=None, alias='City')
    address2: (str | None) = Field(default=None, alias='Address2')
    address1: (str | None) = Field(default=None, alias='Address1')
    client: (Models.Client | None) = Field(default=None, alias='Client')
    default_deployment_group: (Models.Group | None) = Field(default=None, alias='DefaultDeploymentGroup')
    extra_fields: (list[ExtraFields.ExtraField] | None) = Field(default=None, alias='ExtraFields')

class Contact(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    contact_id: (int | None) = Field(default=None, alias='ContactId')
    first_name: (str | None) = Field(default=None, alias='FirstName')
    last_name: (str | None) = Field(default=None, alias='LastName')
    email_address: (str | None) = Field(default=None, alias='EmailAddress')
    phone_number: (str | None) = Field(default=None, alias='PhoneNumber')
    mobile_number: (str | None) = Field(default=None, alias='MobileNumber')
    pager_number: (str | None) = Field(default=None, alias='PagerNumber')
    fax_number: (str | None) = Field(default=None, alias='FaxNumber')
    address1: (str | None) = Field(default=None, alias='Address1')
    address2: (str | None) = Field(default=None, alias='Address2')
    city: (str | None) = Field(default=None, alias='City')
    state: (str | None) = Field(default=None, alias='State')
    zip_code: (str | None) = Field(default=None, alias='ZipCode')
    client: (Client | None) = Field(default=None, alias='Client')
    location: (Location | None) = Field(default=None, alias='Location')
    password: (str | None) = Field(default=None, alias='Password')
    permissions: (list[str] | None) = Field(default=None, alias='Permissions')
    is_managed: (bool | None) = Field(default=None, alias='IsManaged')
    is_activated: (bool | None) = Field(default=None, alias='IsActivated')
    date_created: (datetime | None) = Field(default=None, alias='DateCreated')
    last_update_date: (datetime | None) = Field(default=None, alias='LastUpdateDate')
    plugin_data: (dict[(str, dict[(str, dict[(str, Any)])])] | None) = Field(default=None, alias='PluginData')
    source: (ContactSource | None) = Field(default=None, alias='Source')
from . import ExtraFields
from .....LabTech.Models import TemporaryApiContracts
from .....LabTech import Models
