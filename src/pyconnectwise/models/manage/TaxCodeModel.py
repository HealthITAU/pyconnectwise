from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CountryReferenceModel import CountryReferenceModel
from enum import Enum
class LevelOneRateType(str, Enum):
    Amount = 'Amount'
    Percent = 'Percent'
class LevelTwoRateType(str, Enum):
    Amount = 'Amount'
    Percent = 'Percent'
class LevelThreeRateType(str, Enum):
    Amount = 'Amount'
    Percent = 'Percent'
class LevelFourRateType(str, Enum):
    Amount = 'Amount'
    Percent = 'Percent'
class LevelFiveRateType(str, Enum):
    Amount = 'Amount'
    Percent = 'Percent'
class LevelSixRateType(str, Enum):
    Amount = 'Amount'
    Percent = 'Percent'

class TaxCodeModel(ConnectWiseModel):
    id: int
    identifier: str
    description: str
    invoice_caption: str
    country: CountryReferenceModel
    effective_date: str
    default_flag: bool
    display_on_invoice_flag: bool
    canada_calculate_g_s_t_flag: bool
    cancel_date: str
    level_one_rate: float
    level_one_rate_type: LevelOneRateType
    level_one_taxable_max: float
    level_one_caption: str
    level_one_tax_code_xref: str
    level_one_agency_xref: str
    level_one_services_flag: bool
    level_one_expenses_flag: bool
    level_one_products_flag: bool
    level_one_apply_single_unit_flag: bool
    level_one_apply_single_unit_min: float
    level_one_apply_single_unit_max: float
    level_two_rate: float
    level_two_rate_type: LevelTwoRateType
    level_two_taxable_max: float
    level_two_caption: str
    level_two_tax_code_xref: str
    level_two_agency_xref: str
    level_two_services_flag: bool
    level_two_expenses_flag: bool
    level_two_products_flag: bool
    level_two_apply_single_unit_flag: bool
    level_two_apply_single_unit_min: float
    level_two_apply_single_unit_max: float
    level_three_rate: float
    level_three_rate_type: LevelThreeRateType
    level_three_taxable_max: float
    level_three_caption: str
    level_three_tax_code_xref: str
    level_three_agency_xref: str
    level_three_services_flag: bool
    level_three_expenses_flag: bool
    level_three_products_flag: bool
    level_three_apply_single_unit_flag: bool
    level_three_apply_single_unit_min: float
    level_three_apply_single_unit_max: float
    level_four_rate: float
    level_four_rate_type: LevelFourRateType
    level_four_taxable_max: float
    level_four_caption: str
    level_four_tax_code_xref: str
    level_four_agency_xref: str
    level_four_services_flag: bool
    level_four_expenses_flag: bool
    level_four_products_flag: bool
    level_four_apply_single_unit_flag: bool
    level_four_apply_single_unit_min: float
    level_four_apply_single_unit_max: float
    level_five_rate: float
    level_five_rate_type: LevelFiveRateType
    level_five_taxable_max: float
    level_five_caption: str
    level_five_tax_code_xref: str
    level_five_agency_xref: str
    level_five_services_flag: bool
    level_five_expenses_flag: bool
    level_five_products_flag: bool
    level_five_apply_single_unit_flag: bool
    level_five_apply_single_unit_min: float
    level_five_apply_single_unit_max: float
    level_six_rate: float
    level_six_rate_type: LevelSixRateType
    level_six_taxable_max: float
    level_six_caption: str
    level_six_tax_code_xref: str
    level_six_agency_xref: str
    level_six_services_flag: bool
    level_six_expenses_flag: bool
    level_six_products_flag: bool
    level_six_apply_single_unit_flag: bool
    level_six_apply_single_unit_min: float
    level_six_apply_single_unit_max: float
    work_role_ids: list[int]
    add_all_work_roles: bool
    remove_all_work_roles: bool
    expense_type_ids: list[int]
    add_all_expense_types: bool
    remove_all_expense_types: bool
    product_type_ids: list[int]
    add_all_product_types: bool
    remove_all_product_types: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True