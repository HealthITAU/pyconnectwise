from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from enum import Enum
class Status(str, Enum):
    Open = 'Open'
    Rejected = 'Rejected'
    PendingApproval = 'PendingApproval'
    ErrorsCorrected = 'ErrorsCorrected'
    PendingProjectApproval = 'PendingProjectApproval'
    ApprovedByTierOne = 'ApprovedByTierOne'
    RejectBySecondTier = 'RejectBySecondTier'
    ApprovedByTierTwo = 'ApprovedByTierTwo'
    ReadyToBill = 'ReadyToBill'
    Billed = 'Billed'
    WrittenOff = 'WrittenOff'
    BilledAgreement = 'BilledAgreement'

class ExpenseReportModel(ConnectWiseModel):
    id: int
    member: MemberReferenceModel
    year: int
    period: int
    date_start: str
    date_end: str
    status: Status
    total: float
    due_date: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True