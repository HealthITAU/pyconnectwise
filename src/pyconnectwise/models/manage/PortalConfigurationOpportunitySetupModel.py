from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.OpportunityStatusReferenceModel import OpportunityStatusReferenceModel
from pyconnectwise.models.manage.ActivityTypeReferenceModel import ActivityTypeReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.OpportunityStatusReferenceModel import OpportunityStatusReferenceModel
from pyconnectwise.models.manage.ActivityTypeReferenceModel import ActivityTypeReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel

class PortalConfigurationOpportunitySetupModel(ConnectWiseModel):
    id: int
    opportunity_status_rec_i_ds: list[int]
    add_all_opportunity_statuses: bool
    remove_all_opportunity_statuses: bool
    opportunity_type_rec_i_ds: list[int]
    add_all_opportunity_types: bool
    remove_all_opportunity_types: bool
    restrict_view_by_opportunity_status_flag: bool
    restrict_view_by_opportunity_type_flag: bool
    acceptance_change_status_flag: bool
    acceptance_create_activity_flag: bool
    acceptance_opportunity_status: OpportunityStatusReferenceModel
    acceptance_send_email_flag: bool
    acceptance_email_from_first_name: str
    acceptance_email_from_last_name: str
    acceptance_email_subject: str
    acceptance_email_body: str
    acceptance_from_email: str
    acceptance_email_activity_type: ActivityTypeReferenceModel
    acceptance_email_assigned_by_member: MemberReferenceModel
    rejection_change_status_flag: bool
    rejection_create_activity_flag: bool
    rejection_opportunity_status: OpportunityStatusReferenceModel
    rejection_send_email_flag: bool
    rejection_email_from_first_name: str
    rejection_email_from_last_name: str
    rejection_from_email: str
    rejection_email_subject: str
    rejection_email_body: str
    rejection_email_activity_type: ActivityTypeReferenceModel
    rejection_email_assigned_by_member: MemberReferenceModel
    confirmation_send_email_flag: bool
    confirmation_email_use_default_company_email_address_flag: bool
    confirmation_email_from_first_name: str
    confirmation_email_from_last_name: str
    confirmation_from_email: str
    confirmation_email_subject: str
    confirmation_email_body: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True