from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.CountryReferenceModel import CountryReferenceModel
from pyconnectwise.models.manage.RelationshipReferenceModel import RelationshipReferenceModel
from pyconnectwise.models.manage.ContactDepartmentReferenceModel import ContactDepartmentReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from enum import Enum
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.ContactCommunicationItemModel import ContactCommunicationItemModel
from pyconnectwise.models.manage.ContactTypeReferenceModel import ContactTypeReferenceModel
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel
from pyconnectwise.models.manage.DocumentReferenceModel import DocumentReferenceModel
class Gender(str, Enum):
    Female = 'Female'
    Male = 'Male'
class Presence(str, Enum):
    NoAgent = 'NoAgent'
    Online = 'Online'
    DoNotDisturb = 'DoNotDisturb'
    Away = 'Away'
    Offline = 'Offline'

class ContactModel(ConnectWiseModel):
    id: int
    first_name: str
    last_name: str
    company: CompanyReferenceModel
    site: SiteReferenceModel
    address_line1: str
    address_line2: str
    city: str
    state: str
    zip: str
    country: CountryReferenceModel
    relationship: RelationshipReferenceModel
    relationship_override: str
    department: ContactDepartmentReferenceModel
    inactive_flag: bool
    default_merge_contact_id: int
    security_identifier: str
    manager_contact: ContactReferenceModel
    assistant_contact: ContactReferenceModel
    title: str
    school: str
    nick_name: str
    married_flag: bool
    children_flag: bool
    children: str
    significant_other: str
    portal_password: str
    portal_security_level: int
    disable_portal_login_flag: bool
    unsubscribe_flag: bool
    gender: Gender
    birth_day: str
    anniversary: str
    presence: Presence
    mobile_guid: str
    facebook_url: str
    twitter_url: str
    linked_in_url: str
    default_phone_type: str
    default_phone_nbr: str
    default_phone_extension: str
    default_billing_flag: bool
    default_flag: bool
    user_defined_field1: str
    user_defined_field2: str
    user_defined_field3: str
    user_defined_field4: str
    user_defined_field5: str
    user_defined_field6: str
    user_defined_field7: str
    user_defined_field8: str
    user_defined_field9: str
    user_defined_field10: str
    company_location: SystemLocationReferenceModel
    communication_items: list[ContactCommunicationItemModel]
    types: list[ContactTypeReferenceModel]
    integrator_tags: list[str]
    custom_fields: list[CustomFieldValueModel]
    photo: DocumentReferenceModel
    ignore_duplicates: bool
    _info: dict[str, str]
    type_ids: list[int]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True