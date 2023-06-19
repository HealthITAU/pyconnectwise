from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
class InvoiceRule(str, Enum):
    All = 'All'
    Standard = 'Standard'
    Project = 'Project'
    Agreement = 'Agreement'
class RoutingRule(str, Enum):
    Account = 'Account'
    Territory = 'Territory'
    Creator = 'Creator'
    Department = 'Department'
    Location = 'Location'
    Member = 'Member'
    Project = 'Project'
    Sales = 'Sales'

class BillingSetupRoutingModel(ConnectWiseModel):
    id: int
    sequence_number: int
    invoice_rule: InvoiceRule
    routing_rule: RoutingRule
    member: MemberReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True