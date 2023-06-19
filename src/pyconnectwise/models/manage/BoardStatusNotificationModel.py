from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.NotificationRecipientReferenceModel import NotificationRecipientReferenceModel
from pyconnectwise.models.manage.ServiceStatusReferenceModel import ServiceStatusReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel

class BoardStatusNotificationModel(ConnectWiseModel):
    id: int
    notify_who: NotificationRecipientReferenceModel
    status: ServiceStatusReferenceModel
    member: MemberReferenceModel
    email: str
    workflow_step: int
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True