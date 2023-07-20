from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ExpenseTypeReferenceModel import ExpenseTypeReferenceModel
from pyconnectwise.models.manage.ChargeCodeReferenceModel import ChargeCodeReferenceModel

class ChargeCodeExpenseTypeModel(ConnectWiseModel):
    id: int
    type: ExpenseTypeReferenceModel
    charge_code: ChargeCodeReferenceModel
    _info: dict[str, str]