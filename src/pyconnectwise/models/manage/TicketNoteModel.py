from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel

class TicketNoteModel(ConnectWiseModel):
    id: int
    ticket_id: int
    text: str
    detail_description_flag: bool
    internal_analysis_flag: bool
    resolution_flag: bool
    issue_flag: bool
    member: MemberReferenceModel
    contact: ContactReferenceModel
    customer_updated_flag: bool
    process_notifications: bool
    internal_flag: bool
    external_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True