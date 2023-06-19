from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.GLExportSettingsModel import GLExportSettingsModel
from pyconnectwise.models.manage.GLExportVendorModel import GLExportVendorModel
from pyconnectwise.models.manage.GLExportCustomerModel import GLExportCustomerModel
from pyconnectwise.models.manage.GLExportTransactionModel import GLExportTransactionModel
from pyconnectwise.models.manage.GLExportExpenseModel import GLExportExpenseModel
from pyconnectwise.models.manage.GLExportExpenseBillModel import GLExportExpenseBillModel
from pyconnectwise.models.manage.GLExportPurchaseTransactionModel import GLExportPurchaseTransactionModel
from pyconnectwise.models.manage.GLExportAdjustmentTransactionModel import GLExportAdjustmentTransactionModel
from pyconnectwise.models.manage.GLExportInventoryTransferModel import GLExportInventoryTransferModel

class GLExportModel(ConnectWiseModel):
    export_settings: GLExportSettingsModel
    vendors: list[GLExportVendorModel]
    customers: list[GLExportCustomerModel]
    transactions: list[GLExportTransactionModel]
    expenses: list[GLExportExpenseModel]
    expense_bills: list[GLExportExpenseBillModel]
    purchase_transactions: list[GLExportPurchaseTransactionModel]
    adjustment_transactions: list[GLExportAdjustmentTransactionModel]
    inventory_transfers: list[GLExportInventoryTransferModel]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True