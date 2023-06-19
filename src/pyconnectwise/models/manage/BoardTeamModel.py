from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel

class BoardTeamModel(ConnectWiseModel):
    id: int
    name: str
    team_leader: MemberReferenceModel
    members: list[int]
    default_flag: bool
    notify_on_ticket_delete: bool
    board_id: int
    location_id: int
    business_unit_id: int
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True