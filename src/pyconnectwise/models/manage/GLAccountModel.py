from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.MappedTypeReferenceModel import MappedTypeReferenceModel
from pyconnectwise.models.manage.MappedRecordReferenceModel import MappedRecordReferenceModel
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

class GLAccountModel(ConnectWiseModel):
    id: int
    gl_type: GlType
    mapped_type: MappedTypeReferenceModel
    mapped_record: MappedRecordReferenceModel
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
    product_id: str
    inventory: str
    sales_code: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True