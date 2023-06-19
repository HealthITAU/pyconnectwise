from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class NotificationType(str, Enum):
    Email = 'Email'
    Push = 'Push'
class NotificationTrigger(str, Enum):
    ActivityStatusReq = 'ActivityStatusReq'
    CustomerUpdated = 'CustomerUpdated'
    ExpenseReport = 'ExpenseReport'
    TicketStatusChange = 'TicketStatusChange'
    TicketStatusRequest = 'TicketStatusRequest'
    TimeNagApprover = 'TimeNagApprover'
    TimeNagMember = 'TimeNagMember'
    TimeSheet = 'TimeSheet'
    WorkflowRules = 'WorkflowRules'

class MemberNotificationSettingModel(ConnectWiseModel):
    id: int
    notification_type: NotificationType
    notification_trigger: NotificationTrigger
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True