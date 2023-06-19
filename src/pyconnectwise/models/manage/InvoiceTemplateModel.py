from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from enum import Enum
class HeaderLogoPosition(str, Enum):
    Center = 'Center'
    LeftSide = 'LeftSide'
    RightSide = 'RightSide'
class HeaderAddressPosition(str, Enum):
    Center = 'Center'
    LeftSide = 'LeftSide'
    RightSide = 'RightSide'
class HeaderTitlePosition(str, Enum):
    Center = 'Center'
    LeftSide = 'LeftSide'
    RightSide = 'RightSide'
class HeaderTitleFont(str, Enum):
    Regular = 'Regular'
    RegularBold = 'RegularBold'
    Large = 'Large'
    LargeBold = 'LargeBold'
    ExtraLarge = 'ExtraLarge'
    ExtraLargeBold = 'ExtraLargeBold'

class InvoiceTemplateModel(ConnectWiseModel):
    id: int
    name: str
    margin_left: float
    margin_right: float
    margin_top: float
    margin_bottom: float
    logo_visible_flag: bool
    header_logo_position: HeaderLogoPosition
    remit_to_visible_flag: bool
    header_address_position: HeaderAddressPosition
    header_title_visible_flag: bool
    header_title_caption: str
    header_title_position: HeaderTitlePosition
    header_title_font: HeaderTitleFont
    header_terms_visible_flag: bool
    header_terms_caption: str
    header_due_date_visible_flag: bool
    header_due_date_caption: str
    header_po_number_visible_flag: bool
    header_po_number_caption: str
    header_reference_visible_flag: bool
    header_reference_caption: str
    header_account_visible_flag: bool
    header_account_caption: str
    header_tax_id_visible_flag: bool
    header_tax_id_caption: str
    header_ship_to_visible_flag: bool
    header_ship_to_caption: str
    header_hours_based_extended_amount_visible_flag: bool
    payable_caption: str
    service_header_ticket_number_visible_flag: bool
    service_header_ticket_number_caption: str
    service_header_company_name_visible_flag: bool
    service_header_company_name_caption: str
    service_header_summary_visible_flag: bool
    service_header_summary_caption: str
    service_header_contact_name_visible_flag: bool
    service_header_contact_name_caption: str
    service_header_detail_description_visible_flag: bool
    service_header_detail_description_caption: str
    service_header_resolution_visible_flag: bool
    service_header_resolution_caption: str
    service_header_amount_visible_flag: bool
    service_header_amount_caption: str
    service_header_billing_method_visible_flag: bool
    service_header_billing_method_caption: str
    service_header_closed_tasks_visible_flag: bool
    service_header_open_tasks_visible_flag: bool
    service_header_bundled_tickets_visible_flag: bool
    project_header_project_name_visible_flag: bool
    project_header_project_name_caption: str
    project_header_company_name_visible_flag: bool
    project_header_company_name_caption: str
    project_header_original_downpayment_visible_flag: bool
    project_header_original_downpayment_caption: str
    project_header_contact_name_visible_flag: bool
    project_header_contact_name_caption: str
    project_header_amount_visible_flag: bool
    project_header_amount_caption: str
    project_header_billing_method_visible_flag: bool
    project_header_billing_method_caption: str
    project_header_billing_type_visible_flag: bool
    project_header_billing_type_caption: str
    invoice_payment_amount_visible_flag: bool
    invoice_payment_amount_caption: str
    invoice_credit_amount_visible_flag: bool
    invoice_credit_amount_caption: str
    invoice_balance_due_visible_flag: bool
    invoice_balance_due_caption: str
    credit_credit_amount_visible_flag: bool
    credit_credit_amount_caption: str
    credit_remaining_amount_visible_flag: bool
    credit_remaining_amount_caption: str
    time_detail_visible_flag: bool
    time_detail_primary_sort_field: str
    time_detail_primary_sort_direction: str
    time_detail_secondary_sort_field: str
    time_detail_secondary_sort_direction: str
    time_detail_subtotal_visible_flag: bool
    time_detail_start_end_time_visible_flag: bool
    time_detail_hours_visible_flag: bool
    time_detail_members_visible_flag: bool
    time_detail_billable_visible_flag: bool
    time_detail_extended_amount_visible_flag: bool
    time_detail_dollar_amounts_on_hourse_based_visible_flag: bool
    time_detail_hourly_rate_visible_flag: bool
    time_detail_contacts_visible_flag: bool
    time_detail_notes_visible_flag: bool
    time_detail_non_billable_caption: str
    time_detail_agreement_visible_flag: bool
    time_detail_hours_based_hours_visible_flag: bool
    time_detail_hours_based_ext_amount_visible_flag: bool
    time_detail_hoursbased_hourly_rate_visible_flag: bool
    time_detail_amount_based_hours_visible_flag: bool
    time_detail_amount_based_ext_amount_visible_flag: bool
    time_detail_amount_based_hourly_rate_visible_flag: bool
    time_detail_s_r_ticket_summary_visible_flag: bool
    time_detail_s_r_contact_visible_flag: bool
    time_detail_s_r_address_visible_flag: bool
    time_detail_pm_phase_visible_flag: bool
    time_detail_pm_summary_visible_flag: bool
    time_detail_ticket_number_visible_flag: bool
    time_detail_dates_visible_flag: bool
    services_staff_caption: str
    services_staff_visible_flag: bool
    services_amount_caption: str
    services_amount_visible_flag: bool
    services_hours_caption: str
    services_hours_visible_flag: bool
    services_rate_caption: str
    services_rate_visible_flag: bool
    services_work_role_caption: str
    services_work_role_visible_flag: bool
    services_work_type_caption: str
    services_work_type_visible_flag: bool
    services_total_visible_flag: bool
    services_member_name_visible_flag: bool
    services_member_name_caption: str
    currency_id_visible_flag: bool
    currency_symbol_visible_flag: bool
    portal_flag: bool
    services_collapsed_flag: bool
    expenses_collapsed_flag: bool
    other_charges_collapsed_flag: bool
    expenses_type_caption: str
    expenses_staff_caption: str
    expenses_amount_caption: str
    expenses_type_visible_flag: bool
    expenses_staff_visible_flag: bool
    expenses_amount_visible_flag: bool
    expenses_total_visible_flag: bool
    expense_detail_subtotal_visible_flag: bool
    expense_detail_members_visible_flag: bool
    expense_detail_contacts_visible_flag: bool
    expense_detail_billable_visible_flag: bool
    expense_detail_ext_amount_visible_flag: bool
    expense_detail_notes_visible_flag: bool
    expense_detail_primary_sort_field: str
    expense_detail_primary_sort_direction: str
    expense_detail_secondary_sort_field: str
    expense_detail_secondary_sort_direction: str
    expense_detail_nonbillable_caption: str
    expense_detail_visible_flag: bool
    expense_detail_agreement_visible_flag: bool
    expense_detail_agreement_ext_amount_visible_flag: bool
    expense_detail_ticket_number_visible_flag: bool
    expense_detail_sr_ticket_summary_visible_flag: bool
    expense_detail_sr_contact_visible_flag: bool
    expense_detail_sr_address_visible_flag: bool
    expense_detail_pm_phase_visible_flag: bool
    expense_detail_pm_summary_visible_flag: bool
    other_charges_amount_caption: str
    other_charges_amount_visible_flag: bool
    other_charges_description_caption: str
    other_charges_description_visible_flag: bool
    other_charges_display_six_decimals: bool
    other_charges_item_id_visible_flag: bool
    other_charges_price_caption: str
    other_charges_price_visible_flag: bool
    other_charges_quantity_caption: str
    other_charges_quantity_visible_flag: bool
    other_charges_serial_number_visible_flag: bool
    other_charges_total_visible_flag: bool
    adjustment_description_visible_flag: bool
    adjustment_description_caption: str
    adjustment_quantity_visible_flag: bool
    adjustment_quantity_caption: str
    adjustment_amount_visible_flag: bool
    adjustment_amount_caption: str
    adjustment_agr_type_visible_flag: bool
    adjustment_total_visible_flag: bool
    adjustment_price_visible_flag: bool
    adjustment_price_caption: str
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True