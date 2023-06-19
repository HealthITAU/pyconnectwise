from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.BoardReferenceModel import BoardReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel

class IntegratorLoginModel(ConnectWiseModel):
    id: int
    username: str
    password: str
    can_access_all_records_flag: bool
    can_access_all_apis_flag: bool
    inactive_flag: bool
    date_inactivated: str
    inactivated_by: MemberReferenceModel
    service_ticket_api_flag: bool
    board: BoardReferenceModel
    service_board_callback_url: str
    service_board_legacy_callback_flag: bool
    time_entry_api_flag: bool
    member: MemberReferenceModel
    time_entry_callback_url: str
    time_entry_legacy_callback_flag: bool
    managed_services_api_flag: bool
    managed_services_auto_child_flag: bool
    managed_services_childing_flag: bool
    contact_api_flag: bool
    contact_callback_url: str
    contact_legacy_callback_flag: bool
    company_api_flag: bool
    company_callback_url: str
    company_legacy_callback_flag: bool
    activity_api_flag: bool
    activity_callback_url: str
    activity_legacy_callback_flag: bool
    invoice_api_flag: bool
    product_api_flag: bool
    product_callback_url: str
    product_legacy_callback_flag: bool
    opportunity_api_flag: bool
    opportunity_callback_url: str
    opportunity_legacy_callback_flag: bool
    opportunity_conversion_api_flag: bool
    member_api_flag: bool
    marketing_api_flag: bool
    purchasing_api_flag: bool
    purchasing_callback_url: str
    purchasing_legacy_callback_flag: bool
    reporting_api_flag: bool
    system_api_flag: bool
    project_api_flag: bool
    project_callback_url: str
    project_legacy_callback_flag: bool
    configuration_api_flag: bool
    configuration_auto_child_flag: bool
    configuration_childling_flag: bool
    configuration_callback_url: str
    configuration_legacy_callback_flag: bool
    schedule_api_flag: bool
    schedule_callback_url: str
    schedule_legacy_callback_flag: bool
    agreement_api_flag: bool
    agreement_callback_url: str
    agreement_callback_legacy_flag: bool
    document_api_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True