# generated by datamodel-codegen:
#   filename:  All.json

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from . import (
    CompanyReference,
    CompanyTypeReference,
    ConfigurationQuestion,
    ConfigurationStatusReference,
    ConfigurationTypeReference,
    ContactReference,
    ContactTypeReference,
    CustomFieldValue,
    ManufacturerReference,
    MemberReference,
    SiteReference,
    SLAReference,
)


class CompanyTypeAssociation(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: int | None = None
    type: CompanyTypeReference | None = None
    company: CompanyReference | None = None
    field_info: dict[str, str] | None = Field(default=None, alias='_info')


class Configuration(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: int | None = None
    name: str
    """
     Max length: 100;
    """
    type: ConfigurationTypeReference | None = None
    status: ConfigurationStatusReference | None = None
    company: CompanyReference | None = None
    contact: ContactReference | None = None
    site: SiteReference | None = None
    location_id: int | None = Field(default=None, alias='locationId')
    business_unit_id: int | None = Field(default=None, alias='businessUnitId')
    device_identifier: str | None = Field(default=None, alias='deviceIdentifier')
    """
     Max length: 100;
    """
    serial_number: str | None = Field(default=None, alias='serialNumber')
    """
     Max length: 250;
    """
    model_number: str | None = Field(default=None, alias='modelNumber')
    """
     Max length: 50;
    """
    tag_number: str | None = Field(default=None, alias='tagNumber')
    """
     Max length: 50;
    """
    purchase_date: datetime | None = Field(default=None, alias='purchaseDate')
    installation_date: datetime | None = Field(default=None, alias='installationDate')
    installed_by: MemberReference | None = Field(default=None, alias='installedBy')
    warranty_expiration_date: datetime | None = Field(
        default=None, alias='warrantyExpirationDate'
    )
    vendor_notes: str | None = Field(default=None, alias='vendorNotes')
    notes: str | None = None
    mac_address: str | None = Field(default=None, alias='macAddress')
    """
     Max length: 25;
    """
    last_login_name: str | None = Field(default=None, alias='lastLoginName')
    """
     Max length: 100;
    """
    bill_flag: bool | None = Field(default=None, alias='billFlag')
    backup_successes: int | None = Field(default=None, alias='backupSuccesses')
    backup_incomplete: int | None = Field(default=None, alias='backupIncomplete')
    backup_failed: int | None = Field(default=None, alias='backupFailed')
    backup_restores: int | None = Field(default=None, alias='backupRestores')
    last_backup_date: datetime | None = Field(default=None, alias='lastBackupDate')
    backup_server_name: str | None = Field(default=None, alias='backupServerName')
    """
     Max length: 50;
    """
    backup_billable_space_gb: float | None = Field(
        default=None, alias='backupBillableSpaceGb'
    )
    backup_protected_device_list: str | None = Field(
        default=None, alias='backupProtectedDeviceList'
    )
    backup_year: int | None = Field(default=None, alias='backupYear')
    backup_month: int | None = Field(default=None, alias='backupMonth')
    ip_address: str | None = Field(default=None, alias='ipAddress')
    """
     Max length: 50;
    """
    default_gateway: str | None = Field(default=None, alias='defaultGateway')
    """
     Max length: 50;
    """
    os_type: str | None = Field(default=None, alias='osType')
    """
     Max length: 250;
    """
    os_info: str | None = Field(default=None, alias='osInfo')
    """
     Max length: 250;
    """
    cpu_speed: str | None = Field(default=None, alias='cpuSpeed')
    """
     Max length: 100;
    """
    ram: str | None = None
    """
     Max length: 25;
    """
    local_hard_drives: str | None = Field(default=None, alias='localHardDrives')
    parent_configuration_id: int | None = Field(
        default=None, alias='parentConfigurationId'
    )
    vendor: CompanyReference | None = None
    manufacturer: ManufacturerReference | None = None
    questions: list[ConfigurationQuestion] | None = None
    active_flag: bool | None = Field(default=None, alias='activeFlag')
    management_link: str | None = Field(default=None, alias='managementLink')
    """
     Max length: 1000;
    """
    remote_link: str | None = Field(default=None, alias='remoteLink')
    """
     Max length: 1000;
    """
    sla: SLAReference | None = None
    mobile_guid: UUID | None = Field(default=None, alias='mobileGuid')
    display_vendor_flag: bool | None = Field(default=None, alias='displayVendorFlag')
    company_location_id: int | None = Field(default=None, alias='companyLocationId')
    show_remote_flag: bool | None = Field(default=None, alias='showRemoteFlag')
    show_automate_flag: bool | None = Field(default=None, alias='showAutomateFlag')
    needs_renewal_flag: bool | None = Field(default=None, alias='needsRenewalFlag')
    manufacturer_part_number: str | None = Field(
        default=None, alias='manufacturerPartNumber'
    )
    """
     Max length: 50;
    """
    field_info: dict[str, str] | None = Field(default=None, alias='_info')
    custom_fields: list[CustomFieldValue] | None = Field(
        default=None, alias='customFields'
    )


class ContactTypeAssociation(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: int | None = None
    type: ContactTypeReference | None = None
    contact: ContactReference | None = None
    field_info: dict[str, str] | None = Field(default=None, alias='_info')
