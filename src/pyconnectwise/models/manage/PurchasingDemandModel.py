from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ProductDemandModel import ProductDemandModel
from pyconnectwise.models.manage.PurchaseOrderModel import PurchaseOrderModel

class PurchasingDemandModel(ConnectWiseModel):
    warehouse: WarehouseReferenceModel
    vendor: CompanyReferenceModel
    products: list[ProductDemandModel]
    purchase_order: PurchaseOrderModel

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True