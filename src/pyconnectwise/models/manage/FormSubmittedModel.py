from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel

class FormSubmittedModel(ConnectWiseModel):
    id: int
    campaign_id: int
    contact_id: int
    date_submitted: str
    url: str
    query_string: str
    page_type: str
    page_sub_type: str
    topic: str
    version: str
    status: str

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True