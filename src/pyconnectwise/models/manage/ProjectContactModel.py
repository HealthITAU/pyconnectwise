from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel

class ProjectContactModel(ConnectWiseModel):
    id: int
    project_id: int
    contact: ContactReferenceModel
    _info: dict[str, str]