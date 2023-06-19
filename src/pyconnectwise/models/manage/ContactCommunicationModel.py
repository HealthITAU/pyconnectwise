from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CommunicationTypeReferenceModel import CommunicationTypeReferenceModel
from enum import Enum
class CommunicationType(str, Enum):
    Email = 'Email'
    Fax = 'Fax'
    Phone = 'Phone'

class ContactCommunicationModel(ConnectWiseModel):
    id: int
    contact_id: int
    type: CommunicationTypeReferenceModel
    value: str
    extension: str
    default_flag: bool
    mobile_guid: str
    communication_type: CommunicationType
    domain: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True