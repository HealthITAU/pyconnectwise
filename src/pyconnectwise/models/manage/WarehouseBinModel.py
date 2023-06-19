from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel

class WarehouseBinModel(ConnectWiseModel):
    id: int
    name: str
    warehouse: WarehouseReferenceModel
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    min_quantity: float
    max_quantity: float
    overflow_bin: WarehouseBinReferenceModel
    manager: MemberReferenceModel
    length: float
    width: float
    height: float
    weight: float
    default_flag: bool
    inactive_flag: bool
    quantity_on_hand: int
    company: CompanyReferenceModel
    transfer_bin: WarehouseBinReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True