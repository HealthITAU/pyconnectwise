from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class EmailTokenModel(ConnectWiseModel):
    id: int
    token: str
    description: str
    address_flag: bool
    agreement_flag: bool
    company_flag: bool
    config_flag: bool
    contact_flag: bool
    invoice_flag: bool
    purchase_order_flag: bool
    purchase_order_status_flag: bool
    rma_flag: bool
    sales_flag: bool
    service_flag: bool
    tracks_flag: bool
    workflow_flag: bool
    portal_password_flag: bool

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True