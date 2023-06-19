from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from enum import Enum
class Language(str, Enum):
    English = 'English'
    Spanish = 'Spanish'
    French = 'French'
    British = 'British'
    Australian = 'Australian'
    BrazilianPortuguese = 'BrazilianPortuguese'
    CanadianFrench = 'CanadianFrench'
    German = 'German'
    NewZealand = 'NewZealand'
    Dutch = 'Dutch'

class PortalConfigurationModel(ConnectWiseModel):
    id: int
    name: str
    default_flag: bool
    company: CompanyReferenceModel
    login_background_color: str
    portal_background_color: str
    menu_color: str
    button_color: str
    header_color: str
    url: str
    language: Language
    welcome_text: str
    board_ids: list[int]
    agreement_type_ids: list[int]
    config_type_ids: list[int]
    location_ids: list[int]
    portal_image_copy_success_flag: bool
    display_vendor_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True