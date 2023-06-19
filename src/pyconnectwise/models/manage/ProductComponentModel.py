from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CatalogItemReferenceModel import CatalogItemReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ProductItemReferenceModel import ProductItemReferenceModel
from pyconnectwise.models.manage.ProductItemReferenceModel import ProductItemReferenceModel

class ProductComponentModel(ConnectWiseModel):
    id: int
    sequence_number: int
    quantity: float
    catalog_item: CatalogItemReferenceModel
    hide_price_flag: bool
    hide_item_identifier_flag: bool
    hide_description_flag: bool
    hide_quantity_flag: bool
    hide_extended_price_flag: bool
    vendor: CompanyReferenceModel
    parent_product_item: ProductItemReferenceModel
    product_item: ProductItemReferenceModel
    price: float
    cost: float
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True