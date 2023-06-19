from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ConfigurationTypeReferenceModel import ConfigurationTypeReferenceModel
from pyconnectwise.models.manage.ConfigurationStatusReferenceModel import ConfigurationStatusReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ManufacturerReferenceModel import ManufacturerReferenceModel
from pyconnectwise.models.manage.ConfigurationQuestionModel import ConfigurationQuestionModel
from pyconnectwise.models.manage.SLAReferenceModel import SLAReferenceModel
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel

class ConfigurationModel(ConnectWiseModel):
    id: int
    name: str
    type: ConfigurationTypeReferenceModel
    status: ConfigurationStatusReferenceModel
    company: CompanyReferenceModel
    contact: ContactReferenceModel
    site: SiteReferenceModel
    location_id: int
    business_unit_id: int
    device_identifier: str
    serial_number: str
    model_number: str
    tag_number: str
    purchase_date: str
    installation_date: str
    installed_by: MemberReferenceModel
    warranty_expiration_date: str
    vendor_notes: str
    notes: str
    mac_address: str
    last_login_name: str
    bill_flag: bool
    backup_successes: int
    backup_incomplete: int
    backup_failed: int
    backup_restores: int
    last_backup_date: str
    backup_server_name: str
    backup_billable_space_gb: float
    backup_protected_device_list: str
    backup_year: int
    backup_month: int
    ip_address: str
    default_gateway: str
    os_type: str
    os_info: str
    cpu_speed: str
    ram: str
    local_hard_drives: str
    parent_configuration_id: int
    vendor: CompanyReferenceModel
    manufacturer: ManufacturerReferenceModel
    questions: list[ConfigurationQuestionModel]
    active_flag: bool
    management_link: str
    remote_link: str
    sla: SLAReferenceModel
    mobile_guid: str
    _info: dict[str, str]
    display_vendor_flag: bool
    company_location_id: int
    show_remote_flag: bool
    show_automate_flag: bool
    needs_renewal_flag: bool
    manufacturer_part_number: str
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True