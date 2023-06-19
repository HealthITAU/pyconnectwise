from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.LdapConfigurationReferenceModel import LdapConfigurationReferenceModel

class DepartmentLocationModel(ConnectWiseModel):
    id: int
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    department_manager: MemberReferenceModel
    dispatch: MemberReferenceModel
    service_manager: MemberReferenceModel
    duty_manager: MemberReferenceModel
    ldap_config: LdapConfigurationReferenceModel
    add_all_locations: bool
    remove_all_locations: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True