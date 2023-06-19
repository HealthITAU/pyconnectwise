from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.IvItemReferenceModel import IvItemReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.UnitOfMeasureReferenceModel import UnitOfMeasureReferenceModel
from pyconnectwise.models.manage.ProductSubCategoryReferenceModel import ProductSubCategoryReferenceModel
from pyconnectwise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pyconnectwise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel
from pyconnectwise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pyconnectwise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from pyconnectwise.models.manage.GLExportInventoryTransferOffsetModel import GLExportInventoryTransferOffsetModel

class GLExportInventoryTransferModel(ConnectWiseModel):
    id: str
    document_type: str
    document_date: str
    account_number: str
    gl_class: str
    gl_type_id: str
    description: str
    sales_code: str
    memo: str
    cost_account_number: str
    inventory_account_number: str
    transfer_id: int
    item: IvItemReferenceModel
    gl_item_id: str
    sales_description: str
    item_description: str
    currency: CurrencyReferenceModel
    item_price: float
    taxable: bool
    unit_of_measure: UnitOfMeasureReferenceModel
    quantity: float
    cost: float
    total: float
    sub_category: ProductSubCategoryReferenceModel
    serialized_flag: bool
    serial_numbers: str
    bin: WarehouseBinReferenceModel
    warehouse: WarehouseReferenceModel
    transfer_from_bin: WarehouseBinReferenceModel
    transfer_from_location_xref: str
    transfer_to_bin: WarehouseBinReferenceModel
    transfer_to_location_xref: str
    location_xref: str
    price_level_xref: str
    uom_schedule_xref: str
    item_type_xref: str
    inventory_xref: str
    cogs_xref: str
    tax_note: str
    offset: GLExportInventoryTransferOffsetModel

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True