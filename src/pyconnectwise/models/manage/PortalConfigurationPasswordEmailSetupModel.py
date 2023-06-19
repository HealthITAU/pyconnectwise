from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class PortalConfigurationPasswordEmailSetupModel(ConnectWiseModel):
    id: int
    valid_password_email_use_custom_email_flag: bool
    valid_password_email_from_first_name: str
    valid_password_email_from_last_name: str
    valid_password_email_from_email: str
    valid_password_email_subject: str
    valid_password_email_body: str
    invalid_password_email_use_custom_email_flag: bool
    invalid_password_email_from_first_name: str
    invalid_password_email_from_last_name: str
    invalid_password_email_from_email: str
    invalid_password_email_subject: str
    invalid_password_email_body: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True