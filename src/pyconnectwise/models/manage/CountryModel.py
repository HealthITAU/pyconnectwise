from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.AddressFormatReferenceModel import AddressFormatReferenceModel

class CountryModel(ConnectWiseModel):
    id: int
    name: str
    default_flag: bool
    currency: CurrencyReferenceModel
    city_caption: str
    state_caption: str
    zip_caption: str
    zip_minimum_length: int
    dialing_prefix: str
    address_format: AddressFormatReferenceModel
    country_code: str
    localization_caption_one: str
    localization_value_one: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True