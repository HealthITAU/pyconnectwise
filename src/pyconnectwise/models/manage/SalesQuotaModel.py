from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.ProductCategoryReferenceModel import ProductCategoryReferenceModel
from pyconnectwise.models.manage.ProductSubCategoryReferenceModel import ProductSubCategoryReferenceModel
from pyconnectwise.models.manage.CurrencyReferenceModel import CurrencyReferenceModel

class SalesQuotaModel(ConnectWiseModel):
    id: int
    member: MemberReferenceModel
    forecast_year: int
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    category: ProductCategoryReferenceModel
    sub_category: ProductSubCategoryReferenceModel
    january_revenue: float
    january_margin: float
    february_revenue: float
    february_margin: float
    march_revenue: float
    march_margin: float
    april_revenue: float
    april_margin: float
    may_revenue: float
    may_margin: float
    june_revenue: float
    june_margin: float
    july_revenue: float
    july_margin: float
    august_revenue: float
    august_margin: float
    september_revenue: float
    september_margin: float
    october_revenue: float
    october_margin: float
    november_revenue: float
    november_margin: float
    december_revenue: float
    december_margin: float
    currency: CurrencyReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True