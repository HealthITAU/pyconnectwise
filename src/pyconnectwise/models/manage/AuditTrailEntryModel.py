from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class AuditTrailEntryModel(ConnectWiseModel):
    text: str
    entered_date: str
    entered_by: str
    audit_type: str
    audit_sub_type: str
    audit_source: str

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True