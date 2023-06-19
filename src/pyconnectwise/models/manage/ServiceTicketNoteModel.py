from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.TicketReferenceModel import TicketReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
class NoteType(str, Enum):
    TicketNote = 'TicketNote'
    TimeEntryNote = 'TimeEntryNote'
    MeetingNote = 'MeetingNote'

class ServiceTicketNoteModel(ConnectWiseModel):
    id: int
    note_type: NoteType
    ticket: TicketReferenceModel
    text: str
    is_markdown_flag: bool
    detail_description_flag: bool
    internal_analysis_flag: bool
    resolution_flag: bool
    time_start: str
    time_end: str
    bundled_flag: bool
    merged_flag: bool
    issue_flag: bool
    original_author: str
    member: MemberReferenceModel
    contact: ContactReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True