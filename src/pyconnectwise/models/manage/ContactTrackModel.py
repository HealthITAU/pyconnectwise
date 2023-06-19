from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel

class ContactTrackModel(ConnectWiseModel):
    id: int
    track_id: int
    name: str
    start_date: str
    end_date: str
    action_taken: int
    action_remaining: int
    started_by: str
    company: CompanyReferenceModel
    contact: ContactReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True