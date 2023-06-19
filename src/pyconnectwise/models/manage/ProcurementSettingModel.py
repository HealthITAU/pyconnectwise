from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class PrefixSuffixType(str, Enum):
    Prefix = 'Prefix'
    Suffix = 'Suffix'
class CostingMethod(str, Enum):
    FIFO = 'FIFO'
    LIFO = 'LIFO'
    AverageCosting = 'AverageCosting'

class ProcurementSettingModel(ConnectWiseModel):
    id: int
    starting_purchase_order_num: int
    purchase_order_prefix: str
    purchase_order_suffix: str
    prefix_suffix_type: PrefixSuffixType
    disable_cost_updates_flag: bool
    disable_negative_inventory_flag: bool
    costing_method: CostingMethod
    auto_close_purchase_order_flag: bool
    auto_close_purchase_order_item_flag: bool
    auto_approve_purchase_order_flag: bool
    tax_purchase_order_flag: bool
    tax_freight_flag: bool
    use_vendor_tax_code_flag: bool
    num_decimal_places: int
    disable_auto_pick_flag: bool
    default_product_taxable_flag: bool
    eori_number: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True