from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel

class MemberDeactivationServiceTeamModel(ConnectWiseModel):
    count: int
    re_assign_to_member: MemberReferenceModel