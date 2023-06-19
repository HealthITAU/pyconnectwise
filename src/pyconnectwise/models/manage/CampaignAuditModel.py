from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.GroupReferenceModel import GroupReferenceModel

class CampaignAuditModel(ConnectWiseModel):
    id: int
    emails_sent: int
    emails_unsent: int
    documents_created: int
    email_subject: str
    group: GroupReferenceModel
    campaign_id: int
    created_by: str
    date_created: str

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True