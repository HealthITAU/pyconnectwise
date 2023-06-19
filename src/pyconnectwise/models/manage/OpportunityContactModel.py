from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.OpportunitySalesRoleReferenceModel import OpportunitySalesRoleReferenceModel

class OpportunityContactModel(ConnectWiseModel):
    id: int
    contact: ContactReferenceModel
    company: CompanyReferenceModel
    role: OpportunitySalesRoleReferenceModel
    notes: str
    referral_flag: bool
    opportunity_id: int
    phone_number: str
    email_address: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True