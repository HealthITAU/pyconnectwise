from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
class LevelCount(str, Enum):
    Level1 = 'Level1'
    Level2 = 'Level2'
    Level3 = 'Level3'
    Level4 = 'Level4'
    Level5 = 'Level5'
class FiscalYearStart(str, Enum):
    January = 'January'
    February = 'February'
    March = 'March'
    April = 'April'
    May = 'May'
    June = 'June'
    July = 'July'
    August = 'August'
    September = 'September'
    October = 'October'
    November = 'November'
    December = 'December'

class CorporateStructureModel(ConnectWiseModel):
    id: int
    level_count: LevelCount
    level1_name: str
    level2_name: str
    level3_name: str
    level4_name: str
    level5_name: str
    fiscal_year_start: FiscalYearStart
    location_caption: str
    group_caption: str
    base_currency: CurrencyReferenceModel
    president: MemberReferenceModel
    chief_operating_officer: MemberReferenceModel
    controller: MemberReferenceModel
    dispatcher: MemberReferenceModel
    service_manager: MemberReferenceModel
    duty_manager: MemberReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True