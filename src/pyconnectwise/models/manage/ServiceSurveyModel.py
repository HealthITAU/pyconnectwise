from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.GenericIdIdentifierReferenceModel import GenericIdIdentifierReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel

class ServiceSurveyModel(ConnectWiseModel):
    id: int
    name: str
    inactive_flag: bool
    header_include_logo_flag: bool
    header_text: str
    header_text_visible_flag: bool
    footer_text: str
    footer_text_visible_flag: bool
    thank_you_text: str
    notify_who: GenericIdIdentifierReferenceModel
    notify_who_visible_flag: bool
    notify_member: MemberReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True