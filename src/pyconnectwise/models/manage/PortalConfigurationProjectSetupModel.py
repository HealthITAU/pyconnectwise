from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.PortalConfigurationReferenceModel import PortalConfigurationReferenceModel
from enum import Enum
class OnlyDisplay(str, Enum):
    DoNotDisplay = 'DoNotDisplay'
    Closed30Days = 'Closed30Days'
    Closed60Days = 'Closed60Days'
    Closed90Days = 'Closed90Days'
    Closed120Days = 'Closed120Days'
    AllClosed = 'AllClosed'

class PortalConfigurationProjectSetupModel(ConnectWiseModel):
    id: int
    portal_config: PortalConfigurationReferenceModel
    project_name_flag: bool
    project_type_flag: bool
    status_flag: bool
    project_manager_flag: bool
    billing_method_flag: bool
    contact_flag: bool
    estimated_start_flag: bool
    estimated_end_flag: bool
    description_flag: bool
    last_updated_flag: bool
    only_display: OnlyDisplay
    time_material_budget_hrs_flag: bool
    time_material_scheduled_start_flag: bool
    time_material_scheduled_finish_flag: bool
    time_material_scheduled_hrs_flag: bool
    time_material_actual_start_flag: bool
    time_material_actual_finish_flag: bool
    time_material_actual_hrs_flag: bool
    time_material_bill_flag: bool
    time_material_status_flag: bool
    time_material_assigned_flag: bool
    fixed_fee_budget_hrs_flag: bool
    fixed_fee_scheduled_start_flag: bool
    fixed_fee_scheduled_finish_flag: bool
    fixed_fee_scheduled_hrs_flag: bool
    fixed_fee_actual_start_flag: bool
    fixed_fee_actual_finish_flag: bool
    fixed_fee_actual_hrs_flag: bool
    fixed_fee_bill_flag: bool
    fixed_fee_status_flag: bool
    fixed_fee_assigned_flag: bool
    project_issue_budget_hrs_flag: bool
    project_issue_scheduled_start_flag: bool
    project_issue_scheduled_finish_flag: bool
    project_issue_scheduled_hrs_flag: bool
    project_issue_actual_start_flag: bool
    project_issue_actual_finish_flag: bool
    project_issue_actual_hrs_flag: bool
    project_issue_bill_flag: bool
    project_issue_status_flag: bool
    project_issue_assigned_flag: bool
    project_detail_total_hours_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True