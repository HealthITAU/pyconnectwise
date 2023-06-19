from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class SsoType(str, Enum):
    CWSSO = 'CWSSO'
    SAML = 'SAML'

class SsoConfigurationModel(ConnectWiseModel):
    id: int
    name: str
    sso_type: SsoType
    inactive_flag: bool
    saml_entity_id: str
    saml_sign_in_url: str
    saml_idp_certificate: str
    saml_certificate_name: str
    saml_certificate_issued_to: str
    saml_certificate_thumbprint: str
    saml_certificate_valid_from: str
    saml_certificate_valid_to: str
    location_ids: list[int]
    client_id: str
    sts_base_url: str
    sts_user_admin_url: str
    token: str
    submitted_member_count: int
    all_members_submitted: bool
    _info: dict[str, str]
    is_sso_on_by_default: bool

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True