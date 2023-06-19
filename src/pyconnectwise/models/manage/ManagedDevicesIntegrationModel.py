from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.IntegratorLoginReferenceModel import IntegratorLoginReferenceModel
class LoginBy(str, Enum):
    Global = 'Global'
    Member = 'Member'
class DefaultBillingLevel(str, Enum):
    Detail = 'Detail'
    Summary = 'Summary'

class ManagedDevicesIntegrationModel(ConnectWiseModel):
    id: int
    name: str
    solution: str
    portal_url: str
    login_by: LoginBy
    global_login_username: str
    global_login_password: str
    default_billing_level: DefaultBillingLevel
    management_it_setup_type: str
    default_location: SystemLocationReferenceModel
    default_department: SystemDepartmentReferenceModel
    integrator_login: IntegratorLoginReferenceModel
    match_on_serial_number_flag: bool
    disable_new_cross_references_flag: bool
    config_bill_customer_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True