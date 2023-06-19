from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class GlType(str, Enum):
    AP = 'AP'
    AR = 'AR'
    EE = 'EE'
    EI = 'EI'
    EO = 'EO'
    IA = 'IA'
    IT = 'IT'
    P = 'P'
    PF = 'PF'
    R = 'R'
    RA = 'RA'
    RD = 'RD'
    RE = 'RE'
    RP = 'RP'
    ST = 'ST'
    SD = 'SD'
    ET = 'ET'
    FT = 'FT'
    PT = 'PT'

class MappedTypeModel(ConnectWiseModel):
    id: int
    name: str
    table: str
    rec_id_field: str
    gl_type: GlType
    sort_order: int

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True