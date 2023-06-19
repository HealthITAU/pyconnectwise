from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ManagedDevicesIntegrationReferenceModel import ManagedDevicesIntegrationReferenceModel
from pyconnectwise.models.manage.NotificationRecipientReferenceModel import NotificationRecipientReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from enum import Enum
class LogType(str, Enum):
    All = 'All'
    Error = 'Error'
    NewManagedSolution = 'NewManagedSolution'
    NewDeviceType = 'NewDeviceType'
    NewConfiguration = 'NewConfiguration'
    NewAddition = 'NewAddition'
    Info = 'Info'

class ManagedDevicesIntegrationNotificationModel(ConnectWiseModel):
    id: int
    managed_devices_integration: ManagedDevicesIntegrationReferenceModel
    notify_who: NotificationRecipientReferenceModel
    member: MemberReferenceModel
    log_type: LogType
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True