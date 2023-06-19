from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ClassificationReferenceModel import ClassificationReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel

class GLExportExpenseBillDetailModel(ConnectWiseModel):
    id: list[int]
    document_date: str
    gl_type_id: str
    memo: str
    company: CompanyReferenceModel
    account_number: str
    expense_class: ClassificationReferenceModel
    currency: CurrencyReferenceModel
    total: float
    billable: bool
    reimbursable: bool
    company_advance: bool

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True