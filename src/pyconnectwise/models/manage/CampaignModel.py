from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CampaignTypeReferenceModel import CampaignTypeReferenceModel
from pyconnectwise.models.manage.CampaignSubTypeReferenceModel import CampaignSubTypeReferenceModel
from pyconnectwise.models.manage.CampaignStatusReferenceModel import CampaignStatusReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.GroupReferenceModel import GroupReferenceModel

class CampaignModel(ConnectWiseModel):
    id: int
    name: str
    type: CampaignTypeReferenceModel
    sub_type: CampaignSubTypeReferenceModel
    status: CampaignStatusReferenceModel
    start_date: str
    end_date: str
    location_id: int
    member: MemberReferenceModel
    inactive: bool
    inactive_days_after_end: int
    notes: str
    default_group: GroupReferenceModel
    marketing_manager_default_track_id: int
    opportunity_default_track_id: int
    impressions: int
    budget_revenue: float
    budget_cost: float
    actual_cost: float
    budget_gross_margin: float
    budget_r_o_i: float
    actual_revenue: float
    actual_gross_margin: float
    actual_r_o_i: float
    emails_sent: int
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True