from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel

class SsoUserModel(ConnectWiseModel):
    id: int
    sso_user_id: str
    user_name: str
    first_name: str
    last_name: str
    email: str
    email_confirmed: bool
    disabled_flag: bool
    linked_flag: bool
    date_entered: str
    last_updated: str
    linked_member: MemberReferenceModel

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True