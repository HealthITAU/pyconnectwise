from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ActivityTypeReferenceModel import ActivityTypeReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.ActivityStatusReferenceModel import ActivityStatusReferenceModel
from pyconnectwise.models.manage.OpportunityReferenceModel import OpportunityReferenceModel
from pyconnectwise.models.manage.TicketReferenceModel import TicketReferenceModel
from pyconnectwise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from pyconnectwise.models.manage.CampaignReferenceModel import CampaignReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.ScheduleStatusReferenceModel import ScheduleStatusReferenceModel
from pyconnectwise.models.manage.ReminderReferenceModel import ReminderReferenceModel
from pyconnectwise.models.manage.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel

class ActivityModel(ConnectWiseModel):
    id: int
    name: str
    type: ActivityTypeReferenceModel
    company: CompanyReferenceModel
    contact: ContactReferenceModel
    phone_number: str
    email: str
    status: ActivityStatusReferenceModel
    opportunity: OpportunityReferenceModel
    ticket: TicketReferenceModel
    agreement: AgreementReferenceModel
    campaign: CampaignReferenceModel
    notes: str
    date_start: str
    date_end: str
    assigned_by: MemberReferenceModel
    assign_to: MemberReferenceModel
    schedule_status: ScheduleStatusReferenceModel
    reminder: ReminderReferenceModel
    where: ServiceLocationReferenceModel
    notify_flag: bool
    mobile_guid: str
    currency: CurrencyReferenceModel
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True