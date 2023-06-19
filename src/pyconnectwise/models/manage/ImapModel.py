from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.EmailConnectorReferenceModel import EmailConnectorReferenceModel

class ImapModel(ConnectWiseModel):
    id: int
    name: str
    imap_name: str
    processed_name: str
    failed_folder: str
    server: str
    user_name: str
    password: str
    port: int
    ssl_flag: bool
    email_connector: EmailConnectorReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True