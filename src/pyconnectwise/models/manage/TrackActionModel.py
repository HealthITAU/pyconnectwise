from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.ServiceTemplateReferenceModel import ServiceTemplateReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.ActivityTypeReferenceModel import ActivityTypeReferenceModel
from pyconnectwise.models.manage.ActivityStatusReferenceModel import ActivityStatusReferenceModel
from pyconnectwise.models.manage.CompanyStatusReferenceModel import CompanyStatusReferenceModel
from pyconnectwise.models.manage.TrackReferenceModel import TrackReferenceModel
from pyconnectwise.models.manage.TrackReferenceModel import TrackReferenceModel
from pyconnectwise.models.manage.GroupReferenceModel import GroupReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.NotificationRecipientReferenceModel import NotificationRecipientReferenceModel
from pyconnectwise.models.manage.NotificationRecipientReferenceModel import NotificationRecipientReferenceModel
class NotifyType(str, Enum):
    CreateActivity = 'CreateActivity'
    SendEmail = 'SendEmail'
    AddToGroup = 'AddToGroup'
    AttachTrack = 'AttachTrack'
    ChangeCompanyStatus = 'ChangeCompanyStatus'
    CreateServiceTicket = 'CreateServiceTicket'

class TrackActionModel(ConnectWiseModel):
    id: int
    notify_type: NotifyType
    service_template: ServiceTemplateReferenceModel
    specific_member_to: MemberReferenceModel
    email_recipient: str
    specific_member_from: MemberReferenceModel
    email_from: str
    subject: str
    notes: str
    activity_type: ActivityTypeReferenceModel
    activity_status: ActivityStatusReferenceModel
    company_status: CompanyStatusReferenceModel
    track: TrackReferenceModel
    attached_track: TrackReferenceModel
    group: GroupReferenceModel
    cc_contact: ContactReferenceModel
    bcc_contact: ContactReferenceModel
    days_to_execute: int
    notify_who: NotificationRecipientReferenceModel
    notify_from: NotificationRecipientReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True