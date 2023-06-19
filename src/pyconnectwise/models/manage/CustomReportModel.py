from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class Module(str, Enum):
    Companies = 'Companies'
    Finance = 'Finance'
    Marketing = 'Marketing'
    Procurement = 'Procurement'
    Project = 'Project'
    Sales = 'Sales'
    ServiceDesk = 'ServiceDesk'
    TimeExpense = 'TimeExpense'

class CustomReportModel(ConnectWiseModel):
    id: int
    report_link: str
    name: str
    module: Module
    description: str
    generated_flag: bool
    parameter_prefix: str
    parameter_separator: str
    parameter_name_separator: str
    parameter_suffix: str
    location_flag: bool
    location_param_id: int
    location_default_flag: bool
    location_override: str
    department_flag: bool
    department_param_id: int
    department_default_flag: bool
    department_override: str
    territory_flag: bool
    territory_param_id: int
    territory_default_flag: bool
    territory_override: str
    company_flag: bool
    company_param_id: int
    company_override: str
    member_flag: bool
    member_param_id: int
    member_override: str
    start_date_flag: bool
    start_date_param_id: int
    start_date_override: str
    end_date_flag: bool
    end_date_param_id: int
    end_date_override: str
    opp_type_flag: bool
    opp_type_param_id: int
    opp_type_override: str
    opportunity_flag: bool
    opportunity_param_id: int
    opportunity_override: str
    marketing_campaign_flag: bool
    marketing_campaign_param_id: int
    marketing_campaign_override: str
    service_board_flag: bool
    service_board_param_id: int
    service_board_default_flag: bool
    service_board_override: str
    service_type_flag: bool
    service_type_param_id: int
    service_type_override: str
    service_status_flag: bool
    service_status_param_id: int
    service_status_override: str
    agreement_type_flag: bool
    agreement_type_param_id: int
    agreement_type_override: str
    agreement_flag: bool
    agreement_param_id: int
    agreement_override: str
    project_type_flag: bool
    project_type_param_id: int
    project_type_override: str
    project_flag: bool
    project_param_id: int
    project_override: str
    work_role_flag: bool
    work_role_param_id: int
    work_role_override: str
    work_type_flag: bool
    work_type_param_id: int
    work_type_override: str
    invoice_flag: bool
    invoice_param_id: int
    invoice_override: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True