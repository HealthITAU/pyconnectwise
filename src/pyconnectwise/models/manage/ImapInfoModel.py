from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.EmailConnectorReferenceModel import EmailConnectorReferenceModel

class ImapInfoModel(ConnectWiseModel):
    id: int
    name: str
    email_connector: EmailConnectorReferenceModel
    _info: dict[str, str]