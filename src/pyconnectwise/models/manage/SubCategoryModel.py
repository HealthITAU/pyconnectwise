from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ProductCategoryReferenceModel import ProductCategoryReferenceModel

class SubCategoryModel(ConnectWiseModel):
    id: int
    name: str
    inactive_flag: bool
    integration_xref: str
    default_flag: bool
    category: ProductCategoryReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True