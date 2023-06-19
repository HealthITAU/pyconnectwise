from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
class DelegationType(str, Enum):
    Approval = 'Approval'
    Project = 'Project'

class MemberDelegationModel(ConnectWiseModel):
    id: int
    delegation_type: DelegationType
    delegated_to: MemberReferenceModel
    date_start: str
    date_end: str
    member: MemberReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True