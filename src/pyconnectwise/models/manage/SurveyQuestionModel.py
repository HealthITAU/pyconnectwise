from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.SurveyReferenceModel import SurveyReferenceModel
from enum import Enum
class FieldType(str, Enum):
    TextArea = 'TextArea'
    Button = 'Button'
    Currency = 'Currency'
    Date = 'Date'
    Hyperlink = 'Hyperlink'
    IPAddress = 'IPAddress'
    Checkbox = 'Checkbox'
    Number = 'Number'
    Percent = 'Percent'
    Text = 'Text'
    Password = 'Password'
class EntryType(str, Enum):
    Date = 'Date'
    EntryField = 'EntryField'
    List = 'List'
    Option = 'Option'

class SurveyQuestionModel(ConnectWiseModel):
    id: int
    survey: SurveyReferenceModel
    field_type: FieldType
    entry_type: EntryType
    sequence_number: float
    question: str
    number_of_decimals: int
    required_flag: bool
    inactive_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True