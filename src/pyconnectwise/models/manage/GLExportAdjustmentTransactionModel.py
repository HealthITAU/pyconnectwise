from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.GLExportAdjustmentTransactionDetailModel import GLExportAdjustmentTransactionDetailModel

class GLExportAdjustmentTransactionModel(ConnectWiseModel):
    id: str
    document_type: str
    document_date: str
    gl_type_i_d: str
    account_number: str
    memo: str
    gl_class: str
    adjustment_description: str
    adjustment_detail: list[GLExportAdjustmentTransactionDetailModel]