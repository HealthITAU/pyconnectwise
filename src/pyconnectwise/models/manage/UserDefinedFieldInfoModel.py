from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.UserDefinedFieldOptionModel import UserDefinedFieldOptionModel
class FieldTypeIdentifier(str, Enum):
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
class EntryTypeIdentifier(str, Enum):
    Date = 'Date'
    EntryField = 'EntryField'
    List = 'List'
    Option = 'Option'

class UserDefinedFieldInfoModel(ConnectWiseModel):
    id: int
    pod_id: int
    caption: str
    sequence_number: int
    help_text: str
    field_type_identifier: FieldTypeIdentifier
    number_decimals: int
    entry_type_identifier: EntryTypeIdentifier
    required_flag: bool
    display_on_screen_flag: bool
    read_only_flag: bool
    list_view_flag: bool
    button_url: str
    options: list[UserDefinedFieldOptionModel]
    business_unit_ids: list[int]
    location_ids: list[int]
    date_created: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True