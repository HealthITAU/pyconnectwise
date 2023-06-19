from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.IvItemReferenceModel import IvItemReferenceModel

class GLExportAdjustmentTransactionDetailModel(ConnectWiseModel):
    gl_class: str
    description: str
    memo: str
    item: IvItemReferenceModel
    quantity: int
    total: float
    cost: float
    cost_account_number: str
    inventory_account_number: str
    account_number: str
    product_account_number: str

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True