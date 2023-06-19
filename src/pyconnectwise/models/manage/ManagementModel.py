from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ConfigurationStatusReferenceModel import ConfigurationStatusReferenceModel
from pyconnectwise.models.manage.ConfigurationStatusReferenceModel import ConfigurationStatusReferenceModel
from pyconnectwise.models.manage.IntegratorLoginReferenceModel import IntegratorLoginReferenceModel

class ManagementModel(ConnectWiseModel):
    id: int
    run_time: str
    added_configuration_status: ConfigurationStatusReferenceModel
    deleted_configuration_status: ConfigurationStatusReferenceModel
    integrator_login: IntegratorLoginReferenceModel
    schedule_executive_summary_report_flag: bool
    executive_summary_report_schedule_day: int
    executive_summary_report_schedule_hour: int
    executive_summary_report_schedule_minute: int
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True