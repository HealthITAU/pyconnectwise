from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pyconnectwise.models.manage.CatalogItemReferenceModel import CatalogItemReferenceModel
from enum import Enum
class BillingLevel(str, Enum):
    Detail = 'Detail'
    Summary = 'Summary'

class ManagementBackupModel(ConnectWiseModel):
    id: int
    type: AgreementTypeReferenceModel
    item: CatalogItemReferenceModel
    billing_level: BillingLevel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True