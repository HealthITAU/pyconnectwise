from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ScheduleEntryReferenceModel import ScheduleEntryReferenceModel
from pyconnectwise.models.manage.ServiceCodeReferenceModel import ServiceCodeReferenceModel
from enum import Enum
class ChildScheduleAction(str, Enum):
    Transfer = 'Transfer'
    Delete = 'Delete'
    Done = 'Done'

class TicketTaskModel(ConnectWiseModel):
    id: int
    ticket_id: int
    notes: str
    closed_flag: bool
    priority: int
    schedule: ScheduleEntryReferenceModel
    code: ServiceCodeReferenceModel
    resolution: str
    child_schedule_action: ChildScheduleAction
    child_ticket_id: int
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True