from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class Segment1type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment2type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment3type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment4type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment5type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment6type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment7type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment8type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment9type(str, Enum):
    Account = 'Account'
    Class = 'Class'
class Segment10type(str, Enum):
    Account = 'Account'
    Class = 'Class'

class GLCaptionModel(ConnectWiseModel):
    id: int
    segment1: str
    segment2: str
    segment3: str
    segment4: str
    segment5: str
    segment6: str
    segment7: str
    segment8: str
    segment9: str
    segment10: str
    segment1type: Segment1type
    segment2type: Segment2type
    segment3type: Segment3type
    segment4type: Segment4type
    segment5type: Segment5type
    segment6type: Segment6type
    segment7type: Segment7type
    segment8type: Segment8type
    segment9type: Segment9type
    segment10type: Segment10type
    cogs1: str
    cogs2: str
    cogs3: str
    cogs4: str
    cogs5: str
    cogs6: str
    cogs7: str
    cogs8: str
    cogs9: str
    cogs10: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True