from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class DocumentSetupModel(ConnectWiseModel):
    id: int
    upload_as_link_flag: bool
    is_public_flag: bool
    doc_path: str
    template_path: str
    template_output_path: str
    _info: dict[str, str]