from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ProductCategoryReferenceModel import ProductCategoryReferenceModel

class SubCategoryInfoModel(ConnectWiseModel):
    id: int
    name: str
    category: ProductCategoryReferenceModel
    inactive_flag: bool
    _info: dict[str, str]