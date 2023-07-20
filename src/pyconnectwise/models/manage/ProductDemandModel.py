from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ProductDemandModel(ConnectWiseModel):
    product_rec_id: int
    quantity: int
    cost: float