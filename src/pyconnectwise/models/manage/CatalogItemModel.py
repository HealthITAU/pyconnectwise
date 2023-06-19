from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ProductSubCategoryReferenceModel import ProductSubCategoryReferenceModel
from pyconnectwise.models.manage.ProductTypeReferenceModel import ProductTypeReferenceModel
from enum import Enum
from pyconnectwise.models.manage.UnitOfMeasureReferenceModel import UnitOfMeasureReferenceModel
from pyconnectwise.models.manage.ManufacturerReferenceModel import ManufacturerReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.SLAReferenceModel import SLAReferenceModel
from pyconnectwise.models.manage.EntityTypeReferenceModel import EntityTypeReferenceModel
from pyconnectwise.models.manage.BillingCycleReferenceModel import BillingCycleReferenceModel
from pyconnectwise.models.manage.ProductCategoryReferenceModel import ProductCategoryReferenceModel
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class ProductClass(str, Enum):
    Agreement = 'Agreement'
    Bundle = 'Bundle'
    Inventory = 'Inventory'
    NonInventory = 'NonInventory'
    Service = 'Service'
class PriceAttribute(str, Enum):
    FixedFee = 'FixedFee'
    NotToExceed = 'NotToExceed'
    OverrideRate = 'OverrideRate'
    TimeAndMaterials = 'TimeAndMaterials'
class RecurringCycleType(str, Enum):
    ContractYear = 'ContractYear'
    CalendarYear = 'CalendarYear'

class CatalogItemModel(ConnectWiseModel):
    id: int
    identifier: str
    description: str
    inactive_flag: bool
    subcategory: ProductSubCategoryReferenceModel
    type: ProductTypeReferenceModel
    product_class: ProductClass
    serialized_flag: bool
    serialized_cost_flag: bool
    phase_product_flag: bool
    unit_of_measure: UnitOfMeasureReferenceModel
    min_stock_level: int
    price: float
    cost: float
    price_attribute: PriceAttribute
    taxable_flag: bool
    drop_ship_flag: bool
    special_order_flag: bool
    customer_description: str
    manufacturer: ManufacturerReferenceModel
    manufacturer_part_number: str
    vendor: CompanyReferenceModel
    vendor_sku: str
    notes: str
    integration_x_ref: str
    sla: SLAReferenceModel
    entity_type: EntityTypeReferenceModel
    recurring_flag: bool
    recurring_revenue: float
    recurring_cost: float
    recurring_one_time_flag: bool
    recurring_bill_cycle: BillingCycleReferenceModel
    recurring_cycle_type: RecurringCycleType
    date_entered: str
    calculated_price_flag: bool
    calculated_cost_flag: bool
    category: ProductCategoryReferenceModel
    calculated_price: float
    calculated_cost: float
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True