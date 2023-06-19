from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.ProjectReferenceModel import ProjectReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel
from pyconnectwise.models.manage.GLExportExpenseOffsetModel import GLExportExpenseOffsetModel

class GLExportExpenseModel(ConnectWiseModel):
    id: int
    document_date: str
    document_type: str
    ap_account_number: str
    ap_class: str
    account_number: str
    gl_class: str
    gl_type_id: str
    memo: str
    description: str
    period_start_date: str
    period_end_date: str
    member: MemberReferenceModel
    vendor_number: str
    company: CompanyReferenceModel
    company_account_number: str
    project: ProjectReferenceModel
    currency: CurrencyReferenceModel
    total: float
    offset: GLExportExpenseOffsetModel

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True