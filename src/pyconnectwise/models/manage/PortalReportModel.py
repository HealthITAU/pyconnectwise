from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.PortalConfigurationReferenceModel import PortalConfigurationReferenceModel

class PortalReportModel(ConnectWiseModel):
    id: int
    portal_configuration: PortalConfigurationReferenceModel
    name: str
    url: str
    open_same_window_flag: bool
    custom_flag: bool
    display_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True