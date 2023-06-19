from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
from pyconnectwise.models.manage.ServiceSignoffReferenceModel import ServiceSignoffReferenceModel
from pyconnectwise.models.manage.ServiceSignoffReferenceModel import ServiceSignoffReferenceModel
class DisplayClosedTicketsOption(str, Enum):
    DoNotDisplay = 'DoNotDisplay'
    Closed30Days = 'Closed30Days'
    Closed60Days = 'Closed60Days'
    Closed90Days = 'Closed90Days'
    Closed120Days = 'Closed120Days'
    AllClosed = 'AllClosed'

class PortalConfigurationServiceSetupModel(ConnectWiseModel):
    id: int
    service_type_flag: bool
    service_sub_type_flag: bool
    service_sub_type_item_flag: bool
    status_flag: bool
    site_name_flag: bool
    entered_date_flag: bool
    last_update_flag: bool
    required_date_flag: bool
    contact_flag: bool
    assigned_resources_flag: bool
    sla_info_flag: bool
    service_board_flag: bool
    budget_hours_flag: bool
    actual_hours_flag: bool
    approval_status_flag: bool
    open_tasks_flag: bool
    closed_tasks_flag: bool
    enable_chat_assist_flag: bool
    display_closed_tickets_option: DisplayClosedTicketsOption
    time_materials_ticket_template: ServiceSignoffReferenceModel
    fixed_fee_ticket_template: ServiceSignoffReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True