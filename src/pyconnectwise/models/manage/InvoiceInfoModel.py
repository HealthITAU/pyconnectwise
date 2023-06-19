from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.InvoiceModel import InvoiceModel
from pyconnectwise.models.manage.InvoiceTemplateModel import InvoiceTemplateModel
from pyconnectwise.models.manage.ProductItemModel import ProductItemModel
from pyconnectwise.models.manage.ProductComponentModel import ProductComponentModel
from pyconnectwise.models.manage.ExpenseEntryModel import ExpenseEntryModel
from pyconnectwise.models.manage.TimeEntryModel import TimeEntryModel
from pyconnectwise.models.manage.DocumentInfoModel import DocumentInfoModel
from pyconnectwise.models.manage.BillingSetupModel import BillingSetupModel
from pyconnectwise.models.manage.AgreementBillingInfoModel import AgreementBillingInfoModel

class InvoiceInfoModel(ConnectWiseModel):
    id: int
    invoice: InvoiceModel
    invoice_template: InvoiceTemplateModel
    products: list[ProductItemModel]
    bundled_components_info: list[ProductComponentModel]
    expenses: list[ExpenseEntryModel]
    time_entries: list[TimeEntryModel]
    logo: DocumentInfoModel
    billing_setup: BillingSetupModel
    agreement_billing_info: list[AgreementBillingInfoModel]
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True