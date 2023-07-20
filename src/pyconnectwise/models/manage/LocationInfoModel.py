from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CorporateStructureLevelReferenceModel import CorporateStructureLevelReferenceModel

class LocationInfoModel(ConnectWiseModel):
    id: int
    name: str
    location_flag: bool
    structure_level: CorporateStructureLevelReferenceModel
    _info: dict[str, str]