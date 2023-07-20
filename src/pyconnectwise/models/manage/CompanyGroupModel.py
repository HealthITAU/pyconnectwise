from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.GroupReferenceModel import GroupReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel

class CompanyGroupModel(ConnectWiseModel):
    id: int
    group: GroupReferenceModel
    company: CompanyReferenceModel
    default_contact_flag: bool
    all_contacts_flag: bool
    remove_all_contacts_flag: bool
    unsubscribe_flag: bool
    contact_ids: list[int]
    _info: dict[str, str]