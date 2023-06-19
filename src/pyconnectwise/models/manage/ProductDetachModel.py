from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class ProductDetachModel(ConnectWiseModel):
    remove_from_ticket: bool
    remove_from_invoice: bool
    remove_from_opportunity: bool
    remove_from_sales_order: bool
    remove_from_project: bool

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True