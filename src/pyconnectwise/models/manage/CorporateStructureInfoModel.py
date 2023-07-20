from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel

class CorporateStructureInfoModel(ConnectWiseModel):
    id: int
    location_caption: str
    group_caption: str
    base_currency: CurrencyReferenceModel
    _info: dict[str, str]