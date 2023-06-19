from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CatalogItemReferenceModel import CatalogItemReferenceModel
from pyconnectwise.models.manage.ProductCategoryReferenceModel import ProductCategoryReferenceModel
from pyconnectwise.models.manage.ProductSubCategoryReferenceModel import ProductSubCategoryReferenceModel

class PricingDetailModel(ConnectWiseModel):
    id: int
    product: CatalogItemReferenceModel
    category: ProductCategoryReferenceModel
    sub_category: ProductSubCategoryReferenceModel
    start_date: str
    end_date: str
    no_end_date: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True