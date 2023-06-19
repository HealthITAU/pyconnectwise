from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.TeamRoleReferenceModel import TeamRoleReferenceModel
from pyconnectwise.models.manage.TeamRoleReferenceModel import TeamRoleReferenceModel
from pyconnectwise.models.manage.TeamRoleReferenceModel import TeamRoleReferenceModel

class CrmModel(ConnectWiseModel):
    id: int
    company_list_count: int
    lock_probability_flag: bool
    account_manager_role: TeamRoleReferenceModel
    technical_contact_role: TeamRoleReferenceModel
    sales_rep_role: TeamRoleReferenceModel
    company_id_generation_flag: bool
    exclude_spaces_flag: bool
    field1_caption: str
    field2_caption: str
    field3_caption: str
    field4_caption: str
    field5_caption: str
    field6_caption: str
    field7_caption: str
    field8_caption: str
    field9_caption: str
    field10_caption: str
    primary_rep_caption: str
    secondary_rep_caption: str
    other1_caption: str
    other2_caption: str
    default_year: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True