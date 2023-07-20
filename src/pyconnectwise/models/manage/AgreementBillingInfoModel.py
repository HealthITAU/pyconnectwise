from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class AgreementBillingInfoModel(ConnectWiseModel):
    agreement_name: str
    agreement_type: str
    agreement_amount: float
    agreement_rec_id: int
    parent_rec_id: int