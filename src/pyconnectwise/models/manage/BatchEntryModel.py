from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.InvoiceReferenceModel import InvoiceReferenceModel
from pyconnectwise.models.manage.PurchaseOrderReferenceModel import PurchaseOrderReferenceModel
from pyconnectwise.models.manage.PurchaseOrderLineItemReferenceModel import PurchaseOrderLineItemReferenceModel
from pyconnectwise.models.manage.ExpenseDetailReferenceModel import ExpenseDetailReferenceModel
from pyconnectwise.models.manage.AdjustmentDetailReferenceModel import AdjustmentDetailReferenceModel

class BatchEntryModel(ConnectWiseModel):
    id: int
    account_type: str
    name: str
    account_number: str
    debit: float
    credit: float
    cost: float
    item: str
    sales_code: str
    cost_of_goods_sold_account_number: str
    invoice: InvoiceReferenceModel
    purchase_order: PurchaseOrderReferenceModel
    line_item: PurchaseOrderLineItemReferenceModel
    transfer: str
    expense: ExpenseDetailReferenceModel
    adjustment_detail: AdjustmentDetailReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True