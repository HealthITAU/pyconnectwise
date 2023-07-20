from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.EmailConnectorParsingTypeReferenceModel import EmailConnectorParsingTypeReferenceModel

class EmailConnectorParsingStyleModel(ConnectWiseModel):
    id: int
    parsing_type: EmailConnectorParsingTypeReferenceModel
    parse_rule: str
    priority: int
    _info: dict[str, str]