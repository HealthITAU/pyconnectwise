from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.SalesTeamReferenceModel import SalesTeamReferenceModel
class TeamModelType(str, Enum):
    Individual = 'Individual'
    Team = 'Team'

class TeamModel(ConnectWiseModel):
    id: int
    type: TeamModelType
    member: MemberReferenceModel
    sales_team: SalesTeamReferenceModel
    commission_percent: int
    referral_flag: bool
    opportunity_id: int
    responsible_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True