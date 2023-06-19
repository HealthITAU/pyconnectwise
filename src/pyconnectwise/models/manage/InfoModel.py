from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.LicenseBitModel import LicenseBitModel

class InfoModel(ConnectWiseModel):
    version: str
    is_cloud: bool
    server_time_zone: str
    license_bits: list[LicenseBitModel]
    cloud_region: str

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True