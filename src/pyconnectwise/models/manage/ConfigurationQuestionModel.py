from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class FieldType(str, Enum):
    TextArea = 'TextArea'
    Currency = 'Currency'
    Date = 'Date'
    Hyperlink = 'Hyperlink'
    IPAddress = 'IPAddress'
    Checkbox = 'Checkbox'
    Number = 'Number'
    Percent = 'Percent'
    Text = 'Text'
    Password = 'Password'

class ConfigurationQuestionModel(ConnectWiseModel):
    answer_id: int
    question_id: int
    question: str
    answer: Any
    sequence_number: float
    number_of_decimals: int
    field_type: FieldType
    required_flag: bool

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True