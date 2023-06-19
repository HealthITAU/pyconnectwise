from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel
from pyconnectwise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pyconnectwise.models.manage.ShipmentMethodReferenceModel import ShipmentMethodReferenceModel
from pyconnectwise.models.manage.ProductItemReferenceModel import ProductItemReferenceModel

class ProductPickingShippingDetailModel(ConnectWiseModel):
    id: int
    picked_quantity: int
    shipped_quantity: int
    warehouse: WarehouseReferenceModel
    warehouse_bin: WarehouseBinReferenceModel
    shipment_method: ShipmentMethodReferenceModel
    serial_number: str
    serial_number_ids: list[int]
    tracking_number: str
    product_item: ProductItemReferenceModel
    line_number: int
    quantity: int
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True