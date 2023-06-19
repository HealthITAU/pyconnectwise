from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class ProductClass(str, Enum):
    Agreement = 'Agreement'
    Bundle = 'Bundle'
    Inventory = 'Inventory'
    NonInventory = 'NonInventory'
    Service = 'Service'

class CatalogItemInfoModel(ConnectWiseModel):
    id: int
    identifier: str
    description: str
    inactive_flag: bool
    product_class: ProductClass
    serialized_cost_flag: bool
    price: float
    cost: float
    taxable_flag: bool
    drop_ship_flag: bool
    special_order_flag: bool
    customer_description: str
    manufacturer_part_number: str
    vendor_sku: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True