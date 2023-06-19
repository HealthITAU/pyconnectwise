from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.OpportunityReferenceModel import OpportunityReferenceModel
from pyconnectwise.models.manage.OpportunityStatusReferenceModel import OpportunityStatusReferenceModel
from pyconnectwise.models.manage.IvItemReferenceModel import IvItemReferenceModel
from enum import Enum
from pyconnectwise.models.manage.BillingCycleReferenceModel import BillingCycleReferenceModel
class ForecastType(str, Enum):
    Other1 = 'Other1'
    Other2 = 'Other2'
    Agreement = 'Agreement'
    Product = 'Product'
    Service = 'Service'

class ForecastItemModel(ConnectWiseModel):
    id: int
    forecast_description: str
    opportunity: OpportunityReferenceModel
    quantity: float
    status: OpportunityStatusReferenceModel
    catalog_item: IvItemReferenceModel
    product_description: str
    product_class: str
    revenue: float
    cost: float
    margin: float
    percentage: int
    include_flag: bool
    quote_werks_doc_no: str
    quote_werks_doc_name: str
    quote_werks_quantity: int
    forecast_type: ForecastType
    link_flag: bool
    recurring_revenue: float
    recurring_cost: float
    recurring_date_start: str
    recurring_date_end: str
    bill_cycle: BillingCycleReferenceModel
    cycle_basis: str
    cycles: int
    recurring_flag: bool
    sequence_number: float
    sub_number: int
    taxable_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True