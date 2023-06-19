from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.EmailConnectorReferenceModel import EmailConnectorReferenceModel

class Office365EmailSetupModel(ConnectWiseModel):
    id: int
    name: str
    username: str
    inbox_folder: str
    processed_folder: str
    failed_folder: str
    tenant_id: str
    client_id: str
    client_secret: str
    authorized_flag: bool
    inactive_flag: bool
    email_connector: EmailConnectorReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True