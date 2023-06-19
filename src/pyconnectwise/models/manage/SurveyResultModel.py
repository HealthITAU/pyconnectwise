from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ContactReferenceModel import ContactReferenceModel
from pyconnectwise.models.manage.SurveyResultDetailModel import SurveyResultDetailModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel

class SurveyResultModel(ConnectWiseModel):
    id: int
    ticket_id: int
    email_address: str
    footer_response: str
    contact_me_flag: bool
    contact: ContactReferenceModel
    results: list[SurveyResultDetailModel]
    total_points: int
    company: CompanyReferenceModel
    survey_id: int
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True