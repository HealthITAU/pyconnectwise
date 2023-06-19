from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.IvItemReferenceModel import IvItemReferenceModel
from enum import Enum
from pyconnectwise.models.manage.OpportunityReferenceModel import OpportunityReferenceModel
from pyconnectwise.models.manage.InvoiceGroupingReferenceModel import InvoiceGroupingReferenceModel
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class BillCustomer(str, Enum):
    Billable = 'Billable'
    DoNotBill = 'DoNotBill'
    NoCharge = 'NoCharge'
class AgreementStatus(str, Enum):
    Active = 'Active'
    Cancelled = 'Cancelled'
    Expired = 'Expired'
    Inactive = 'Inactive'

class AdditionModel(ConnectWiseModel):
    id: int
    product: IvItemReferenceModel
    quantity: float
    less_included: float
    unit_price: float
    unit_cost: float
    bill_customer: BillCustomer
    effective_date: str
    cancelled_date: str
    taxable_flag: bool
    serial_number: str
    invoice_description: str
    purchase_item_flag: bool
    special_order_flag: bool
    agreement_id: int
    description: str
    billed_quantity: float
    uom: str
    ext_price: float
    ext_cost: float
    sequence_number: float
    margin: float
    prorate_cost: float
    prorate_price: float
    extended_prorate_cost: float
    extended_prorate_price: float
    prorate_current_period_flag: bool
    opportunity: OpportunityReferenceModel
    agreement_status: AgreementStatus
    invoice_grouping: InvoiceGroupingReferenceModel
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True