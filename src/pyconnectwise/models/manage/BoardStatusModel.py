from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.BoardReferenceModel import BoardReferenceModel
from enum import Enum
from pyconnectwise.models.manage.ServiceEmailTemplateReferenceModel import ServiceEmailTemplateReferenceModel
from pyconnectwise.models.manage.StatusIndicatorReferenceModel import StatusIndicatorReferenceModel
class EscalationStatus(str, Enum):
    NotResponded = 'NotResponded'
    Responded = 'Responded'
    ResolutionPlan = 'ResolutionPlan'
    Resolved = 'Resolved'
    NoEscalation = 'NoEscalation'

class BoardStatusModel(ConnectWiseModel):
    id: int
    name: str
    board: BoardReferenceModel
    sort_order: int
    display_on_board: bool
    inactive: bool
    closed_status: bool
    time_entry_not_allowed: bool
    default_flag: bool
    escalation_status: EscalationStatus
    customer_portal_description: str
    customer_portal_flag: bool
    email_template: ServiceEmailTemplateReferenceModel
    status_indicator: StatusIndicatorReferenceModel
    custom_status_indicator_name: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True