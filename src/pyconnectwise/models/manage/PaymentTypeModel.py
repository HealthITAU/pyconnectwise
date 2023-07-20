from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ClassificationReferenceModel import ClassificationReferenceModel

class PaymentTypeModel(ConnectWiseModel):
    id: int
    name: str
    classification: ClassificationReferenceModel
    default_flag: bool
    company_flag: bool
    _info: dict[str, str]