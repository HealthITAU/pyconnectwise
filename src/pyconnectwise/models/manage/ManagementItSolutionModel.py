from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class ManagementItSolutionType(str, Enum):
    LevelPlatforms = 'LevelPlatforms'
    NAble = 'NAble'
    Continuum = 'Continuum'
    Custom = 'Custom'

class ManagementItSolutionModel(ConnectWiseModel):
    id: int
    name: str
    management_it_solution_type: ManagementItSolutionType
    management_solution_name: str
    management_server_url: str
    webservice_override_url: str
    portal_override_login_url: str
    global_login_flag: bool
    global_login_username: str
    global_login_password: str
    using_ssl_flag: bool
    n_able_username: str
    n_able_password: str
    override_web_service_location_flag: bool
    override_login_location_flag: bool
    continuum_api_username: str
    continuum_api_password: str
    level_api_username: str
    level_api_password: str
    level_var_domain: str
    no_display_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True