from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.BillingStatusReferenceModel import BillingStatusReferenceModel

class ClosedInvoiceModel(ConnectWiseModel):
    id: int
    status: BillingStatusReferenceModel
    _info: dict[str, str]