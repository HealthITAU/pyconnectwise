from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.TaxCodeReferenceModel import TaxCodeReferenceModel
class LevelOne(str, Enum):
    NonTaxable = 'NonTaxable'
    Taxable = 'Taxable'
class LevelTwo(str, Enum):
    NonTaxable = 'NonTaxable'
    Taxable = 'Taxable'
class LevelThree(str, Enum):
    NonTaxable = 'NonTaxable'
    Taxable = 'Taxable'
class LevelFour(str, Enum):
    NonTaxable = 'NonTaxable'
    Taxable = 'Taxable'
class LevelFive(str, Enum):
    NonTaxable = 'NonTaxable'
    Taxable = 'Taxable'
class LevelSix(str, Enum):
    NonTaxable = 'NonTaxable'
    Taxable = 'Taxable'

class TaxCodeXRefModel(ConnectWiseModel):
    id: int
    description: str
    default_flag: bool
    level_one: LevelOne
    level_two: LevelTwo
    level_three: LevelThree
    level_four: LevelFour
    level_five: LevelFive
    level_six: LevelSix
    tax_code: TaxCodeReferenceModel
    taxable_levels: list[int]
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True