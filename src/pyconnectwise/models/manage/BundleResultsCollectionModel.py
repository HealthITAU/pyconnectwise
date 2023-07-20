from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.BundleResultModel import BundleResultModel

class BundleResultsCollectionModel(ConnectWiseModel):
    results: list[BundleResultModel]
    _info: dict[str, str]