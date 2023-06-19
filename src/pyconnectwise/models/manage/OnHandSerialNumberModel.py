from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CatalogItemReferenceModel import CatalogItemReferenceModel
from pyconnectwise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel
from pyconnectwise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel

class OnHandSerialNumberModel(ConnectWiseModel):
    id: int
    serial: str
    catalog_item: CatalogItemReferenceModel
    warehouse: WarehouseReferenceModel
    warehouse_bin: WarehouseBinReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True