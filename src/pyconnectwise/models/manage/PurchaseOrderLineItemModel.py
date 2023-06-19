from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.IvItemReferenceModel import IvItemReferenceModel
from pyconnectwise.models.manage.ShipmentMethodReferenceModel import ShipmentMethodReferenceModel
from pyconnectwise.models.manage.UnitOfMeasureReferenceModel import UnitOfMeasureReferenceModel
from pyconnectwise.models.manage.WarehouseReferenceModel import WarehouseReferenceModel
from pyconnectwise.models.manage.WarehouseBinReferenceModel import WarehouseBinReferenceModel
from enum import Enum
from pyconnectwise.models.manage.CustomFieldValueModel import CustomFieldValueModel
class ReceivedStatus(str, Enum):
    Waiting = 'Waiting'
    FullyReceived = 'FullyReceived'
    PartiallyReceiveCancelRest = 'PartiallyReceiveCancelRest'
    PartiallyReceiveCloneRest = 'PartiallyReceiveCloneRest'

class PurchaseOrderLineItemModel(ConnectWiseModel):
    id: int
    backordered_flag: bool
    canceled_by: str
    canceled_flag: bool
    canceled_reason: str
    closed_flag: bool
    date_canceled: str
    date_canceled_utc: str
    description: str
    display_internal_notes_flag: bool
    expected_ship_date: str
    internal_notes: str
    line_number: int
    packing_slip: str
    product: IvItemReferenceModel
    purchase_order_id: int
    quantity: float
    received_quantity: int
    serial_numbers: str
    ship_date: str
    shipment_method: ShipmentMethodReferenceModel
    tax: float
    tracking_number: str
    unit_cost: float
    unit_of_measure: UnitOfMeasureReferenceModel
    vendor_order_number: str
    vendor_sku: str
    warehouse: WarehouseReferenceModel
    warehouse_bin: WarehouseBinReferenceModel
    ship_set: str
    date_received: str
    received_status: ReceivedStatus
    _info: dict[str, str]
    custom_fields: list[CustomFieldValueModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True