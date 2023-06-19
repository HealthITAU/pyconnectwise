from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ReportCardReferenceModel import ReportCardReferenceModel
from enum import Enum
from pyconnectwise.models.manage.MemberTypeReferenceModel import MemberTypeReferenceModel
from pyconnectwise.models.manage.TimeZoneSetupReferenceModel import TimeZoneSetupReferenceModel
from pyconnectwise.models.manage.CountryReferenceModel import CountryReferenceModel
from pyconnectwise.models.manage.DocumentReferenceModel import DocumentReferenceModel
from pyconnectwise.models.manage.MemberOffice365Model import MemberOffice365Model
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.WorkRoleReferenceModel import WorkRoleReferenceModel
from pyconnectwise.models.manage.WorkTypeReferenceModel import WorkTypeReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.BoardReferenceModel import BoardReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.ProjectBoardReferenceModel import ProjectBoardReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.ServiceLocationReferenceModel import ServiceLocationReferenceModel
from pyconnectwise.models.manage.CalendarReferenceModel import CalendarReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel
from pyconnectwise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class LicenseClass(str, Enum):
    A = 'A'
    C = 'C'
    F = 'F'
    X = 'X'
class DefaultEmail(str, Enum):
    Office = 'Office'
    Mobile = 'Mobile'
    Home = 'Home'
class DefaultPhone(str, Enum):
    Office = 'Office'
    Mobile = 'Mobile'
    Home = 'Home'
class CompanyActivityTabFormat(str, Enum):
    SummaryList = 'SummaryList'
    DetailList = 'DetailList'
class InvoiceTimeTabFormat(str, Enum):
    SummaryList = 'SummaryList'
    DetailList = 'DetailList'
class InvoiceScreenDefaultTabFormat(str, Enum):
    ShowInvoicingTab = 'ShowInvoicingTab'
    ShowAgreementInvoicingTab = 'ShowAgreementInvoicingTab'
class InvoicingDisplayOptions(str, Enum):
    RemainOnInvoicingScreen = 'RemainOnInvoicingScreen'
    ShowRecentInvoices = 'ShowRecentInvoices'
class AgreementInvoicingDisplayOptions(str, Enum):
    RemainOnInvoicingScreen = 'RemainOnInvoicingScreen'
    ShowRecentInvoices = 'ShowRecentInvoices'
class AuthenticationServiceType(str, Enum):
    AuthAnvil = 'AuthAnvil'
    GoogleAuthenticator = 'GoogleAuthenticator'
    Email = 'Email'
class GlobalSearchDefaultTicketFilter(str, Enum):
    OpenRecords = 'OpenRecords'
    ClosedRecords = 'ClosedRecords'
    AllRecords = 'AllRecords'
class GlobalSearchDefaultSort(str, Enum):
    NONE = 'NONE'
    LastUpdatedDesc = 'LastUpdatedDesc'
    LastUpdatedAsc = 'LastUpdatedAsc'
    CreatedDesc = 'CreatedDesc'
    CreatedAsc = 'CreatedAsc'
class PhoneIntegrationType(str, Enum):
    TAPI = 'TAPI'
    SKYPE = 'SKYPE'
    NONE = 'NONE'

class MyAccountModel(ConnectWiseModel):
    id: int
    identifier: str
    password: str
    first_name: str
    middle_initial: str
    last_name: str
    title: str
    report_card: ReportCardReferenceModel
    license_class: LicenseClass
    disable_online_flag: bool
    enable_mobile_flag: bool
    type: MemberTypeReferenceModel
    employee_identifer: str
    vendor_number: str
    notes: str
    time_zone: TimeZoneSetupReferenceModel
    country: CountryReferenceModel
    service_board_team_ids: list[int]
    enable_mobile_gps_flag: bool
    inactive_date: str
    inactive_flag: bool
    last_login: str
    photo: DocumentReferenceModel
    partner_portal_flag: bool
    client_id: str
    sts_user_admin_url: str
    token: str
    toast_notification_flag: bool
    member_personas: list[int]
    office365: MemberOffice365Model
    office_email: str
    office_phone: str
    office_extension: str
    mobile_email: str
    mobile_phone: str
    mobile_extension: str
    home_email: str
    home_phone: str
    home_extension: str
    default_email: DefaultEmail
    primary_email: str
    default_phone: DefaultPhone
    default_location: SystemLocationReferenceModel
    default_department: SystemDepartmentReferenceModel
    reports_to: MemberReferenceModel
    work_role: WorkRoleReferenceModel
    work_type: WorkTypeReferenceModel
    time_approver: MemberReferenceModel
    expense_approver: MemberReferenceModel
    billable_forecast: float
    daily_capacity: float
    include_in_utilization_reporting_flag: bool
    require_expense_entry_flag: bool
    require_time_sheet_entry_flag: bool
    require_start_and_end_time_on_time_entry_flag: bool
    allow_in_cell_entry_on_time_sheet: bool
    enter_time_against_company_flag: bool
    allow_expenses_entered_against_companies_flag: bool
    time_reminder_email_flag: bool
    days_tolerance: int
    minimum_hours: float
    time_sheet_start_date: str
    hire_date: str
    service_default_location: SystemLocationReferenceModel
    service_default_department: SystemDepartmentReferenceModel
    service_default_board: BoardReferenceModel
    project_default_location: SystemLocationReferenceModel
    project_default_department: SystemDepartmentReferenceModel
    project_default_board: ProjectBoardReferenceModel
    schedule_default_location: SystemLocationReferenceModel
    schedule_default_department: SystemDepartmentReferenceModel
    schedule_capacity: float
    service_location: ServiceLocationReferenceModel
    hide_member_in_dispatch_portal_flag: bool
    calendar: CalendarReferenceModel
    sales_default_location: SystemLocationReferenceModel
    warehouse: WarehouseReferenceModel
    warehouse_bin: WarehouseBinReferenceModel
    mapi_name: str
    calendar_sync_integration_flag: bool
    company_activity_tab_format: CompanyActivityTabFormat
    invoice_time_tab_format: InvoiceTimeTabFormat
    invoice_screen_default_tab_format: InvoiceScreenDefaultTabFormat
    invoicing_display_options: InvoicingDisplayOptions
    agreement_invoicing_display_options: AgreementInvoicingDisplayOptions
    authentication_service_type: AuthenticationServiceType
    timebased_one_time_password_activated: bool
    auto_start_stopwatch: bool
    auto_popup_quick_notes_with_stopwatch: bool
    signature: str
    global_search_default_ticket_filter: GlobalSearchDefaultTicketFilter
    global_search_default_sort: GlobalSearchDefaultSort
    phone_source: str
    phone_integration_type: PhoneIntegrationType
    use_browser_language_flag: bool
    _info: dict[str, str]
    copy_pod_layouts: bool
    copy_shared_default_views: bool
    copy_column_layouts_and_filters: bool
    from_member_rec_id: int
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True